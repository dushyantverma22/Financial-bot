
from backened.analytics.portfolio_analytics import PortfolioAnalytics


class AnalyticsAgent:

    def __init__(self, db_path):

        self.analytics = PortfolioAnalytics(
            db_path
        )

    def answer(self, question):

        question = question.lower()

        if "summary" in question:

            return self.analytics.get_portfolio_summary()

        if "winner" in question:

            return self.analytics.get_biggest_winner()

        if "loser" in question:

            return self.analytics.get_biggest_loser()

        if "sector" in question:

            return self.analytics.get_sector_allocation()

        if "risk" in question:

            return self.analytics.get_concentration_risk()

        return None
