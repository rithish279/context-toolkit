# Abtract Class for All Strategies

from abc import ABC, abstractmethod
from typing import List, Dict, Any

class BaseStrategy(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply(self, conversation: List[str], **kwargs) -> Dict[str, Any]:
        """
        Apply strategy to conversation.
        
        Must return:
        {
            "kept_messages": List[str],
            "metadata": {"description": str, "color": str, ...}
        }
        """
        pass
    
    def get_info(self) -> Dict[str, Any]:
        """Return Strategy metadata"""
        
        return {
            "name": self.name,
            "type": self.__class__.__name__
        }