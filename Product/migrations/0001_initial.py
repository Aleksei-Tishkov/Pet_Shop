# Generated by Django 4.2.6 on 2023-11-16 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(db_index=True, default='Default_Product_Name', max_length=30)),
                ('slug', models.SlugField(unique=True)),
                ('price', models.FloatField(default=0.0)),
                ('quantity', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True, db_index=True)),
                ('is_published', models.BooleanField(default=False)),
                ('product_type', models.CharField(db_index=True, default='Dog product', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSpecs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
