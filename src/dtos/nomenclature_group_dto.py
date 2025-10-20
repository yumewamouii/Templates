from dataclasses import dataclass


from src.dtos.base_dto import BaseDTO


@dataclass
class NomenclatureGroupDTO(BaseDTO):
    id: str
    fullname: str