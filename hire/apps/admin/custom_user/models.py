from django.contrib.auth.models             import AbstractUser, BaseUserManager
from django.db                              import models


class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password=None, is_active=True, is_staff=False, is_superuser=False):
        if not username:
            raise ValueError("Users must have a username")
        if not password:
            raise ValueError("Users must have a password")
        if not email:
            raise ValueError("Users must have an email address")

        user_obj = self.model(
            username=username
        )
        user_obj.set_password(password)
        user_obj.is_active    = is_active
        user_obj.is_staff     = is_staff
        user_obj.is_superuser = is_superuser
        user_obj.email        = email
        user_obj.save(using=self._db)

        return user_obj

    def create_staffuser(self, username, email, password=None):
        user = self.create_user(
            username = username,
            password = password,
            email    = email,
            is_staff = True
        )

        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username     = username,
            password     = password,
            email        = email,
            is_superuser = True,
            is_staff     = True
        )

        return user


class CustomUser(AbstractUser):
    ph_mobile = models.CharField('Mobile', max_length=20, null=True, blank=True)
    ph_mobile_2 = models.CharField('Mobile 2', max_length=20, null=True, blank=True)

    date_birth = models.DateField(null=True, blank=True)

    objects = CustomUserManager()

    class Meta:
        app_label = 'custom_user'
        db_table  = 'user_custom_users'

    def save(self, *args, **kwargs):
        self.username = self.username.lower()
        return super(CustomUser, self).save(*args, **kwargs)

    def get_full_name(self):
        if self.first_name:
            return self.first_name + ' ' + self.last_name
        return self.username

    def __str__(self):
        return self.username
