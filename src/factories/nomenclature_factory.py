from src.factories.measurement_units_factory import MeasurementUnitsFactory


from src.models.nomenclature import Nomenclature
from src.models.nomenclature_group import NomenclatureGroup


class NomenclatureFactory:
    def __init__(self, unitsFactory: MeasurementUnitsFactory):
        self._unitsFactory = unitsFactory
    

    def get_nomenclatures(self) -> list[Nomenclature]:
        return [
            self.wheat_flour(),
            self.milk(),
            self.egg(),
            self.sugar(),
            self.baking_powder()
        ]
    

    def get_nomenclature_groups(self) -> list[NomenclatureGroup]:
        return [
            self.nomenclature_group_food()
        ]


    def nomenclature_group_food(self) -> NomenclatureGroup:
        return NomenclatureGroup.create('Еда')
    

    def wheat_flour(self) -> Nomenclature:
        return Nomenclature.create('Пшеничная мука', self._unitsFactory.kg(), self.nomenclature_group_food())
    

    def milk(self) -> Nomenclature:
        return Nomenclature.create('Молоко', self._unitsFactory.l(), self.nomenclature_group_food())
    

    def egg(self) -> Nomenclature:
        return Nomenclature.create('Яйцо', self._unitsFactory.tens(), self.nomenclature_group_food())
    

    def sugar(self) -> Nomenclature:
        return Nomenclature.create('Сахар', self._unitsFactory.kg(), self.nomenclature_group_food())
    

    def baking_powder(self) -> Nomenclature:
        return Nomenclature.create('Разрыхлитель', self._unitsFactory.kg(), self.nomenclature_group_food())
