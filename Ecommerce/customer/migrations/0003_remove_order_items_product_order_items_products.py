# Generated by Django 4.1.3 on 2023-06-23 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_remove_order_items_products_order_items_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_items',
            name='product',
        ),
        migrations.AddField(
            model_name='order_items',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='customer.products'),
        ),
    ]
