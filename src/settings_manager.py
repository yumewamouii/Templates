import os
import json


from src.models.settings import Settings


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
    def load_from_json(self, path: str = os.path.join(os.pardir, __filename)) -> None:
        try:
            if not isinstance(path, str): 
                raise Exception('File path must be a string.')
            if not os.path.exists(path):
                raise Exception(f'File {path} does not exist.')
            with open(path, 'r', encoding='utf-8') as f:
                file = json.load(f)
                for company_key, company_data in file.items():
                    for key, value in company_data.items():
                        if hasattr(self.__settings, key):
                            setattr(self.__settings, key, value)
        except:
            raise Exception('Failed to load settings from json file.')
    





