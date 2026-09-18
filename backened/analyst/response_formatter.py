import json


class ResponseFormatter:

    @staticmethod
    def format_result(result):

        if hasattr(
            result,
            "to_dict"
        ):

            result = result.to_dict(
                orient="records"
            )

        return json.dumps(
            result,
            indent=2,
            default=str
        )