from src.models.measurement_unit import MeasurementUnit


class MeasurementUnitRepository:
    def __init__(self):
        self.__cache: dict[str, MeasurementUnit] = {}
    

    def get_or_create(self, name: str, factor: int = 1, base: 'MeasurementUnit' | None = None) -> 'MeasurementUnit':
        key = name.lower()
        if key not in self.__cache:
            self.__cache[key] = MeasurementUnit.create(name = name, factor = factor,
                                                       base = base)
        return self.__cache[key]


    def create_g(self) -> MeasurementUnit:
        return self.get_or_create('g')
    

    def create_kg(self) -> MeasurementUnit:
        g = self.create_g()
        return self.get_or_create('kg', 1000, g)
    

    def create_pcs(self) -> MeasurementUnit:
        return self.get_or_create('pcs')


    def all(self) -> list['MeasurementUnit']:
        return list(self.__cache.values())