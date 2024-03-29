# Generated by Django 4.1.3 on 2023-07-08 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0033_alter_customer_profile_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_profile',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('cash', 'Cash'), ('paypal', 'PayPal'), ('bank_transfer', 'Bank Transfer'), ('credit_card', 'Credit Card')], default='credit_card', max_length=20),
        ),
    ]
