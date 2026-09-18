def error_node(state):

    if state["error"]:

        state["explanation"] = (
            f"Request failed: {state['error']}"
        )

    else:

        state["explanation"] = (
            "Please ask a portfolio-related question."
        )

    return state