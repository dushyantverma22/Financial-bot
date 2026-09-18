from backened.agents.sql_generator import SQLGenerator

generator = SQLGenerator()

def sql_generation_node(state):

    sql = generator.generate_sql(
        question=state["question"],
        error_context=state["error"]
    )

    state["sql_query"] = sql

    return state