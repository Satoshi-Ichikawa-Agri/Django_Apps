# Generated by Django 4.1.7 on 2023-02-26 07:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'carts',
            },
        ),
        migrations.CreateModel(
            name='Manufacturers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'manufacturers',
            },
        ),
        migrations.CreateModel(
            name='ProductTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'product_types',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('Manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.manufacturers')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.producttypes')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductPictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(upload_to='product_pictures/')),
                ('order', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.products')),
            ],
            options={
                'db_table': 'product_pictures',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.carts')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.products')),
            ],
            options={
                'db_table': 'cart_items',
                'unique_together': {('product', 'cart')},
            },
        ),
    ]
