# Generated by Django 4.1.3 on 2023-07-08 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0031_remove_order_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_items',
            name='selected',
            field=models.BooleanField(),
        ),
    ]