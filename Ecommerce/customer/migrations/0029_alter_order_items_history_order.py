# Generated by Django 4.1.3 on 2023-07-04 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0028_alter_order_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_items_history',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items_history', to='customer.order_history'),
        ),
    ]