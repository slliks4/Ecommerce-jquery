# Generated by Django 4.1.3 on 2023-07-04 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0026_order_history_total_price_order_items_history_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipping_address',
            name='order_history',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.order_history'),
        ),
    ]