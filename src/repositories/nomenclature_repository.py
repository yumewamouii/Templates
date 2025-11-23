from src.store.nomenclature_group_storage import NomenclatureGroupStorage
from src.store.nomenclature_storage import NomenclatureStorage


from src.exceptions.validation import ArgumentException


from src.models.nomenclature import Nomenclature
from src.models.nomenclature_group import NomenclatureGroup


class NomenclatureRepository:
    def __init__(
                 self, 
                 nomenclature_storage: NomenclatureStorage,
                 nomenclature_group_storage: NomenclatureGroupStorage,
                 start_nomenclature: list[Nomenclature],
                 start_nomenclature_group: list[NomenclatureGroup]
                 ):
        self._nomenclature_storage = nomenclature_storage
        self._nomenclature_group_storage = nomenclature_group_storage
        self._start_nomenclature = start_nomenclature
        self._start_nomenclature_group = start_nomenclature_group
    

    def get_nomenclature(self, nomenclature_id: str) -> Nomenclature | None:
        if not isinstance(nomenclature_id, str):
            raise ArgumentException(f'excepted str, you gave {type(nomenclature_id)}')
        

        return self._nomenclature_storage.get(nomenclature_id)
    

    def get_nomenclatures(self, offset: int = 0, limit: int | None = None) -> list[Nomenclature]:
        return self._nomenclature_storage.get_all(offset, limit)


    def get_nomenclature_groups(self, offset: int = 0, limit: int | None = None) -> list[NomenclatureGroup]:
        return self._nomenclature_group_storage.get_all(offset, limit)
    

    def init_start_nomenclature(self):
        if self._nomenclature_storage.is_empty():
            for recipe in self._start_nomenclature:
                self._nomenclature_storage.create(recipe)

        if self._nomenclature_group_storage.is_empty():
            for group in self._start_nomenclature_group:
                self._nomenclature_group_storage.create(group)