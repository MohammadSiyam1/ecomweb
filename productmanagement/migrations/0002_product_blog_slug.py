# Generated by Django 4.1.2 on 2022-10-31 12:05

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Blog_slug',
            field=autoslug.fields.AutoSlugField(default=None, null=True, unique=True),
        ),
    ]