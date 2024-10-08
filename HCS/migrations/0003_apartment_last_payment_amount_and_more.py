# Generated by Django 5.1.1 on 2024-10-08 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("HCS", "0002_apartment_apartment_number_paymentrecord"),
    ]

    operations = [
        migrations.AddField(
            model_name="apartment",
            name="last_payment_amount",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="apartment",
            name="last_payment_month",
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]
