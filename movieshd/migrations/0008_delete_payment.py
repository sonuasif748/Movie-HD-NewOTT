# Generated by Django 3.2.4 on 2021-08-13 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieshd', '0007_alter_payment_payment_order_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='payment',
        ),
    ]
