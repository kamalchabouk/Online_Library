from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Laptop(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)
    processor_type = models.CharField(max_length=100, null=True, blank=True)
    processor_speed = models.FloatField(null=True, blank=True)  # in GHz
    ram_size = models.IntegerField(null=True, blank=True)  # in GB
    ram_type = models.CharField(max_length=50, null=True, blank=True)
    storage_capacity = models.IntegerField(null=True, blank=True)  # in GB
    storage_type = models.CharField(max_length=50, null=True, blank=True)
    graphics_card = models.CharField(max_length=100, null=True, blank=True)
    screen_size = models.FloatField(null=True, blank=True)  # in inches
    screen_resolution = models.CharField(max_length=20, null=True, blank=True)
    battery_life = models.FloatField(null=True, blank=True)  # in hours
    weight = models.FloatField(null=True, blank=True)  # in kg
    dimensions = models.CharField(max_length=50, null=True, blank=True)  # e.g., "14.1 x 9.6 x 0.7 inches"
    image = models.ImageField(upload_to='laptop_images/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.model_name
