from backened.services.query_service import QueryService

query_service = QueryService("data/portfolio.db"
)


def sql_execution_node(state):

    try:

        result = query_service.execute_query(
            state["sql_query"]
        )

        state["raw_result"] = result

        state["error"] = None

    except Exception as e:

        state["error"] = str(e)

        state["retry_count"] += 1

    return state