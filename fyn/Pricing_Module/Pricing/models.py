# pricing_module/models.py

from django.db import models

class PricingConfig(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    distance_base_price = models.DecimalField(max_digits=10, decimal_places=2)
    distance_additional_price = models.DecimalField(max_digits=10, decimal_places=2)
    time_multiplier_factor = models.DecimalField(max_digits=5, decimal_places=2)
    waiting_charges = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
