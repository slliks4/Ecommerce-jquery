# Generated by Django 4.1.3 on 2023-06-24 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_remove_shipping_address_order_item_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shipping_address',
            options={'verbose_name_plural': 'Shipping_address'},
        ),
    ]
