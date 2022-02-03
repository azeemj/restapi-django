from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters

from .serializers import ProductSerializer, InventorySerializer
from .models import Product, Inventory, Supplier



class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class InventoryView(viewsets.ModelViewSet):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])