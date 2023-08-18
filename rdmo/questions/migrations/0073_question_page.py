# Generated by Django 3.2.14 on 2022-12-07 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0072_questionset_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='page',
            field=models.ForeignKey(blank=True, help_text='The page this question belongs to.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='questions.page', verbose_name='Page'),
        )
    ]