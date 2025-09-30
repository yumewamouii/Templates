import uuid


from src.models.base_model import BaseModel
from src.utils.fields import ValidatedField


class Company(BaseModel):
    id = ValidatedField(str, nullable=False, blank = False)
    name = ValidatedField(str, strip = True, default = 'Рога и копыта', nullable = False)
    tin = ValidatedField(int, length = 12, default = 123456789012, nullable = False)
    account = ValidatedField(int, length = 11, blank = True)
    corr_account = ValidatedField(int, length = 11, blank = True)
    bic = ValidatedField(int, length = 9, blank = True)
    ownership_type = ValidatedField(str, strip = True, length = 5, blank = True)


    def __init__(self):
        super().__init__()
        self.id = str(uuid.uuid4().hex)


    def __str__(self):
        return (f"Identification number: {self.id}\n"
                f"TIN: {self.tin}\n"
                f"Account: {self.account}\n"
                f"Correspondent account: {self.corr_account}\n"
                f"BIC: {self.bic}\n"
                f"Name: {self.name}\n"
                f"Ownership type: {self.ownership_type}")
    

    def __repr__(self):
        return self.__str__()

