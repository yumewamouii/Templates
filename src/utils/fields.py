from typing import Any


from src.utils.validator import Validator
from src.exceptions.validation import ArgumentException

'''This class validates fields by type, fixed length, 
        maximum length, empty value, missing value, and default value.'''
class ValidatedField:
    def __init__(self, expected_type: object, length: int | None = None, max_length: int | None = None, strip: bool = False,
                nullable: bool = False, default: Any | None = None, blank: bool = False):
        self.__expected_type = expected_type
        self.__length = length
        self.__max_length = max_length
        self.__strip = strip
        self.__nullable = nullable
        self.__default = default
        self.__blank = blank
        self.__private_name = None
    
    #Immediately sets the name of the field as private
    def __set_name__(self, owner: type, namefield: str) -> None:
        self.__private_name = f'__{owner.__name__}__{namefield}'

    #Returns the default value of the field. 
    #If the default value is callable, it calls the callable and returns the result.
    def __get_default(self):
        if callable(self.__default):
            return self.__default()
        return self.__default
    

# Returns the field value or default, raising ArgumentException when rules are violated
    def __get__(self, obj: Any, obj_type: object = None) -> str:        
        if obj is None:
            return self
        if not hasattr(obj, self.__private_name):
            if self.__blank:
                if self.__expected_type == str:
                    return ''
                elif self.__expected_type == int:
                    return 0
            elif self.__default is not None:
                return self.__get_default()
            return None
        return getattr(obj, self.__private_name, self.__get_default())
    

# Sets the field value, enforcing type, blank/null rules, and validation.
    def __set__(self, obj: object, value: Any) -> None:
        if value is None and not self.__nullable:
            if self.__blank:
                if self.__expected_type == str:
                    setattr(obj, self.__private_name, '')
                    return
                elif self.__expected_type == int:
                    setattr(obj, self.__private_name, 0)
                    return
            raise ArgumentException(f'Field can not be None')
        if value == 0:
            if self.__blank:
                setattr(obj, self.__private_name, 0)
                return
            raise ArgumentException('This argument can not be blank')
        if self.__blank and len(str(value).strip()) == 0:
            setattr(obj, self.__private_name, '')
            return
        Validator.validate(value, self.__expected_type, self.__length, self.__max_length)
        if self.__strip and isinstance(value, str):
            value = value.strip()
        elif isinstance(value, int):
            setattr(obj, self.__private_name, value)
            return
        setattr(obj, self.__private_name, value)


