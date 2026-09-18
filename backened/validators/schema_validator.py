class SchemaValidator:

    ALLOWED_COLUMNS = {

        "symbol",
        "company_name",
        "isin",
        "market_cap",
        "sector",
        "quantity",
        "avg_trading_price",
        "invested_value",
        "market_value",
        "overall_gain_loss",
        "holding_weightage"
    }

    @staticmethod
    def validate(sql):

        return True