# Generated by Django 3.2.8 on 2021-12-07 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20211207_1319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='hits',
        ),
    ]
