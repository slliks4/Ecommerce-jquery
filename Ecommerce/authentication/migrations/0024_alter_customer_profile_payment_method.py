# Generated by Django 4.1.3 on 2023-06-29 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0023_alter_customer_profile_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_profile',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('credit_card', 'Credit Card'), ('bank_transfer', 'Bank Transfer'), ('cash', 'Cash'), ('paypal', 'PayPal')], default='credit_card', max_length=20),
        ),
    ]
