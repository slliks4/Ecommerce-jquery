# Generated by Django 4.2.3 on 2023-07-03 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0001_initial'),
        ('Payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkout',
            old_name='select',
            new_name='complete',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='product',
        ),
        migrations.AddField(
            model_name='checkout',
            name='order_items',
            field=models.ManyToManyField(to='Cart.order_items'),
        ),
    ]