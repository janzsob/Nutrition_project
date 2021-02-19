# Generated by Django 3.1.5 on 2021-02-13 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TopIngredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, verbose_name='Product Name')),
                ('product_id', models.IntegerField(verbose_name='Product ID')),
            ],
            options={
                'verbose_name': 'TopIngredient',
                'verbose_name_plural': 'TopIngredients',
                'ordering': ['product_name'],
            },
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('plural_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Unit',
                'verbose_name_plural': 'Units',
            },
        ),
    ]
