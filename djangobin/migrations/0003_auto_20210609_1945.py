# Generated by Django 3.1.7 on 2021-06-09 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangobin', '0002_auto_20210609_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='lang_code',
            field=models.CharField(max_length=100, unique=True, verbose_name='Language Code'),
        ),
    ]