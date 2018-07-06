# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-28 11:23
from __future__ import unicode_literals

from django.db import migrations


def set_question_condition(apps, schema_editor):
    QuestionEntity = apps.get_model('questions', 'QuestionEntity')

    for entity in QuestionEntity.objects.all():
        try:
            for condition in entity.attribute_entity.conditions.all():
                print(condition)
                entity.conditions.add(condition)

        except AttributeError:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0019_questionentity_conditions'),
    ]

    operations = [
        migrations.RunPython(set_question_condition),
    ]
