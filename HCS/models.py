from django.db import models


class Tariff(models.Model):
    """Модель тарифов"""
    name = models.CharField(max_length=100)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class House(models.Model):
    """Модель дома"""
    street = models.CharField(max_length=255)
    house_number = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.street}, {self.house_number}'


class Apartment(models.Model):
    """Модель квартиры"""
    house = models.ForeignKey(House, related_name='apartments', on_delete=models.CASCADE)
    area = models.DecimalField(max_digits=7, decimal_places=2)
    apartment_number = models.IntegerField(default=1)
    last_payment_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    last_payment_month = models.CharField(max_length=7, null=True, blank=True)  # Формат YYYY-MM

    def __str__(self):
        return f"Apartment in {self.house.street} {self.house.house_number}"


class WaterMeter(models.Model):
    """Модель счетчика"""
    apartment = models.ForeignKey(Apartment, related_name='water_meters', on_delete=models.CASCADE)
    readings = models.JSONField()  # { 'YYYY-MM': value }

    def __str__(self):
        return f"Water Meter in {self.apartment}"


class PaymentRecord(models.Model):
    """Модель записи расчетов"""
    apartment = models.ForeignKey(Apartment, related_name='payment_records', on_delete=models.CASCADE)
    month = models.CharField(max_length=7)  # Формат YYYY-MM
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    calculated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.apartment} in {self.month}"
