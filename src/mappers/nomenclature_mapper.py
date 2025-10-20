from src.models.nomenclature import Nomenclature


from src.dtos.nomenclature_dto import NomenclatureDTO


from src.utils.validator import Validator


class NomenclatureMapper:
    @staticmethod
    def from_dto(dto: NomenclatureDTO, cache: dict):
        Validator.validate(dto, NomenclatureDTO)
        Validator.validate(cache, dict)


        if dto.measurement_unit_id in cache:
            measurement_unit = cache[dto.measurement_unit_id]
        else:
            measurement_unit = None
        

        if dto.nomenclature_group_id in cache:
            nomenclature_group = cache[dto.nomenclature_group_id]
        else:
            nomenclature_group = None
        
        
        item = Nomenclature()
        item.id = dto.id
        item.fullname = dto.fullname
        item.nomenclature_group = nomenclature_group
        item.measurement_unit = measurement_unit


        return item