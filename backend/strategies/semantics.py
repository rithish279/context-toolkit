"""Semantic chunking using sentence embeddings"""

from typing import List, Dict, Any
import numpy as np
from sentence_transformers import SentenceTransformer
from .base import BaseStrategy

class SemanticChunkingStrategy(BaseStrategy):
    """Keep messages most semantically relevant to the question"""
    
    def __init__(self):
        super().__init__(name="Semantic Chunking")
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
    
    def apply(self, conversation: List[str], keep_top_n: int = 3, **kwargs) -> Dict[str, Any]:
        """Keep the N messages most relevant to the final question."""
        
        if len(conversation) <= keep_top_n + 1:
            return {
                "kept_messages": conversation,
                "metadata": {
                    "description": f"Keeps top {keep_top_n} semantically relevant messages",
                    "color": "#9b59b6",
                    "kept_count": len(conversation),
                    "total_messages": len(conversation)
                }
            }
        
        question = conversation[-1]
        history = conversation[:-1]
        
        # Encode question and all history messages
        question_embedding = self.model.encode(question)
        history_embeddings = self.model.encode(history)
        
        # Calculate cosine similarity
        similarities = []
        for hist_emb in history_embeddings:
            similarity = np.dot(question_embedding, hist_emb) / (
                np.linalg.norm(question_embedding) * np.linalg.norm(hist_emb)
            )
            similarities.append(float(similarity))  
        
        # Get indices of top N most similar messages
        top_indices_array = np.argsort(similarities)[-keep_top_n:]
        top_indices = sorted([int(idx) for idx in top_indices_array])  
        
        # Build kept messages
        kept = [history[i] for i in top_indices]
        kept.append(question)
        
        return {
            "kept_messages": kept,
            "metadata": {
                "description": f"Keeps top {keep_top_n} semantically relevant messages using embeddings",
                "color": "#9b59b6",
                "kept_count": len(kept),
                "total_messages": len(conversation),
                "similarity_scores": [round(similarities[i], 3) for i in top_indices]
            }
        }