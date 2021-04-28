from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager, PermissionsMixin)
# Create your models here.


class Usermanager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """create and saves new user"""
        if not email:
            raise ValueError("User must have a emmail")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """create amnd saves new superuer"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """custom usermodel that supports using email instead username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = Usermanager()

    USERNAME_FIELD = "email"
