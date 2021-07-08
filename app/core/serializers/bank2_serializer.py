from typing import List

from .base_serializer import BaseSerializer


class Bank2Serializer(BaseSerializer):

    header = ["date", "transaction", "amounts", "to", "from"]

    @staticmethod
    def _get_field_from(data: List) -> str:
        return data[4]

    @staticmethod
    def _get_field_to(data: List) -> str:
        return data[3]

    @staticmethod
    def _get_date_pattern() -> str:
        return "%d-%m-%Y"
