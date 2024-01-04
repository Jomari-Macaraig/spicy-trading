from rest_framework import serializers

from ..models import Journal


class JournalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Journal
        fields = (
            "open_time",
            "ticker",
            "side",
            "entry_price",
            "close_price",
            "details",
        )