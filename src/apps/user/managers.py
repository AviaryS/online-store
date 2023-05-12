from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, phone, username, sex=None, password=None, **extra_fields):
        """
        Создание и сохранение пользователя с номером телефона, именем, полом и паролем.
        """
        if not phone:
            raise ValueError('Укажите номер телефона')
        if not username:
            raise ValueError('Укажите имя пользователя')

        user = self.model(
            phone=phone,
            username=username,
            sex=sex,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, username, sex=None, password=None, **extra_fields):
        """
        Создание и сохранение суперпользователя с email, номером телефона, полом и паролем.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')

        return self.create_user(phone, username, sex, password, **extra_fields)
