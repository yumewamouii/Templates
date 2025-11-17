from dataclasses import dataclass


from src.dtos.base_dto import BaseDTO


from src.models.filter import Filter


@dataclass
class TransactionsRequestDto(BaseDTO):
    filters: list[Filter]
    date_from: int
    date_to: int