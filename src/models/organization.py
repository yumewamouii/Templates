from src.models.base_model import BaseModel
from src.models.settings import Settings
from src.utils.fields import ValidatedField


class Organization(BaseModel):
    name = ValidatedField(str, max_length = 50, default = 'Рога и копыта', nullable = False)
    tin = ValidatedField(int, length = 12, default = 123456789012, nullable = False)
    bic = ValidatedField(int, length = 9, blank = True)
    account = ValidatedField(int, length = 11, blank = True)
    ownership_type = ValidatedField(str, strip = True, length = 5, blank = True)


    def __init__(self, settings: Settings | None = None):
        if settings is not None:
            company_data = settings.company
            if company_data is not None:
                self.name = company_data.name
                self.tin = company_data.tin
                self.bic = company_data.bic
                self.account = company_data.account
                self.ownership_type = company_data.ownership_type
