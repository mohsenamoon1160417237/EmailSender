# Generated by Django 2.1 on 2021-03-25 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0016_auto_20210319_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
    ]
