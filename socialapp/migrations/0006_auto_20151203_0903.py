# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-03 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0005_auto_20151203_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(),
        ),
    ]