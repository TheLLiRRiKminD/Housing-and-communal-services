from rest_framework import viewsets
from .models import House, Apartment, WaterMeter, Tariff, PaymentRecord
from .serializers import HouseSerializer, ApartmentSerializer, WaterMeterSerializer, TariffSerializer, \
    PaymentRecordSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import calculate_all_payments


@api_view(['POST'])
def start_calculation(request, house_id, month):
    """Запуск фонового процесса рассчета коммунальных услуг"""
    task = calculate_all_payments.delay(house_id, month)
    return Response({'task_id': task.id})


class PaymentRecordViewSet(viewsets.ModelViewSet):
    """Вьюсет для просмотра результатов вычислений """
    queryset = PaymentRecord.objects.all()
    serializer_class = PaymentRecordSerializer


class HouseViewSet(viewsets.ModelViewSet):
    """Вьюсет данных о доме"""
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class ApartmentViewSet(viewsets.ModelViewSet):
    """Вьюсет данных о квартире"""
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer


class WaterMeterViewSet(viewsets.ModelViewSet):
    """Вьюсет данных о счетчике"""
    queryset = WaterMeter.objects.all()
    serializer_class = WaterMeterSerializer


class TariffViewSet(viewsets.ModelViewSet):
    """Вьюсет данных о тарифах для оплаты"""
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer
