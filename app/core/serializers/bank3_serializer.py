from decimal import Decimal
from typing import List

from .base_serializer import BaseSerializer


class Bank3Serializer(BaseSerializer):

    header = ["date_readable", "type", "euro", "cents", "to", "from"]

    @staticmethod
    def _get_amount(data: List) -> Decimal:
        return Decimal(data[2]) + Decimal(data[3]) / 100

    @staticmethod
    def _get_field_from(data: List) -> str:
        return data[5]

    @staticmethod
    def _get_date_pattern() -> str:
        return "%d %b %Y"
