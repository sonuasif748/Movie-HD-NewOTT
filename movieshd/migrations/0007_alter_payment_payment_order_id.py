# Generated by Django 3.2.4 on 2021-08-12 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieshd', '0006_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_order_id',
            field=models.CharField(max_length=500),
        ),
    ]