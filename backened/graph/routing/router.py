def route_intent(state):

    return state["intent"]

def route_sql_result(state):

    if state["error"]:

        if state["retry_count"] < 5:

            return "retry"

        return "error"

    return "success"