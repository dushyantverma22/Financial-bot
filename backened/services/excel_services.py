import sqlite3
import pandas as pd


class ExcelService:

    def __init__(self, file_path):

        self.file_path = file_path

    def load_holdings(self):
        raw_df = pd.read_excel( self.file_path, sheet_name="Portfolio", header=None ) 
        header_row = raw_df[ raw_df.iloc[:, 0] == "Scrip/Contract" ].index[0]
        holdings_df = pd.read_excel( self.file_path, sheet_name="Portfolio", header=header_row )
        holdings_df = holdings_df.dropna( subset=["Scrip/Contract"] )
        return holdings_df

    def save_to_database(self, holdings_df, conn):

        required_columns = {

            "Scrip/Contract": "symbol",
            "Company Name": "company_name",
            "ISIN": "isin",
            "MarketCap": "market_cap",
            "Sector": "sector",
            "Quantity": "quantity",
            "Avg Trading Price": "avg_trading_price",
            "Invested Value": "invested_value",
            "Market Value as of last trading day": "market_value",
            "Overall Gain/Loss": "overall_gain_loss",
            "Holding Weightage": "holding_weightage"
        }

        db_df = holdings_df[
            required_columns.keys()
        ].rename(columns=required_columns)

        db_df.to_sql(
            "holdings",
            conn,
            if_exists="replace",
            index=False
        )

        print(
            f"{len(db_df)} holdings inserted"
        )

    def ingest_to_sqlite(
        self,
        db_path
    ):

        conn = sqlite3.connect(db_path)

        holdings_df = self.load_holdings()

        self.save_to_database(
            holdings_df,
            conn
        )

        conn.close()

        return {
            "status": "success",
            "records_loaded":
                len(holdings_df)
        }