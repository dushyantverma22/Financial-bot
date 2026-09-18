from backened.validators.sql_validator import SQLValidator

def sql_validation_node(state):

    try:

        SQLValidator.validate(
            state["sql_query"]
        )

        state["error"] = None

    except Exception as e:

        state["error"] = str(e)

    return state