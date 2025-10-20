from src.models.nomenclature_group import NomenclatureGroup


from src.dtos.nomenclature_group_dto import NomenclatureGroupDTO


from src.utils.validator import Validator


class NomenclatureGroupMapper:
    @staticmethod
    def from_dto(dto: NomenclatureGroupDTO, cache: dict):
        Validator.validate(dto, NomenclatureGroupDTO)
        Validator.validate(cache, dict)


        item = NomenclatureGroup()
        item.id = dto.id
        item.name = dto.fullname


        return item