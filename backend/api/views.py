from rest_framework import generics
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DetailView
from .models import Brand, Laptop
from .serializers import BrandSerializer, LaptopSerializer
import requests

# Brand API Views
class BrandListCreateAPIView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BrandRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

# Laptop API Views
class LaptopListCreateAPIView(generics.ListCreateAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer

class LaptopRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer

# Fetch data from thd-party API
class LaptopShopView(TemplateView):
    template_name = 'laptop_shop.html'  #Adapt template name maybe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Make request to third-party API 
        response = requests.get('https://api.example.com/laptops')
        if response.status_code == 200:
            laptops = response.json() # if data is in JSON format
            context['laptops'] = laptops
        return context


class LaptopShopDetailView(DetailView):
    model = Laptop
    template_name = 'laptop_shop_detail.html'
    context_object_name = 'laptop'

    def get_queryset(self):
        return Laptop.objects.all()

    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        return get_object_or_404(queryset, pk=pk)
