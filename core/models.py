from django.db import models
from django.db.utils import DJANGO_VERSION_PICKLE_KEY
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from core.managers import UserManager


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    REQUIRED_FIELDS = ['email', ]
    objects = UserManager()
