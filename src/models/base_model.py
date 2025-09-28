import uuid
#from src.handlers.validator import Validator


from src.models.abstract_base_model import AbstractBaseModel
from src.utils.fields import ValidatedField


class BaseModel(AbstractBaseModel):
    id = ValidatedField(str, strip = True, default = lambda: str(uuid.uuid4().hex), nullable = False)
    def __init__(self):
        super().__init__()


#The comparison with id, other can be a UUID string
    def __eq__(self, other: str) -> bool:
        if isinstance(other, str):
            return self.id == other
        return False

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id}>"
