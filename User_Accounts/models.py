from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, email, password):
        if not username:
            raise ValueError('Please come up with some username')
        if not email:
            raise ValueError('We need your e-mail to continue the registration process')
        if not password:
            raise ValueError('Please come up with some password')
        user = self.model(
            username=username,
            email=self.normalize_email(email)
        )

        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=10)
    email = models.EmailField(verbose_name='email address',
                              max_length=255,
                              unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    email_confirmed = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    def has_module_permission(self, add_product):
        return False