import pandas as pd

from backened.services.query_service import QueryService


class PortfolioAnalytics:

    def __init__(self, db_path):

        self.query_service = QueryService(db_path)

    def load_holdings(self):

        return self.query_service.execute_query(
            "SELECT * FROM holdings"
        )

    def get_portfolio_summary(self):

        df = self.load_holdings()

        return {

            "total_holdings":
                int(len(df)),

            "total_market_value":
                float(df["market_value"].sum()),

            "total_invested_value":
                float(df["invested_value"].sum()),

            "total_gain_loss":
                float(df["overall_gain_loss"].sum()),

            "portfolio_return_pct":
                round(
                    (
                        df["overall_gain_loss"].sum()
                        /
                        df["invested_value"].sum()
                    ) * 100,
                    2
                )
        }

    def get_top_holdings(
        self,
        top_n=5
    ):

        df = self.load_holdings()

        result = (
            df[
                [
                    "symbol",
                    "market_value"
                ]
            ]
            .sort_values(
                "market_value",
                ascending=False
            )
            .head(top_n)
        )

        return result.to_dict(
            orient="records"
        )

    def get_biggest_winner(self):

        df = self.load_holdings()

        winner = df.loc[
            df[
                "overall_gain_loss"
            ].idxmax()
        ]

        return {

            "symbol":
                str(
                    winner["symbol"]
                ),

            "gain":
                float(
                    winner[
                        "overall_gain_loss"
                    ]
                )
        }

    def get_biggest_loser(self):

        df = self.load_holdings()

        loser = df.loc[
            df[
                "overall_gain_loss"
            ].idxmin()
        ]

        return {

            "symbol":
                str(
                    loser["symbol"]
                ),

            "loss":
                float(
                    loser[
                        "overall_gain_loss"
                    ]
                )
        }

    def get_sector_allocation(self):

        df = self.load_holdings()

        allocation = (

            df.groupby(
                "sector"
            )[
                "market_value"
            ]
            .sum()
            .reset_index()

        )

        total = allocation[
            "market_value"
        ].sum()

        allocation[
            "allocation_pct"
        ] = (

            allocation[
                "market_value"
            ]

            / total

            * 100

        ).round(2)

        allocation = allocation.sort_values(
            "allocation_pct",
            ascending=False
        )

        return allocation.to_dict(
            orient="records"
        )

    def get_concentration_risk(self):

        df = self.load_holdings()

        total_market_value = (
            df[
                "market_value"
            ].sum()
        )

        largest_position = (
            df[
                "market_value"
            ].max()
        )

        weight = (

            largest_position

            /

            total_market_value

            * 100

        )

        if weight > 30:

            risk = "HIGH"

        elif weight > 20:

            risk = "MEDIUM"

        else:

            risk = "LOW"

        return {

            "largest_position_pct":
                round(
                    float(weight),
                    2
                ),

            "risk_level":
                risk
        }