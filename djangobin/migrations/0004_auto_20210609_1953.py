# Generated by Django 3.1.7 on 2021-06-09 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangobin', '0003_auto_20210609_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='highlighted_code',
            field=models.TextField(blank=True, help_text='Read only field. Will contain the syntax-highlited version of the original code.'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='hits',
            field=models.IntegerField(default=0, help_text='Read only field. Will be updated after every visit to snippet.'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='slug',
            field=models.SlugField(help_text='Read only field. Will be filled automatically.'),
        ),
    ]