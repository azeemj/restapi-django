# Generated by Django 3.2.11 on 2022-01-29 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryapi', '0002_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(default='', max_length=40),
        ),
    ]
