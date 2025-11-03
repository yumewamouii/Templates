import unittest


from src.models.measured_value import MeasuredValue
from src.models.measurement_unit import MeasurementUnit
from src.utils.grouping import Grouping


class TestGroupingPrototype(unittest.TestCase):
    def setUp(self):
        self.data = [
            MeasuredValue(1, MeasurementUnit('g', 1000)),
            MeasuredValue(10, MeasurementUnit('g', 1000)),
            MeasuredValue(1, MeasurementUnit('l', 1)),
        ]

    def test_nested_grouping(self):
        res = list(Grouping.group(self.data, ['unit.name']))
        self.assertEqual(len(res), 2)

    def test_multiple_parameters_grouping(self):
        res = list(Grouping.group(self.data, ['value', 'unit.name']))
        self.assertEqual(len(res), 3)