# Generated by Django 3.2.5 on 2021-07-27 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Авторы', 'verbose_name_plural': 'Автор'},
        ),
    ]
