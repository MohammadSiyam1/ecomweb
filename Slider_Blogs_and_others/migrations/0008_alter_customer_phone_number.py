# Generated by Django 4.1.2 on 2022-12-08 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Slider_Blogs_and_others', '0007_alter_customer_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Phone_Number',
            field=models.CharField(max_length=200),
        ),
    ]
