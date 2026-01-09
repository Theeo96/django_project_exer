from django.db import models
from news.models.common import BaseModel
from django.contrib.auth.models import AbstractUser, UserManager


class User(BaseModel, AbstractUser) :

    objects = UserManager()

    address = models.CharField(max_length=500, blank=True, verbose_name="주소")
    birthday = models.DateField(blank=True, null=True, verbose_name="생일")
    postcode = models.CharField(max_length=20, blank=True, null=True, verbose_name="우편번호")