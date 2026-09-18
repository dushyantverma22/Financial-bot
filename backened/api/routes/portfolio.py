from fastapi import APIRouter

router = APIRouter()

from backened.analytics.portfolio_analytics import (
    PortfolioAnalytics
)

analytics = PortfolioAnalytics(
    "data/portfolio.db"
)

@router.get(
    "/portfolio/summary"
)
def portfolio_summary():

    return analytics.get_portfolio_summary()
