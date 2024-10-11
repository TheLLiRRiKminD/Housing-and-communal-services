from celery import shared_task
from .models import House, Tariff, PaymentRecord
from .utils import calculate_payment


@shared_task
def calculate_all_payments(house_id, month):
    house = House.objects.select_related('apartments').get(id=house_id)
    water_tariff = Tariff.objects.get(name='water')
    maintenance_tariff = Tariff.objects.get(name='maintenance')

    apartments = house.apartments.prefetch_related('water_meters')

    for apartment in apartments:
        payment = calculate_payment(apartment, water_tariff, maintenance_tariff, month)

        # Сохранение результата в PaymentRecord
        PaymentRecord.objects.create(apartment=apartment, month=month, amount=payment)

        # Обновление данных о квартире
        apartment.last_payment_amount = payment
        apartment.last_payment_month = month
        apartment.save()

        # Отладочные сообщения
        print(f"Apartment ID: {apartment.id}, Month: {month}, Payment: {payment}")

    return 'Completed'
