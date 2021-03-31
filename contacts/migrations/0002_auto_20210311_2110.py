# Generated by Django 2.1 on 2021-03-11 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(help_text='Enter your message...')),
                ('subject', models.CharField(help_text='Enter subject...', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='emails/contacts')),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(help_text='Enter a name for your contact...', max_length=100),
        ),
        migrations.AddField(
            model_name='email',
            name='files',
            field=models.ManyToManyField(related_name='emails', to='contacts.File'),
        ),
        migrations.AddField(
            model_name='email',
            name='receiver',
            field=models.ManyToManyField(related_name='emails', to='contacts.Contact'),
        ),
    ]
