# Generated by Django 3.2.5 on 2021-07-22 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_fairy',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user_fairy',
            name='username',
        ),
    ]
