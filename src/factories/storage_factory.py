from src.store.base_storage import BaseStorage


from src.exceptions.either import Either


from src.utils.response_factory import ResponseFactory


from src.store.recipe_storage import RecipeStorage
from src.store.nomenclature_storage import NomenclatureStorage
from src.store.nomenclature_group_storage import NomenclatureGroupStorage
from src.store.measurement_unit_storage import MeasurementUnitStorage


class StorageFactory:
    _storages_map = {
        'recipe': RecipeStorage(),
        'nomenclature': NomenclatureStorage(),
        'nomenclature_group': NomenclatureGroupStorage(),
        'unit': MeasurementUnitStorage()
    }


    @classmethod
    def get_storage(cls, model_name: str) -> Either[object, BaseStorage]:
        if model_name not in cls._storages_map:
            return Either.with_left(ResponseFactory.error('Unknown entity: {}'.format(model_name)))
        return Either.with_right(cls._storages_map.get(model_name))