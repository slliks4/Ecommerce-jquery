# Generated by Django 4.1.3 on 2023-07-04 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0025_alter_order_history_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_history',
            name='total_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order_items_history',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
