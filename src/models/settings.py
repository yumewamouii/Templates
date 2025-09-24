class Settings:
    # Properties with default values
    __tin = ''
    __account = ''
    __corr_account = ''
    __bic = ''
    __name = ''
    __ownership_type = ''

    # TIN
    @property
    def tin(self) -> str:
        return self.__tin

    @tin.setter
    def tin(self, value: str) -> str:
        if isinstance(int(value), int) and isinstance(value, str) and len(value) == 12:
            self.__tin = value
        else:
            raise ValueError('TIN must be a number and contain 12 characters.')

    # Account
    @property
    def account(self) -> str:
        return self.__account

    @account.setter
    def account(self, value: str) -> str:
        if isinstance(int(value), int) and isinstance(value, str) and len(value) == 11:
            self.__account = value
        else:
            raise ValueError('account must be a number and contain 11 characters.')

    # Correspondent account
    @property
    def corr_account(self) -> str:
        return self.__corr_account

    @corr_account.setter
    def corr_account(self, value: str) -> str:
        if isinstance(int(value), int) and isinstance(value, str) and len(value) == 11:
            self.__corr_account = value
        else:
            raise ValueError('correspondent account must be a number and contain 11 characters.')
    # BIC
    @property
    def bic(self) -> str:
        return self.__bic

    @bic.setter
    def bic(self, value: str) -> str:
        if isinstance(int(value), int) and isinstance(value, int) and len(value) == 9:
            self.__bic = value
        else:
            raise ValueError("BIC must be a number and contain 9 characters.")

    # Наименование
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> str:
        if isinstance(value, str):
            self.__name = value
        else:
            raise ValueError("name must be string.")

    # Вид собственности
    @property
    def ownership_type(self) -> str:
        return self.__ownership_type

    @ownership_type.setter
    def ownership_type(self, value: str) -> str:
        if isinstance(value, str) and len(value) == 5:
            self.__ownership_type = value
        else:
            raise ValueError("ownership type must be string and contain 5 characters.")

    def __str__(self):
        return (f"ИНН: {self.__tin}\n"
                f"Счет: {self.__account}\n"
                f"Корреспондентский счет: {self.__corr_account}\n"
                f"БИК: {self.__bic}\n"
                f"Наименование: {self.__name}\n"
                f"Вид собственности: {self.__ownership_type}")