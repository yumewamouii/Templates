import json


from src.models.measurement_unit import MeasurementUnit
from src.models.nomenclature import Nomenclature
from src.models.nomenclature_group import NomenclatureGroup
from src.models.recipe import Recipe, Ingredient, RecipeStep


from src.dtos.measurement_unit_dto import MeasurementUnitDTO
from src.dtos.nomenclature_dto import NomenclatureDTO
from src.dtos.nomenclature_group_dto import NomenclatureGroupDTO
from src.dtos.ingredient_dto import IngredientDTO
from src.dtos.recipe_dto import RecipeDTO


from src.mappers.measurement_unit_mapper import MeasurementUnitMapper
from src.mappers.nomenclature_group_mapper import NomenclatureGroupMapper
from src.mappers.nomenclature_mapper import NomenclatureMapper
from src.mappers.ingredient_mapper import IngredientMapper
from src.mappers.recipe_mapper import RecipeMapper


from src.repository import Repository
from src.measurement_unit_repository import MeasurementUnitRepository
from src.utils.fields import ValidatedField
from src.utils.file_search import find_file
from src.utils.validator import Validator


from src.exceptions.validation import OperationException, ArgumentException


class StartService:
    _repository: Repository = Repository()
    _unit_repository: MeasurementUnitRepository = MeasurementUnitRepository()
    _cache = {}
    _recipe: Recipe

    # Ensure StartService is a singleton – only one instance will exist in the application.
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance
    

    def __init__(self):
        if getattr(self, 'initialized', False):
            return
        

        self._repository: Repository = Repository()
        self._unit_repository: MeasurementUnitRepository = MeasurementUnitRepository()
        self._cache = {}
        self._recipe: Recipe


        for key in (self._repository.range_measurement_unit_key(),
                    self._repository.range_nomenclature_group_key(),
                    self._repository.range_nomenclature_key(),
                    self._repository.range_recipe()):
            self._repository.data.setdefault(key, [])
        self.initialized = True

    def data(self) -> dict:
        # Expose repository data for inspection or testing
        return self._repository.data
    

    def load_settings(self, path: str = 'settings.json') -> dict:
        abs_path = find_file(filename = path)
        with open(abs_path, encoding = 'utf-8') as file:
            return json.load(file)
    

    def _save_item(self, key: str, dto, item):
        Validator.validate(key, str)
        item.unique_code = dto.id
        self._cache.setdefault(dto.id, item)
        self._repository.data[key].append(item)
    

    def _convert_measurement_units(self, data: dict) -> None:
        Validator.validate(data, dict)
        if 'measurement_units' in data:
            measurement_units = data['measurement_units']
        else:
            measurement_units = []
        

        if len(measurement_units) == 0:
            raise ArgumentException('Units of measurement are missing in the file')
        

        for unit in measurement_units:
            dto = MeasurementUnitDTO.create(unit)
            item = MeasurementUnitMapper.from_dto(dto, self._cache)
            self._save_item(self._repository.range_measurement_unit_key(), dto, item)
    

    def _convert_nomenclature_groups(self, data: dict) -> None:
        Validator.validate(data, dict)
        if 'nomenclature_groups' in data:
            nomenclature_groups = data['nomenclature_groups']
        else:
            nomenclature_groups = []
        

        if len(nomenclature_groups) == 0:
            raise ArgumentException('Groups of nomenclatures are missing in the file')
        

        for group in nomenclature_groups:
            dto = NomenclatureGroupDTO.create(group)
            item = NomenclatureGroupMapper.from_dto(dto, self._cache)
            self._save_item(self._repository.range_nomenclature_group_key(), dto, item)
    

    def _convert_nomenclatures(self, data: dict) -> None:
        Validator.validate(data, dict)
        if 'nomenclatures' in data:
            nomenclatures = data['nomenclatures']
        else:
            nomenclatures = []
        

        if len(nomenclatures) == 0:
            raise ArgumentException('Nomenclatures are missing in the file')


        for nomenclature in nomenclatures:
            dto = NomenclatureDTO.create(nomenclature)
            item = NomenclatureMapper.from_dto(dto, self._cache)
            self._save_item(self._repository.range_nomenclature_key(), dto, item)
    

    def convert_recipes(self, data: dict) -> None:
        Validator.validate(data, dict)
        if 'recipes' in data:
            recipes = data['recipes']
        else:
            recipes = []
        

        if len(recipes) == 0:
            raise ArgumentException('Recipes are missing in the file')
        

        for recipe_data in recipes:
            recipe_dto = RecipeDTO.create(recipe_data)
            recipe = RecipeMapper.from_dto(recipe_dto, self._cache)

            self._convert_measurement_units(recipe_data)
            self._convert_nomenclature_groups(recipe_data)
            self._convert_nomenclatures(recipe_data)

            self._save_item(self._repository.range_recipe(), recipe_dto, recipe)


    def start(self):
        filename = 'settings.json'
        settings = self.load_settings(filename)
        self.convert_recipes(settings)
    
