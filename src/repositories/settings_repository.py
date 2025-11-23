import json
import os


from src.mappers.absolute_mapper import AbsoluteMapper


from src.exceptions.validation import ArgumentException


from src.mappers.settings_mapper import SettingsMapper


from src.models.settings import Settings


class SettingsRepository:
    @staticmethod
    def load_from_file(file_name: str) -> Settings:
        if not isinstance(file_name, str):
            raise ArgumentException(str, type(file_name))
        

        full_name = os.path.abspath(file_name)


        with open(full_name, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            settings = SettingsMapper.from_json(json_data)
        

        return settings
    

    @staticmethod
    def save_to_file(file_name: str, settings: Settings) -> bool:
        if not isinstance(file_name, str):
            raise ArgumentException(str, type(file_name))
        if not isinstance(settings, Settings):
            raise ArgumentException(Settings, type(settings))
        

        try:
            full_name = os.path.abspath(file_name)
            with open(full_name, 'w', encoding = 'utf-8') as f:
                json_data = AbsoluteMapper.to_dict(settings)
                json.dump(json_data, f)
                return True
        except:
            return False