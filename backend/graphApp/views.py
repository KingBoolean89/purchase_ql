from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductModelSerializer
from .models import ProductModel


class ProductModelViewset(viewsets.ModelViewSet):

    serializer_class = ProductModelSerializer
    queryset = ProductModel.objects.all()
