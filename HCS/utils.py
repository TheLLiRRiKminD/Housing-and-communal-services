import datetime


def get_previous_month(month):
    """
        Получает предыдущий месяц для заданного месяца в формате YYYY-MM.

        :param month: Строка в формате YYYY-MM
        :return: Строка в формате YYYY-MM
        """
    year, month = map(int, month.split('-'))
    first_day_of_current_month = datetime.date(year, month, 1)
    last_day_of_previous_month = first_day_of_current_month - datetime.timedelta(days=1)
    return last_day_of_previous_month.strftime('%Y-%m')


def calculate_payment(apartment, water_tariff, maintenance_tariff, month):
    """
    Рассчитывает квартплату для всех квартир в доме за какой-либо месяц
    :param apartment: Номер квартиры
    :param water_tariff: Тариф за оплату воды
    :param maintenance_tariff: Тариф за содержание общего имущества
    :param month: Месяц
    :return: Результат выполнения вычислений
    """
    last_month = get_previous_month(month)
    water_usage = 0

    for meter in apartment.water_meters.all():
        if month in meter.readings and last_month in meter.readings:
            current_reading = meter.readings[month]
            last_reading = meter.readings[last_month]
            usage = current_reading - last_reading
            water_usage += usage

    water_cost = water_usage * water_tariff.price_per_unit
    maintenance_cost = apartment.area * maintenance_tariff.price_per_unit

    return water_cost + maintenance_cost
