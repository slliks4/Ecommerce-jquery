# Generated by Django 4.1.3 on 2023-06-29 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0020_alter_order_items_selected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_items',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_item', to='customer.order'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.order'),
        ),
        migrations.AlterField(
            model_name='shipping_address',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order', to='customer.order'),
        ),
    ]
