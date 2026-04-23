from typing import List, Dict, Any
from .base import BaseStrategy

class SummarizeStrategy(BaseStrategy):
    def __init__(self):
        super().__init__(name="Summarize")
    
    def apply(self, conversation: List[str], **kwargs) -> Dict[str, Any]:
        if len(conversation) <= 4:
            kept = conversation
        else:
            
            kept = [
                conversation[0],
                f"[... {len(conversation) - 3} messages omitted ...]",
                conversation[-2],
                conversation[-1]
            ]
        
        return {
            "kept_messages": kept,
            "metadata": {
                "description": "Keeps first message + last 2 messages (compresses middle)",
                "color": "#ffe66d",
                "kept_count": len(kept),
                "total_messages": len(conversation)
            }
        }