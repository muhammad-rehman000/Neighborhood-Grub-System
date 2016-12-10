# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-10 09:55
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0008_dish_alchemy_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratechef',
            name='rating',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
