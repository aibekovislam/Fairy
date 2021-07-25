# Generated by Django 3.2.5 on 2021-07-23 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='Article_img')),
                ('likes', models.IntegerField(default=0, verbose_name='Лайки')),
                ('readers', models.ManyToManyField(blank=True, related_name='readers', to=settings.AUTH_USER_MODEL, verbose_name='Читатели')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.users', verbose_name='Пользователь')),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]