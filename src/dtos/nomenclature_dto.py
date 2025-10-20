from dataclasses import dataclass


from src.dtos.base_dto import BaseDTO



@dataclass
class NomenclatureDTO(BaseDTO):
    id: str
    fullname: str
    nomenclature_group_id: str
    measurement_unit_id: str