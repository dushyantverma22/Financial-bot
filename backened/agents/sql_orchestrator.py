from backened.agents.sql_generator import SQLGenerator
from backened.agents.intent_classifier import IntentClassifier

from backened.validators.sql_validator import SQLValidator

from backened.services.query_service import QueryService


class SQLOrchestrator:

    MAX_RETRIES = 5

    def __init__(self, db_path):

        self.generator = SQLGenerator()

        self.intent = IntentClassifier()

        self.query_service = QueryService(
            db_path
        )

    def ask(self, question):

        intent = self.intent.classify(
            question
        )

        if intent == "reject":

            return {
                "status": "rejected",
                "message":
                "Please ask portfolio related questions."
            }

        error_context = None

        for attempt in range(
            self.MAX_RETRIES
        ):

            try:

                sql = (
                    self.generator.generate_sql(
                        question,
                        error_context
                    )
                )

                SQLValidator.validate(sql)

                result = (
                    self.query_service
                    .execute_query(sql)
                )

                return {
                    "status": "success",
                    "sql": sql,
                    "result": result
                }

            except Exception as e:

                error_context = str(e)

        return {
            "status": "failed",
            "message":
            "Unable to process query after 5 attempts."
        }