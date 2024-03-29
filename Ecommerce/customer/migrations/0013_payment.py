# Generated by Django 4.1.3 on 2023-06-24 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_alter_shipping_address_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billing_address', models.BooleanField(blank=True, choices=[('SHIPPING_ADDRESS', 'same as shipping address'), ('DIFFERENT', 'different billing address')], null=True)),
                ('remember_me', models.BooleanField(default=False)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.order')),
            ],
            options={
                'verbose_name_plural': 'Payment',
            },
        ),
    ]
