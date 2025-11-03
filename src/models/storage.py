from src.models.base_model import BaseModel


from src.utils.fields import ValidatedField


class Storage(BaseModel):
    address = ValidatedField(expected_type = str, max_length = 255, strip = True, nullable = True, default = None)


    def __init__(self, address: str = None):
        super().__init__()


        self.address = address