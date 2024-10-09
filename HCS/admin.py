from django.contrib import admin
from HCS.models import PaymentRecord, House, Apartment, WaterMeter, Tariff


# Register your models here.
@admin.register(PaymentRecord)
class HCSAdmin(admin.ModelAdmin):
    list_display = ('amount',)

@admin.register(House)
class HCSAdmin(admin.ModelAdmin):
    list_display = ('address',)

@admin.register(Apartment)
class HCSAdmin(admin.ModelAdmin):
    list_display = ('house', 'area', 'apartment_number', 'last_payment_amount')

@admin.register(WaterMeter)
class HCSAdmin(admin.ModelAdmin):
    list_display = ('apartment', 'readings')

@admin.register(Tariff)
class HCSAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_unit')