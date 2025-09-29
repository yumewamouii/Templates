from src.models.base_model import BaseModel
from src.utils.fields import ValidatedField


class Storage(BaseModel):
    id = ValidatedField(str, strip = True, nullable = False, blank = False)
    name = ValidatedField(str, strip = True, nullable = False, blank = False, default = 'Storage')