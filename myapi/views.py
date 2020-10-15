from django.shortcuts import render
from rest_framework import viewsets

from .serializers import EconomicDataSerializer
from .models import EconomicData


class EconomicDataViewSet(viewsets.ModelViewSet):
    queryset = EconomicData.objects.all()
    serializer_class = EconomicDataSerializer