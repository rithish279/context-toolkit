from .recent import RecentOnlyStrategy
from .important import ImportantOnlyStrategy
from .summarize import SummarizeStrategy

ALL_STRATEGIES = [
    RecentOnlyStrategy(),
    ImportantOnlyStrategy(),
    SummarizeStrategy()
]

def get_all_strategies():
    return ALL_STRATEGIES
