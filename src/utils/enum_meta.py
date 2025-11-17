import enum


class EnumMeta(enum.EnumMeta):
    """ 
    Allows to check the occurrence by name or instance of an enum.

        Examples:
            'RED' in Color
            Color.RED in Color
    """
    def __contains__(cls, item):
        if isinstance(item, cls):
            return True


        if isinstance(item, str):
            return item in cls.__members__


        return False    