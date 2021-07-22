from django.db import models
from django.contrib.auth.models import User



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