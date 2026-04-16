from typing import List, Dict, Any
from .base import BaseStrategy

class ImportantOnlyStrategy(BaseStrategy):
    def __init__(self):
        super().__init__(name="Important Only")
        self.keywords = ["name", "love", "like", "allerg", "allergic", "hate", "prefer"]
    
    def apply(self, conversation: List[str], **kwargs) -> Dict[str, Any]:
        important = []
        
        for msg in conversation:
            if any(k in msg.lower() for k in self.keywords):
                important.append(msg)
        
        if conversation and conversation[-1] not in important:
            important.append(conversation[-1])
        
        return {
            "kept_messages": important,
            "metadata": {
                "description": "Keeps messages with important keywords (names, preferences, allergies)",
                "color": "#4ecdc4",
                "kept_count": len(important),
                "keywords_used": self.keywords
            }
        }