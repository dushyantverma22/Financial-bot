class IntentClassifier:

    PORTFOLIO_KEYWORDS = {

        "portfolio",
        "holding",
        "stock",
        "sector",
        "gain",
        "loss",
        "market value",
        "investment",
        "quantity",
        "weightage"
    }

    def classify(self, question):

        question = question.lower()

        for keyword in self.PORTFOLIO_KEYWORDS:

            if keyword in question:

                return "portfolio"

        return "reject"