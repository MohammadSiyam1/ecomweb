# Generated by Django 4.1.2 on 2022-12-08 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Slider_Blogs_and_others', '0006_customer_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Phone_Number',
            field=models.BigIntegerField(default=None),
        ),
    ]