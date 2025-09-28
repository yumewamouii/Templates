import unittest


from src.models.measurement_unit import MeasurementUnit


class TestMeasurementUnit(unittest.TestCase):
    def setUp(self):
        self.measurement_unit = MeasurementUnit()
        self.measurement_unit_first = MeasurementUnit()
        self.measurement_unit_second = MeasurementUnit()
    

    def test_create_measurement_unit(self):
        self.assertIsInstance(self.measurement_unit, MeasurementUnit)
    

    def test_not_equal_measurement_units(self):
        self.assertNotEqual(self.measurement_unit_first, self.measurement_unit_second)
    

    def test_not_equal_ids_measurement_units(self):
        self.assertNotEqual(self.measurement_unit_first.id, self.measurement_unit_second.id)
    

    def test_equal_properties_without_id_measurement_units(self):
        self.assertEqual((self.measurement_unit_first.basic_unit, self.measurement_unit_first.conversion_factor),
                          (self.measurement_unit_second.basic_unit, self.measurement_unit_second.conversion_factor))
    

    def test_range_model_first(self):
        g = self.measurement_unit.range_model('g')
        self.assertEqual(f'{g.basic_unit} {g.conversion_factor}', 'g 1')
    


    def test_range_model_second(self):
        g = self.measurement_unit.range_model('g')
        kg = self.measurement_unit.range_model('kg', 1000, g)
        self.assertEqual(f'{kg.basic_unit} {kg.conversion_factor}', 'g 1000')
    