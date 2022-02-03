# Generated by Django 3.2.11 on 2022-01-30 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryapi', '0003_alter_product_sku'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',)},
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('note', models.CharField(default='', max_length=40)),
                ('stock', models.IntegerField(default=0)),
                ('availability', models.BooleanField(default=False)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='inventoryapi.product')),
                ('supplier', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventoryapi.supplier')),
            ],
            options={
                'ordering': ('stock',),
            },
        ),
    ]
