# Generated by Django 4.2.3 on 2023-07-03 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0001_initial'),
        ('Payment', '0002_rename_select_checkout_complete_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='order_items',
            field=models.ManyToManyField(related_name='all_order_items', to='Cart.order_items'),
        ),
    ]
