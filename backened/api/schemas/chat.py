from pydantic import BaseModel
from typing import Any

class ChatRequest(BaseModel):
    question: str



class ChatResponse(BaseModel):
    explanation: str
    raw_result: Any

