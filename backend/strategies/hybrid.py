"""Hybrid strategy combining semantic relevance + recency"""

from typing import List, Dict, Any
import numpy as np
from sentence_transformers import SentenceTransformer
from .base import BaseStrategy

class HybridStrategy(BaseStrategy):
    """Combines semantic relevance with recency bias"""
    
    def __init__(self):
        super().__init__(name="Hybrid (Semantic + Recent)")
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
    
    def apply(self, conversation: List[str], keep_top_n: int = 3, **kwargs) -> Dict[str, Any]:
        """
        Keep messages that are either:
        1. Semantically relevant to the question
        2. Very recent (last 2 messages)
        """
        if len(conversation) <= keep_top_n + 1:
            return {
                "kept_messages": conversation,
                "metadata": {
                    "description": "Combines semantic relevance with recency bias",
                    "color": "#e74c3c",
                    "kept_count": len(conversation),
                    "total_messages": len(conversation)
                }
            }
        
        question = conversation[-1]
        history = conversation[:-1]
        
        # Always keep the last 2 messages before the question
        always_keep_count = min(2, len(history))
        always_keep_indices = set(range(len(history) - always_keep_count, len(history)))
        
        # For older messages, use semantic similarity
        if len(history) > always_keep_count:
            older_history = history[:-always_keep_count]
            
            question_embedding = self.model.encode([question])[0]
            older_embeddings = self.model.encode(older_history)
            
            # Calculate similarities
            similarities = []
            for emb in older_embeddings:
                similarity = np.dot(question_embedding, emb) / (
                    np.linalg.norm(question_embedding) * np.linalg.norm(emb)
                )
                similarities.append(float(similarity))  # Convert to Python float
            
            # Keep top semantic matches from older messages
            semantic_keep_count = max(1, keep_top_n - always_keep_count)
            top_indices_array = np.argsort(similarities)[-semantic_keep_count:]
            
            # Convert numpy array to Python list of ints
            top_semantic_indices = [int(idx) for idx in top_indices_array]
            
            # Combine indices
            all_keep_indices = sorted(set(top_semantic_indices) | always_keep_indices)
        else:
            all_keep_indices = sorted(list(always_keep_indices))
        
        # Build kept messages
        kept = [history[i] for i in all_keep_indices]
        kept.append(question)
        
        return {
            "kept_messages": kept,
            "metadata": {
                "description": f"Keeps {keep_top_n} messages: recent + semantically relevant",
                "color": "#e74c3c",
                "kept_count": len(kept),
                "total_messages": len(conversation),
                "strategy": "hybrid (semantic + recency)"
            }
        }