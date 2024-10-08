from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HouseViewSet, ApartmentViewSet, WaterMeterViewSet, TariffViewSet, start_calculation, \
    PaymentRecordViewSet
from HCS.apps import HcsConfig

app_name = HcsConfig.name

router = DefaultRouter()
router.register(r'houses', HouseViewSet)
router.register(r'apartments', ApartmentViewSet)
router.register(r'watermeters', WaterMeterViewSet)
router.register(r'tariffs', TariffViewSet)
router.register(r'payment_records', PaymentRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('start_calculation/<int:house_id>/<str:month>/', start_calculation),
]
