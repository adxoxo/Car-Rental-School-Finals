# Generated by Django 3.2.18 on 2023-03-07 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0007_alter_rental_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='RentalDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='rental',
            name='ReturnDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
