# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-24 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200424_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_as_base64',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(upload_to='images'),
        ),
    ]
