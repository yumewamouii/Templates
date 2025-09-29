import os
import json

from src.models.settings import Settings
from src.utils.file_search import find_file
from src.utils.fields import ValidatedField
from src.exceptions.validation import ArgumentException, OperationException


class SettingManager:
    #Singleton manager for application settings

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(SettingManager, cls).__new__(cls)
            cls._instance.__filename = ''
            cls._instance.__settings = Settings()
        return cls._instance

    @property
    def settings(self) -> Settings:
        return self.__settings

    def load_from_json(self, filename: str = '') -> bool:
        if filename:
            self.__filename = filename

        full_name = find_file(filename=self.__filename)
        if full_name is None:
            raise ArgumentException(f'File {self.__filename} does not exist.')

        try:
            with open(full_name, 'r', encoding='utf-8') as file:
                data = json.load(file)
                if 'company' in data:
                    self.convert(data['company'])
                    return True
            raise ArgumentException(f'File {self.__filename} does not contain "company" section')
        except Exception as e:
            raise OperationException(f'Failed to load settings from json file: {e}')

    def convert(self, data: dict) -> None:
        data = ValidatedField(dict, nullable = True, blank = True)
        #if not isinstance(data, dict):
            #raise ArgumentException('Input data must be a dictionary')
        
        field_types = {
            'tin': int,
            'account': int,
            'corr_account': int,
            'bic': int,
            'name': str,
            'ownership_type': str
        }

        matching_keys = ['tin', 'account', 'corr_account', 'bic', 'name', 'ownership_type']

        for key in matching_keys:
            if key in data:
                value = data[key]
                expected_type = field_types[key]
                try:
                    value = expected_type(value) if value is not None else None
                    setattr(self.__settings.company, key, value)
                except Exception:
                    raise ArgumentException(f"Parameter {key} no in matching keys")

