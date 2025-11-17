from src.models.measurement_unit import MeasurementUnit


class MeasurementUnitsFactory:
    def get_units(self) -> list[MeasurementUnit]:
        return [
            self.g(),
            self.kg(),
            self.pcs(),
            self.tens(),
            self.ml(),
            self.l()
        ]
    

    def g(self) -> MeasurementUnit:
        return MeasurementUnit.create('g', 1)
    

    def kg(self) -> MeasurementUnit:
        return MeasurementUnit.create('kg', 1000, self.g())
    

    def pcs(self) -> MeasurementUnit:
        return MeasurementUnit.create('pcs', 1)


    def tens(self) -> MeasurementUnit:
        return MeasurementUnit.create('tens', 10, self.pcs())
    
    

    def ml(self) -> MeasurementUnit:
        return MeasurementUnit.create('ml', 1)
    

    def l(self) -> MeasurementUnit:
        return MeasurementUnit.create('l', 1000, self.ml())