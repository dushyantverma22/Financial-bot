import sqlite3
from pathlib import Path


class SQLiteManager:

    def __init__(self, db_path="data/portfolio.db"):

        self.db_path = db_path

        Path("data").mkdir(exist_ok=True)

    def get_connection(self):

        return sqlite3.connect(self.db_path)

    def initialize_database(self):

        conn = self.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS holdings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT,
            company_name TEXT,
            isin TEXT,
            market_cap TEXT,
            sector TEXT,
            quantity INTEGER,
            avg_trading_price REAL,
            invested_value REAL,
            market_value REAL,
            overall_gain_loss REAL,
            holding_weightage REAL
        )
        """)

        conn.commit()
        conn.close()

        print("Database initialized successfully")