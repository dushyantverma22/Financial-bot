import sqlite3
import pandas as pd


class QueryService:

    def __init__(self, db_path):

        self.db_path = db_path

    def get_schema(self):

        conn = sqlite3.connect(self.db_path)

        schema = pd.read_sql(
            """
            PRAGMA table_info(holdings)
            """,
            conn
        )

        conn.close()

        return schema

    def execute_query(self, sql):

        conn = sqlite3.connect(self.db_path)

        result = pd.read_sql_query(
            sql,
            conn
        )

        conn.close()

        return result