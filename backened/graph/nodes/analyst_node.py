from backened.analyst.analyst_agent import AnalystAgent

analyst_agent = AnalystAgent()

def analyst_node(state):

    explanation = analyst_agent.explain(
        state["question"],
        state["raw_result"]
    )

    state["explanation"] = explanation

    return state