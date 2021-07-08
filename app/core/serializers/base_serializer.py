from datetime import date, datetime
from decimal import Decimal
from typing import List


class BaseSerializer:

    header: list = None

    @classmethod
    def create_row(cls, row: List) -> List:
        """
        Creating row for result file
        :param row: row of found file
        :return: List of parsed field
        """
        return [
            cls._get_date(row),
            cls._get_transaction_type(row),
            cls._get_amount(row),
            cls._get_field_from(row),
            cls._get_field_to(row),
        ]

    @classmethod
    def _get_date(cls, data: List) -> date:
        return datetime.strptime(data[0], cls._get_date_pattern()).date()

    @staticmethod
    def _get_transaction_type(data: List) -> str:
        return data[1]

    @staticmethod
    def _get_amount(data: List) -> Decimal:
        return data[2]

    @staticmethod
    def _get_field_from(data: List) -> str:
        return data[3]

    @staticmethod
    def _get_field_to(data: List) -> str:
        return data[4]

    @staticmethod
    def _get_date_pattern() -> str:
        return "%b %d %Y"
