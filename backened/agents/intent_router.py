class IntentRouter:

    ANALYTICS_KEYWORDS = {

        "summary",
        "allocation",
        "risk",
        "diversification",
        "winner",
        "loser",
        "performance",
        "sector"
    }

    def classify(self, question):

        question = question.lower()

        for keyword in self.ANALYTICS_KEYWORDS:

            if keyword in question:

                return "analytics"

        return "data_query"