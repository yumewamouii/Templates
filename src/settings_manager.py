import os
import json


from src.models.company_model import companyModel


class settingManager():
    __filename: str = ""
    __company: companyModel = None


    def __init__(self):
        self.set_default()
    

    @property
    def company(self) -> companyModel:
        return self.__company


    @property
    def filename(self) -> str:
        return self.__filename
    
    #Full path to settings file
    @filename.setter
    def filename(self, value: str):
        if value.strip() == '':
            return


        if os.path.exists(value):
            self.__filename = value.strip()
        else:
            raise Exception("File does not exist")
    

    #Load settings from json file
    def load(self) -> bool:
        if self.__filename.strip == '':
            raise Exception('File does not exist')
        try:
            with open(self.__filename.strip(), 'r') as file_instance:
                data = json.load(file_instance)


                if 'company' in data.keys():
                    item = data['company']
                    self.__company.name = item['name']
                    return True
            
            return False
        
        except:
            return False
    

    def set_default(self):
        self.__company = companyModel()
        self.__company.name = 'Рога и копыта'



