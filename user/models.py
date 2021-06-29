from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class SchoolUser(AbstractUser):
    is_instructor = models.BooleanField(default=False)

    class Meta:
        db_table = 'school_user'

