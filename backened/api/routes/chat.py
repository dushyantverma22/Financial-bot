from fastapi import APIRouter

from backened.graph.portfolio_graph import (
    portfolio_graph
)

from backened.api.schemas.chat import (
    ChatRequest
)

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):

    state = {

        "question":
            request.question,

        "intent": None,

        "sql_query": None,

        "raw_result": None,

        "explanation": None,

        "retry_count": 0,

        "error": None
    }

    result = portfolio_graph.invoke(
        state
    )

    return {

        "explanation":
            result["explanation"],

        "raw_result":
            result["raw_result"]
    }