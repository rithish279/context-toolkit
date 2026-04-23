from typing import List, Dict, Any
from .base import BaseStrategy

class RecentOnlyStrategy(BaseStrategy):

    def __init__(self):
        super().__init__(name="Recent Only")

    def apply(self, conversation: List[str], keep_last: int = 2, **kwargs) -> Dict[str, Any]:

        kept = conversation[-keep_last:]

        return {
            "kept_messages": kept,
            "metadata": {
                "description": f"Keeps only the last {keep_last} messages",
                "color": "#ff6b6b",
                "kept_count": len(kept),
                "total_messages": len(conversation)
            }
        }