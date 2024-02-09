# Generated by Django 4.1.3 on 2023-06-23 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_customer_profile_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_profile',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('bank_transfer', 'Bank Transfer'), ('cash', 'Cash'), ('credit_card', 'Credit Card'), ('paypal', 'PayPal')], default='credit_card', max_length=20),
        ),
    ]
