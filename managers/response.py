from flask import Response


class ResponseManager():

    @staticmethod
    def error_response() -> Response:
        """
        Function to return error response
        """
        return Response({"massage": "this is error massage"}, status=400, mimetype='application/json')

    @staticmethod
    def success_response() -> Response:
        """
        Function to return success response
        """
        return Response({"massage": "this is success massage"}, status=200)
