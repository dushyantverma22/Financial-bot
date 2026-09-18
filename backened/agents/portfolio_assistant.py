from backened.agents.intent_router import IntentRouter
from backened.agents.analytics_agent import AnalyticsAgent
from backened.agents.sql_orchestrator import SQLOrchestrator

class PortfolioAssistant:

    def __init__(self, db_path):

        self.router = IntentRouter()

        self.analytics = AnalyticsAgent(
            db_path
        )

        self.sql = SQLOrchestrator(
            db_path
        )

    def ask(self, question):

        intent = self.router.classify(
            question
        )

        if intent == "analytics":

            return self.analytics.answer(
                question
            )

        return self.sql.ask(question)