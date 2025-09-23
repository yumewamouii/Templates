class Settings:
    # Поля с начальными значениями
    _tin = ''
    _account = ''
    _corr_account = ''
    _bik = ''
    _name = ''
    _ownership_type = ''

    # ИНН
    @property
    def tin(self):
        return self._tin

    @tin.setter
    def tin(self, value):
        if isinstance(value, str) and len(value) == 12:
            self._tin = value
        else:
            raise ValueError('TIN must be string and contain 12 characters.')

    # Счет
    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value):
        if isinstance(value, str) and len(value) == 11:
            self._account = value
        else:
            raise ValueError('account must be string and contain 11 characters.')

    # Correspondent account
    @property
    def corr_account(self):
        return self._corr_account

    @corr_account.setter
    def corr_account(self, value):
        if isinstance(value, str) and len(value) == 11:
            self._corr_account = value
        else:
            raise ValueError('correspondent account must be string and contain 11 characters.')
    # BIC
    @property
    def bic(self):
        return self._bic

    @bic.setter
    def bic(self, value):
        if isinstance(value, str) and len(value) == 9:
            self._bic = value
        else:
            raise ValueError("BIC must be string and contain 9 characters.")

    # Наименование
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("name must be string.")

    # Вид собственности
    @property
    def ownership_type(self):
        return self._ownership_type

    @ownership_type.setter
    def ownership_type(self, value):
        if isinstance(value, str) and len(value) == 5:
            self._ownership_type = value
        else:
            raise ValueError("ownership type must be string and contain 5 characters.")

    def __str__(self):
        return (f"ИНН: {self._tin}\n"
                f"Счет: {self._account}\n"
                f"Корреспондентский счет: {self._corr_account}\n"
                f"БИК: {self._bic}\n"
                f"Наименование: {self._name}\n"
                f"Вид собственности: {self._ownership_type}")