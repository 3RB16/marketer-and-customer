from .models import Offer

from rest_framework import serializers

class OffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'