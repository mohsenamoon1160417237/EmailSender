# Generated by Django 2.1 on 2021-03-14 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0013_auto_20210314_1501'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='email',
            options={'ordering': ['subject']},
        ),
    ]