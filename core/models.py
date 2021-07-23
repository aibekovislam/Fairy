from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related



class Users(models.Model):
    acc = models.OneToOneField(
        to=User,
        related_name='Account',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Аккаунт"
    )

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"

    def __str__(self):
        return str(self.acc)


class Publics(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    image = models.ImageField(upload_to="Article_img", null=True, blank=True)
    user = models.ForeignKey(
        to=Users,
        null=True, blank=True,
        verbose_name=("Пользователь"), 
        on_delete=models.CASCADE
    )


    readers = models.ManyToManyField(
        to=User,
        related_name = "readers",
        blank=True, 
        verbose_name="Читатели"
    )

    likes = models.IntegerField(default=0, verbose_name="Лайки")


    class Meta:
        verbose_name = ("Публикации")
        verbose_name_plural = ("Публикация")


    def __str__(self):
        return self.title