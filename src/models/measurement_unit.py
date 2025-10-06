from __future__ import annotations
import uuid



from src.models.base_model import BaseModel
from src.utils.fields import ValidatedField


class MeasurementUnit(BaseModel):
    name = ValidatedField(str, strip = True, nullable = False, max_length = 50)
    basic_unit = ValidatedField(str, strip = True, nullable = True, max_length = 50)
    conversion_factor = ValidatedField(int, nullable = False, blank = False, default = 1)


    @classmethod
    def create(cls, name: str, factor: int = 1, base: 'MeasurementUnit' | None = None) -> 'MeasurementUnit':
        """
        A universal factory method for creating measurement units.
        :param name: name of unit
        :param factor: conversion factor
        :param base: basic unit of measurement or None
        """

        unit = cls()
        unit.name = name


        if base is None:
            unit.basic_unit = name
            unit.conversion_factor = 1
        else:
            unit.basic_unit = base.basic_unit
            unit.conversion_factor = factor
        return unit
    

    @staticmethod
    def create_g() -> 'MeasurementUnit':
        return MeasurementUnit.create('g', 1)
    

    def create_kg() -> 'MeasurementUnit':
        g = MeasurementUnit.create_g()
        return MeasurementUnit.create('kg', 1000, g)


    def create_piece() -> 'MeasurementUnit':
        g = MeasurementUnit.create_g()
        return MeasurementUnit.create('piece', 55, g)
        


    def __str__(self):
        return (f'Identification number: {self.id}\n'
                f'Unit name: {self.name}\n'
                f'Basic unit of measurement: {self.basic_unit}\n'
                f'Conversion factor: {self.conversion_factor}')


