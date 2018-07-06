# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-06 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conditions', '0013_meta'),
        ('questions', '0018_data_migration'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionentity',
            name='conditions',
            field=models.ManyToManyField(blank=True, help_text='List of conditions evaluated for this question/questionset.', to='conditions.Condition', verbose_name='Conditions'),
        ),
    ]
