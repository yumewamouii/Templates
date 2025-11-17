import enum
from src.utils.enum_meta import EnumMeta


class FilterType(enum.Enum, metaclass=EnumMeta):
    """
    Enumeration representing different types of filtering operations.
    Uses a custom metaclass `EnumMeta` to extend enum functionality.
    """

    EQUALS = 0    # Exact value match
    LIKE = 1      # Partial match (e.g., SQL LIKE)
    BETWEEN = 2   # Range comparison (e.g., value between min and max)
