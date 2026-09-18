from typing import TypedDict, Any, Optional, List, Dict

class PortfolioState(TypedDict):

    question: str

    intent: Optional[str]

    sql_query: Optional[str]

    raw_result: Optional[Any]

    explanation: Optional[str]

    retry_count: int

    error: Optional[str]