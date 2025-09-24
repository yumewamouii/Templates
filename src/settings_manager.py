import os
import json


from src.models.settings import Settings
from handlers.file_search import find_file


class settingManager():
    __filename: str = 'settings.json'
    __settings = Settings()

#Singleton pattern
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(settingManager, cls).__new__(cls)
        return cls.instance


    @property
    def settings(self) -> Settings:
        return self.__settings
    
    #Load properties of Settings class from dictionary
    def load_from_dict(self, curr_dict: dict) -> None:
        try:
            if not isinstance(curr_dict, dict):
                raise Exception('Not a dictionary')
            for company_key, company_data in curr_dict.items():
                for key, value in company_data.items():
                    if hasattr(self.__settings, key):
                        setattr(self.__settings, key, value)
        except:
            raise Exception()
    
    #Load properties of Settings class from json file
    def load_from_json(self, filename: str = ''):
        if not isinstance(filename, str):
            raise Exception('Filename must be string.')
        if filename != '':
            self.__filename = filename
        

        full_name = find_file(filename = self.__filename)
        if full_name is None:
            raise Exception(f'File {self.__filename} does not exist.')


        try:
            with open(full_name, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for company_key, company_data in data.items():
                    for key, value in company_data.items():
                        if hasattr(self.__settings, key):
                            setattr(self.__settings, key, value)
        except:
            raise Exception('Failed to load settings from json file')



