
from langgraph.graph import StateGraph, END, START


from backened.graph.state import PortfolioState
from backened.graph.nodes.intent_node import intent_node
from backened.graph.nodes.analytics_node import analytics_node
from backened.graph.nodes.sql_generation_node import sql_generation_node
from backened.graph.nodes.sql_validator_node import sql_validation_node
from backened.graph.nodes.sql_execution_node import sql_execution_node
from backened.graph.nodes.analyst_node import analyst_node
from backened.graph.nodes.error_node import error_node

from backened.graph.routing.router import route_intent, route_sql_result

workflow = StateGraph(
    PortfolioState
)

workflow.add_node(
    "intent",
    intent_node
)

workflow.add_node(
    "analytics",
    analytics_node
)

workflow.add_node(
    "sql_generation",
    sql_generation_node
)

workflow.add_node(
    "sql_validation",
    sql_validation_node
)

workflow.add_node(
    "sql_execution",
    sql_execution_node
)

workflow.add_node(
    "analyst",
    analyst_node
)

workflow.add_node(
    "error",
    error_node
)

workflow.add_edge(
    START,
    "intent"
)

workflow.add_conditional_edges(
    "intent",
    route_intent,
    {
        "analytics":
            "analytics",

        "sql":
            "sql_generation",

        "reject":
            END
    }
)

workflow.add_edge(
    "analytics",
    "analyst"
)

workflow.add_edge(
    "sql_generation",
    "sql_validation"
)

workflow.add_edge(
    "sql_validation",
    "sql_execution"
)

workflow.add_conditional_edges(
    "sql_execution",
    route_sql_result,
    {
        "success": "analyst",
        "retry": "sql_generation",
        "error": "error"
    }
)

workflow.add_edge(
    "analyst",
    END
)

workflow.add_edge(
    "error",
    END
)

portfolio_graph = workflow.compile()


