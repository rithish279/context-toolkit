import tiktoken
from typing import List

class TokenCounter:
    # NOTE: Using OpenAI tokenizer (cl100k_base) as an approximation
    # Actual token counts may differ from LLaMa models
    def __init__(self, model: str = "gpt-3.5-turbo"):
        self.encoding = tiktoken.get_encoding("cl100k_base")
    
    def count(self, text: str) -> int:
        return len(self.encoding.encode(text))
    
    def count_messages(self, messages: List[str]) -> int:
        return sum(self.count(msg) for msg in messages)
    
    def count_conversation(self, conversation: List[str]) -> int:
        return self.count_messages(conversation)