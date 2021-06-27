from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager


class User( AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("Email"), max_length=220, unique=True)
    first_name = models.CharField(_("first_name"), max_length=220)
    last_name = models.CharField(_("last_name"), max_length=220)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # will be overwritten in super_user

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    def get_short_name(self):
        return f"{self.first_name}"

