# from django.test import TestCase, Client
# from django.urls import reverse
# from unittest.mock import patch, MagicMock
# from .models import Brand, Laptop

# class BrandViewsTestCase(TestCase):
#     def setUp(self):
#         self.brand = Brand.objects.create(name='TechNova') 

#     def test_brand_list_create_api_view(self):
#         response = self.client.get(reverse('brand_list'))
#         self.assertEqual(response.status_code, 200)

#     def test_brand_retrieve_update_destroy_api_view(self):
#         brand = Brand.objects.create(name='Test Brand')
#         response = self.client.get(reverse('brand_detail', kwargs={'pk': brand.pk}))
#         self.assertEqual(response.status_code, 200)

# class LaptopViewsTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()

#     def test_laptop_list_create_api_view(self):
#         response = self.client.get(reverse('laptop_list'))
#         self.assertEqual(response.status_code, 200)

#     def test_laptop_retrieve_update_destroy_api_view(self):
#         laptop = Laptop.objects.create(brand=self.brand, model_name='Test Laptop', processor_speed=2.5, price=1000.00)
#         response = self.client.get(reverse('laptop_detail', kwargs={'pk': laptop.pk}))
#         self.assertEqual(response.status_code, 200)

# class LaptopShopViewTestCase(TestCase):
#     @patch('requests.get')
#     def test_laptop_shop_view(self, mock_get):
#         mock_response = MagicMock(status_code=200)
#         mock_response.json.return_value = [
#             {'name': 'Laptop 1', 'processor': 'Intel', 'ram': '8GB'},
#             {'name': 'Laptop 2', 'processor': 'AMD', 'ram': '16GB'}
#         ]
#         mock_get.return_value = mock_response

#         response = self.client.get(reverse('laptop_shop'))

#         self.assertEqual(response.status_code, 200)
#         self.assertIn('laptops', response.context)
#         self.assertEqual(len(response.context['laptops']), 2)
