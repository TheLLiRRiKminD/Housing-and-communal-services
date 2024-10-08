from rest_framework import serializers
from .models import House, Apartment, WaterMeter, Tariff, PaymentRecord


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = '__all__'


class WaterMeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterMeter
        fields = '__all__'


class ApartmentSerializer(serializers.ModelSerializer):
    water_meters = WaterMeterSerializer(many=True, read_only=True)
    last_payment_amount = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    last_payment_month = serializers.CharField(max_length=7, required=False)

    class Meta:
        model = Apartment
        fields = '__all__'


class HouseSerializer(serializers.ModelSerializer):
    apartments = ApartmentSerializer(many=True, read_only=True)

    class Meta:
        model = House
        fields = '__all__'


class PaymentRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentRecord
        fields = '__all__'
