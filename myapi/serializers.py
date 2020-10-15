from rest_framework import serializers
from .models import EconomicData

class EconomicDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EconomicData
        fields = ('dollarBought', 'dollarSold')