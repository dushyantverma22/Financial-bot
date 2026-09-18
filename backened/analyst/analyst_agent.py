from langchain_openai import ChatOpenAI
from backened.config.settings import OPENAI_API_KEY

from backened.analyst.prompts import (
    FINANCIAL_ANALYST_PROMPT
)


class AnalystAgent:

    def __init__(self):

        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.2,
            api_key=OPENAI_API_KEY
        )

    def explain(
        self,
        question,
        result
    ):

        prompt = (
            FINANCIAL_ANALYST_PROMPT
            .format(
                question=question,
                result=result
            )
        )

        response = self.llm.invoke(
            prompt
        )

        return response.content