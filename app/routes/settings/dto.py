import datetime


from src.models.base_model import BaseModel


class UpdateBlockingDateRequestDto(BaseModel):
    blocking_date: int


    @property
    def blocking_date(self) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(self.blocking_date)
    

    @blocking_date.setter
    def blocking_date(self, value: int):
        self.blocking_date = value