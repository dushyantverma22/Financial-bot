class SQLValidator:

    FORBIDDEN = {

        "drop",
        "delete",
        "update",
        "insert",
        "alter",
        "truncate",
        "create",
        "attach",
        "detach"
    }

    @staticmethod
    def validate(sql):

        sql_lower = sql.lower()

        if not sql_lower.startswith(
            "select"
        ):
            raise ValueError(
                "Only SELECT queries allowed"
            )

        for keyword in SQLValidator.FORBIDDEN:

            if keyword in sql_lower:

                raise ValueError(
                    f"Forbidden keyword: {keyword}"
                )

        return True