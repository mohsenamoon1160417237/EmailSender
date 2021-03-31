# Generated by Django 2.1 on 2021-03-13 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0008_contact_is_selected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(help_text='Enter a name for your contact...', max_length=100, unique=True),
        ),
    ]