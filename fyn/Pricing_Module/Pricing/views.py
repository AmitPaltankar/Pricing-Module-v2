# pricing_module/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PricingConfig

@api_view(['POST'])
def calculate_price(request):
    try:
        # Extract parameters from the request
        distance_traveled = float(request.data.get('distance_traveled', 0))
        time_duration = float(request.data.get('time_duration', 0))

        # Retrieve the active pricing configuration
        pricing_config = PricingConfig.objects.get(is_active=True)

        # Pricing calculations
        base_price = pricing_config.distance_base_price
        additional_price = pricing_config.distance_additional_price * max(0, distance_traveled - 3)
        time_multiplier = pricing_config.time_multiplier_factor
        waiting_charges = pricing_config.waiting_charges * max(0, time_duration - 3)

        # Calculate the final price
        calculated_price = (base_price + additional_price) + (time_duration * time_multiplier) + waiting_charges

        # Return the calculated price in the response
        return Response({"price": calculated_price})

    except PricingConfig.DoesNotExist:
        return Response({"error": "No active pricing configuration found."}, status=400)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
