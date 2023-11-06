from django.contrib.auth.models import AbstractUser
from django.db                  import models


class CustomUser(AbstractUser):

    date_birth  = models.DateField(null=True, blank=True)
    cell_number = models.CharField('Mobile', max_length=20, null=True, blank=True)

    def __str__(self):
        return self.username
