from src.models.company import Company
from src.utils.fields import ValidatedField


class Settings:
    def __init__(self):
        self.company = Company()
    

    def __str__(self):
        return f"Settings of company:\n{self.company}"


    def __repr__(self):
        return f"<Settings of company={repr(self.company)}>"