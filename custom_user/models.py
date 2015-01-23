from django.db import models
from authemail.models import EmailUserManager, EmailAbstractUser


class CustomUser(EmailAbstractUser):
    # Custom fields

    # Required
    objects = EmailUserManager()
