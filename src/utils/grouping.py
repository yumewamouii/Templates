from itertools import groupby
from src.mappers import AbsoluteMapper


class Grouping:
    """
    Utility class for grouping a list of models by one or more nested attributes.
    """

    @staticmethod
    def group(data: list, groups: list[str], value_to_group: str = None) -> list:
        """
        Groups a list of objects based on one or more attributes.

        Args:
            data (list): List of objects to group.
            groups (list[str]): List of attribute names (dot notation allowed) to group by.

        Returns:
            iterator: An iterator of (key, group) tuples, where `key` is a tuple of attribute values
                      and `group` is a sublist of objects matching that key.
        """
        # groupby requires the data to be sorted by the key function first
        sorted_data = sorted(
            data,
            key=lambda x: tuple(Grouping._get_property(x, group, value_to_group) for group in groups)
        )
        return groupby(
            sorted_data,
            key=lambda x: tuple(Grouping._get_property(x, group, value_to_group) for group in groups)
        )

    @staticmethod
    def _get_property(model, group: str, value_to_group: str = None):
        """
        Resolves a nested attribute from an object using dot notation.

        Args:
            model: Object to retrieve attribute from.
            group (str): Attribute path, e.g., "unit.name".

        Returns:
            The value of the nested attribute, or False if any part of the path is missing.
        """
        item_dict = AbsoluteMapper.to_dict(model)
        keys_array = group.split('.')
        inner_value = item_dict

        if value_to_group is not None:
            inner_value = inner_value.get(value_to_group, None)
            if inner_value is None:
                return False

        for key in keys_array:
            inner_value = inner_value.get(key, None)
            if inner_value is None:
                return False

        return inner_value
