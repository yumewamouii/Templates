from src.exceptions.either import Either
from src.utils.response_factory import ResponseFactory
from src.serialization.model_serializer import ModelSerializer


class RequestParser:
    """
    Utility class for parsing incoming request JSON bodies into typed objects.
    Uses Either to encapsulate success or failure.
    """

    @staticmethod
    def parse_body(json: dict, json_type: type) -> Either:
        """
        Attempts to deserialize a JSON dictionary into an object of the given type.

        Args:
            json (dict): The JSON data from the request body.
            json_type (type): The type to deserialize the JSON into.

        Returns:
            Either: 
                - Right(value) containing the deserialized object on success.
                - Left(error) containing a ResponseFactory error response on failure.
        """
        serializer = ModelSerializer.get_json_serializer()
        try:
            # Attempt deserialization
            return Either.with_right(serializer.deserialize(json, json_type))
        except Exception as e:
            # Wrap any exception into a Left value containing an error response
            return Either.with_left(ResponseFactory.error(str(e), 400))
