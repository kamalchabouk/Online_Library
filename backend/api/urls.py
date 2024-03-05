from django.urls import path
from .views import BrandListCreateAPIView, BrandRetrieveUpdateDestroyAPIView, LaptopListCreateAPIView, LaptopRetrieveUpdateDestroyAPIView, LaptopShopView, LaptopShopDetailView

urlpatterns = [
    path('brands/', BrandListCreateAPIView.as_view(), name='brand_list'),
    path('brands/<int:pk>/', BrandRetrieveUpdateDestroyAPIView.as_view(), name='brand_detail'),
    path('laptops/', LaptopListCreateAPIView.as_view(), name='laptop_list'),
    path('laptops/<int:pk>/', LaptopRetrieveUpdateDestroyAPIView.as_view(), name='laptop_detail'),
    path('laptop-shop/', LaptopShopView.as_view(), name='laptop_shop'),
    path('laptop-shop/<int:pk>/', LaptopShopDetailView.as_view(), name='laptop_shop_detail'),
]
