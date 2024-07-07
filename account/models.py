from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('Email Address is a Required Field.')

        if not username:
            raise ValueError('User must have an Username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name
        )

        user.is_active = True
        # Hashing of Password in Django ....
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(email=self.normalize_email(email), username=username, password=password,
                                first_name=first_name, last_name=last_name)
        user.is_editor = False
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def create_editor(self, first_name, last_name, email, username, password):
        user = self.create_user(email=self.normalize_email(email), username=username, password=password,
                                first_name=first_name, last_name=last_name)
        # General Flags
        user.is_editor = True
        user.is_superuser = False
        user.is_staff = False
        user.save(using=self._db)


# Account Fields
class Account(AbstractBaseUser):
    # Basic Fields
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    phone_no = models.CharField(max_length=50, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)

    # Access Modifiers ...
    is_editor = models.BooleanField(default=False)

    # Django Default Access Modifier Fields ...
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # Configuring the logi section for the super admin user ...
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', ]

    object = MyAccountManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, add_label):
        return True

    def get_full_name(self):
        return self.first_name.capitalize() + ' ' + self.last_name.capitalize()

    def check_editor(self):
        return self.is_editor

    class Meta:
        db_table = 'accounts'
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
