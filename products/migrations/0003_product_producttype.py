# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-24 16:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productType', '0001_initial'),
        ('products', '0002_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productType',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='productType.ProductType'),
            preserve_default=False,
        ),
    ]
