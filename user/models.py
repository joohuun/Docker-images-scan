from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from user.managers import UsersManager



class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UsersManager()

    username = models.CharField(max_length=30, unique=True, null=False, blank=False)
    email = models.EmailField(max_length=200, unique=True, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    bio = models.CharField(max_length=200, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)