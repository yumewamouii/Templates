from src.store.base_memory_storage import BaseMemoryStorage


from src.models.measurement_unit import MeasurementUnit


class MeasurementUnitStorage(BaseMemoryStorage[str, MeasurementUnit]):
    pass