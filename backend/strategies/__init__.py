from .recent import RecentOnlyStrategy
from .important import ImportantOnlyStrategy
from .summarize import SummarizeStrategy
from .semantics import SemanticChunkingStrategy
from .hybrid import HybridStrategy

ALL_STRATEGIES = [
    RecentOnlyStrategy(),
    ImportantOnlyStrategy(),
    SummarizeStrategy(),
    SemanticChunkingStrategy(),
    HybridStrategy()
]

def get_all_strategies():
    return ALL_STRATEGIES
