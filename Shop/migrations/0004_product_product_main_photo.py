# Generated by Django 4.2.6 on 2023-12-14 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_alter_productphoto_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_main_photo',
            field=models.ImageField(default='static/Images/default_product_image.webp', upload_to='product_photos/%Y/%m/%d'),
        ),
    ]
