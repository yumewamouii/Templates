import datetime


from src.exceptions.validation import ArgumentException


from src.models.settings import Settings


class SettingsMapper:
    @staticmethod
    def from_json(json: dict) -> Settings:
        if not isinstance(json, dict):
            raise ArgumentException(dict, type(json))
        

        settings = Settings(
            ownership_type = json['ownership_type'],
            tin = json['tin'],
            bic = json['bic'],
            account = json['account'],
            blocking_date = datetime.datetime.fromtimestamp(json['blocking_date'])
        )


        return settings
    

    @staticmethod
    def to_json(settings: Settings) -> dict:
        return {
            'ownership_type': settings.ownership_type,
            'tin': settings.tin,
            'bic': settings.bic,
            'account': settings.account,
            'blocking_date': settings.blocking_date.timestamp()
        }