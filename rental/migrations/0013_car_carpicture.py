# Generated by Django 3.2.18 on 2023-03-09 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0012_alter_car_stock_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='CarPicture',
            field=models.ImageField(blank=True, upload_to='media/cars/'),
        ),
    ]