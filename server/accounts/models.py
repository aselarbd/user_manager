from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    """Define a customized user manager"""

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The email is not Given.')
        email = self.normalize_email(email=email)
        user = self.model(email=email, **extra_fields)
        user.set_password(raw_password=password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff = True permission')

        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser = True permission')

        return self.create_user(email=email, password=password, **extra_fields)


class CustomUser(AbstractBaseUser):
    """Define a customized user model"""

    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128, null=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects = CustomUserManager()

    def __repr__(self):
        return f'({self.first_name} : {self.email})'

    def has_module_perms(self, app_label):  # pylint: disable=W0613
        return True

    def has_perm(self, perm, obj=None):  # pylint: disable=W0613
        return True
