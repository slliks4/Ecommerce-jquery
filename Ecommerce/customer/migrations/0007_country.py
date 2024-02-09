# Generated by Django 4.1.3 on 2023-06-23 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_shipping_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('capital', models.CharField(max_length=100)),
                ('population', models.IntegerField()),
            ],
        ),
    ]