import uuid


from src.models.base_model import BaseModel
from src.utils.fields import ValidatedField


class Company(BaseModel):
    id = ValidatedField(str, nullable=False , blank = False)
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
        return (f"Идентификационный номер: {self.id}\n"
                f"ИНН: {self.tin}\n"
                f"Счет: {self.account}\n"
                f"Корреспондентский счет: {self.corr_account}\n"
                f"БИК: {self.bic}\n"
                f"Наименование: {self.name}\n"
                f"Вид собственности: {self.ownership_type}")
    

    def __repr__(self):
        return self.__str__()

