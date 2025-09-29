from typing import Any


from src.exceptions.validation import ArgumentException, OperationException


class Validator:
    @staticmethod
    def validate(value: Any, expected_type: object, length: int | None = None, max_length: int | None = None) -> bool:
        #if value is None:
            #raise ArgumentException('Empty argument')
        

        if not isinstance(value, expected_type):
            raise ArgumentException(f'Incorrect type. {expected_type} is expected. Current type is {type(value)}')
        

        if len(str(value).strip()) == 0:
            raise ArgumentException('This argument can not be blank')
        

        if length is not None and len(str(value).strip()) != length:
            raise ArgumentException(f'Incorrect length of argument. The length of this argument should be {length}')
        

        if max_length is not None and len(str(value).strip()) > max_length:
            raise ArgumentException(f'Incorrect length of argument. The length of this argument should be less of {max_length}')
        

        return True
