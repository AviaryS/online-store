from django.db import models

from django.core.validators import MinLengthValidator

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from .managers import CustomUserManager


SEX_CHOICES = (
    ('man', 'муж'),
    ('woman', 'жен'),
)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Пользователь, который может войти в систему
    с помощью email или номера телефона.
    """
    username = models.CharField(verbose_name='Имя пользователя', max_length=255)

    email = models.EmailField(verbose_name='E-mail', unique=True, blank=True, null=True)
    phone = models.CharField(
        verbose_name='Русский номер телефона',
        max_length=12,
        validators=[MinLengthValidator(11)],
        unique=True
    )
    sex = models.CharField(
        verbose_name='Пол человека',
        choices=SEX_CHOICES,
        blank=True,
        null=True,
        max_length=5
    )
    first_name = models.CharField(verbose_name='Имя', max_length=30, blank=True, null=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=30, blank=True, null=True)

    is_active = models.BooleanField(verbose_name='Активен', default=True)
    is_staff = models.BooleanField(verbose_name='Сотрудник', default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.username} - {self.phone}'