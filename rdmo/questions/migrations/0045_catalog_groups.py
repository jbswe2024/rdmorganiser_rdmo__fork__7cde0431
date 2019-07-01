# Generated by Django 2.2.2 on 2019-07-01 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('questions', '0044_catalog_sites'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups for which this catalog is active.', to='auth.Group', verbose_name='Group'),
        ),
    ]
