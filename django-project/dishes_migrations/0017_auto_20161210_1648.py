# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-10 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0016_auto_20161210_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='diner',
        ),
        migrations.RemoveField(
            model_name='bid',
            name='dish_post',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='chef',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='dish_request',
        ),
        migrations.RemoveField(
            model_name='dishpost',
            name='min_price',
        ),
        migrations.RemoveField(
            model_name='dishrequest',
            name='min_price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='bid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='chef_rated',
        ),
        migrations.RemoveField(
            model_name='order',
            name='diner_rated',
        ),
        migrations.AddField(
            model_name='dish',
            name='alchemy_label',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='dishpost',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dishrequest',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dishpost',
            name='status',
            field=models.IntegerField(choices=[(0, 'Open'), (1, 'Cancelled'), (2, 'Complete')], default=0),
        ),
        migrations.AlterField(
            model_name='dishrequest',
            name='status',
            field=models.IntegerField(choices=[(0, 'Open'), (1, 'Cancelled'), (2, 'Complete')], default=0),
        ),
        migrations.DeleteModel(
            name='Bid',
        ),
        migrations.DeleteModel(
            name='Offer',
        ),
    ]
