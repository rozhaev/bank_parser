from .base_serializer import BaseSerializer


class Bank1Serializer(BaseSerializer):

    header = ["timestamp", "type", "amount", "from", "to"]
