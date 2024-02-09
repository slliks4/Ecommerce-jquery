# Generated by Django 4.1.3 on 2023-07-04 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0028_alter_customer_profile_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_profile',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('bank_transfer', 'Bank Transfer'), ('paypal', 'PayPal'), ('cash', 'Cash'), ('credit_card', 'Credit Card')], default='credit_card', max_length=20),
        ),
    ]