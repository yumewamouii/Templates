from src.models.base_model import BaseModel
from src.utils.fields import ValidatedField


class NomenclatureGroup(BaseModel):
    name = ValidatedField(str, max_length = 50, default = '', nullable = False, blank = True)
