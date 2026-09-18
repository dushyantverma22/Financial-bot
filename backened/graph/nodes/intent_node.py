from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os   

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY")
)

def intent_node(state):

    question = state["question"]

    prompt = f"""
    Classify this question into one of below intents:

    analytics: if the question is related to portfolio analytics, such as summary, allocation, risk, diversification, winner, loser, performance, sector.
    sql: if the question is related to querying the portfolio database.
    reject: if the question is not related to the portfolio.

    Examples:

    Am I diversified?
    -> analytics

    What is my portfolio summary?
    -> analytics

    Show top 5 holdings.
    -> sql

    Which stocks have gains above 10000?
    -> sql

    Who won IPL?
    -> reject

    Return only one word.

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    state["intent"] = (
        response.content
        .strip()
        .lower()
    )

    return state