# Generated by Django 3.1 on 2020-09-18 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, db_column='Image', null=True, upload_to='shop/product_images'),
        ),
    ]
