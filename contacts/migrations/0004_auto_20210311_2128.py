# Generated by Django 2.1 on 2021-03-11 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20210311_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='sent_file',
        ),
        migrations.AddField(
            model_name='file',
            name='email',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='contacts.Email'),
        ),
    ]
