from src.models.measured_value import MeasuredValue
from src.models.store_transaction import StoreTransaction, StoreTransactionType
from src.models.store_turnover import StoreTurnover
from src.utils.grouping import Grouping


class TurnoversFromTransactions:
    """
    Processes a list of StoreTransaction objects and calculates turnovers
    grouped by specified keys.
    """

    @staticmethod
    def calculate(inp: list[StoreTransaction], grouping: list[str]) -> list[StoreTurnover]:
        """
        Groups transactions by specified keys and calculates the turnover
        for each group.

        Args:
            inp (list[StoreTransaction]): List of transactions to process.
            grouping (list[str]): List of keys for grouping, e.g., ['nomenclature', 'store'].

        Returns:
            list[StoreTurnover]: List of calculated turnovers for each group.
        """
        groups = Grouping.group(inp, grouping)
        # Each group is a tuple of (group key values, iterator of transactions)
        return [
            TurnoversFromTransactions._calculate_group(group, grouping)
            for group in groups
        ]

    @staticmethod
    def _calculate_group(group, grouping) -> StoreTurnover:
        """
        Calculates the turnover for a single group of transactions.

        Args:
            group (tuple): (group_key, transactions_iterator)
            grouping (list[str]): List of keys used for grouping.

        Returns:
            StoreTurnover: Calculated turnover object for the group.
        """
        key, transactions_iter = group
        transactions = list(transactions_iter)  # Materialize iterator

        # Initialize the turnover with zero, using the unit of the first transaction
        value = MeasuredValue(0.0, transactions[0].nomenclature.unit)

        # Sum or subtract amounts based on transaction type
        for transaction in transactions:
            match transaction.transaction_type:
                case StoreTransactionType.INCOME:
                    value = value + transaction.amount
                case StoreTransactionType.EXPENSE:
                    value = value - transaction.amount

        # Prepare group metadata for the StoreTurnover
        group_data = {grouping[i]: key[i] for i in range(len(key))}

        return StoreTurnover(turnover=value, group=group_data)


    @staticmethod
    def merge(t1: list[StoreTurnover], t2: list[StoreTurnover]) -> list[StoreTurnover]:
        groups = {}


        for t in t1 + t2:
            if t.group not in groups:
                groups[t.group] = t.turnover
                continue
            groups[t.group] += t.turnover
        

        return [StoreTurnover(turnover = value, group = key) for key, value in groups]