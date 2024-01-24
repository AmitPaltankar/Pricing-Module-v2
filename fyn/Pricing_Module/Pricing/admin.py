# pricing_module/admin.py

from django.contrib import admin
from .models import PricingConfig

class PricingConfigAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'distance_base_price', 'distance_additional_price', 'time_multiplier_factor', 'waiting_charges']
    search_fields = ['name']

admin.site.register(PricingConfig, PricingConfigAdmin)
