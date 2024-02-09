# Generated by Django 4.1.3 on 2023-06-24 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_alter_customer_profile_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_profile',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('cash', 'Cash'), ('credit_card', 'Credit Card'), ('paypal', 'PayPal'), ('bank_transfer', 'Bank Transfer')], default='credit_card', max_length=20),
        ),
    ]
