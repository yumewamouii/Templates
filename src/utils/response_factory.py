from flask import make_response, jsonify

class ResponseFactory:
    """
    Factory for creating standardized HTTP responses.
    """

    @staticmethod
    def error(error: str, status_code: int = 400):
        """
        Creates a JSON error response with the given message and HTTP status.

        Args:
            error (str): Error message to include in the response.
            status_code (int, optional): HTTP status code. Defaults to 400.

        Returns:
            Response: Flask Response object with JSON payload and status code.
        """
        # jsonify ensures the response is proper JSON with content-type application/json
        response = make_response(jsonify({'error': error}))
        response.status_code = status_code
        return response
