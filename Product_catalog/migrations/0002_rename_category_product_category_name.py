# Generated by Django 4.2.3 on 2023-07-03 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product_catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_category',
            old_name='category',
            new_name='name',
        ),
    ]