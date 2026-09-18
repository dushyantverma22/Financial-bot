from langchain_openai import ChatOpenAI
from config.settings import OPENAI_API_KEY



from prompt.sql_prompt import (
    SQL_SYSTEM_PROMPT
)


class SQLGenerator:

    def __init__(self):

        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            api_key=OPENAI_API_KEY,
            temperature=0
        )

    def generate_sql(
        self,
        question,
        error_context=None
    ):

        prompt = f"""
        {SQL_SYSTEM_PROMPT}

        Question:
        {question}
        """

        if error_context:

            prompt += f"""

            Previous Error:
            {error_context}
            """

        response = self.llm.invoke(prompt)

        sql = response.content

        sql = sql.replace(
            "```sql",
            ""
        )

        sql = sql.replace(
            "```",
            ""
        )

        return sql.strip()