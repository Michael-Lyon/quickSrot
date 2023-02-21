from django.shortcuts import render
from rest_framework import viewsets
from .models import Detail
from .serializers import DetailSerializer
# Create your views here.


class DetailViewSet(viewsets.ModelViewSet):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer
