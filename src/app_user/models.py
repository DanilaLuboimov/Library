from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from datetime import datetime

phone_number_validator = RegexValidator(
        regex=r"^(\+7|8)[(]?\d{3}[)]?\d{7}$",
        message='Номер не соответствует: "+7(931)1234567" "8333123456"'
    )


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Почтовый адрес")
    phone_number = models.CharField(
        validators=[phone_number_validator],
        blank=True,
        unique=True,
        null=True,
        max_length=14,
        verbose_name="Номер телефона"
    )

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        db_table = "users"

    def __str__(self):
        return self.username


class Feedback(models.Model):
    email = models.EmailField(verbose_name="Почтовый адрес")
    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=150,
        verbose_name="Имя"
    )
    message = models.TextField(
        max_length=500,
        verbose_name="Сообщение",
    )
    phone_number = models.CharField(
        validators=[phone_number_validator],
        blank=True,
        null=True,
        max_length=14,
        verbose_name="Номер телефона"
    )
    created_at = models.DateTimeField(
        auto_created=True,
        verbose_name="Дата обращения",
        default=datetime.now(),
    )
    is_answer = models.BooleanField(
        default=False, verbose_name="Отвечено"
    )

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"
        db_table = "feedback"

    def __str__(self):
        return self.email
