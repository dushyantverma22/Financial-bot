from backened.agents.analytics_agent import AnalyticsAgent

analytics_agent = AnalyticsAgent(
    "data/portfolio.db"
)

def analytics_node(state):

    result = analytics_agent.answer(
        state["question"]
    )

    state["raw_result"] = result

    return state

