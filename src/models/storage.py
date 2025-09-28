from src.models.base_model import BaseModel
from src.utils.fields import ValidatedField


class Storage(BaseModel):
    #id = ValidatedField(str, nullable = False, blank = False)
    name = ValidatedField(str, strip = True, max_length = 50, nullable = False, blank = False, default = 'Storage')


    def __str__(self):
        return (f'<Storage id={self.id} name={self.name}>')