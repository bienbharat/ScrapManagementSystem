from __future__ import unicode_literals

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.regex import phoneRegex


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **kwargs):
        if not email or kwargs.get("Name") is not True:
            raise ValueError("Not a valid Email or name")
        if email:
            user_name = self.normalize_email(email)
        if kwargs.get("Name") is True:
            name = kwargs.get("Name")
            user_name = self.normalize_email(name)

        user = self.model(username=user_name, **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('IsVerified', True)  # todo: change field name to has_emailVerified
        kwargs.setdefault('IsActive', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Others", "Others"),
    )
    id = models.AutoField(primary_key=True, db_column="id")
    EmailId = models.EmailField(_('EmailId'), unique=True, db_column='email_id')
    Name = models.CharField(_('FirstName'), max_length=30, blank=True, db_column='first_name')
    Gender = models.CharField(_('Gender'), max_length=100, choices=GENDER_CHOICES, default="Male", db_column="gender")
    Mobile = models.CharField(_('Mobile'), validators=[phoneRegex], max_length=17, blank=True, null=True, db_column="mobile")
    Photo = models.ImageField(_('Photo'), blank=True, db_column='photo')
    CreatedOn = models.DateTimeField(_('CreatedOn'), auto_now_add=True, null=True, db_column="created_on")
    UpdatedOn = models.DateTimeField(_('UpdatedOn'), auto_now=True, null=True, db_column="updated_on")
    IsVerified = models.BooleanField(_('IsEmailVerified'), default=False, db_column="is_emailVerified")
    is_superuser = models.BooleanField(_('IsSuperuser'), default=False, db_column="is_superuser")
    IsActive = models.BooleanField(_('IsActive'), default=False, db_column="is_active")
    is_staff = models.BooleanField(_('is_staff'), default=False, db_column="is_staff")
    LastLoginIP = models.GenericIPAddressField(blank=True, null=True, db_column="last_login_ip")

    objects: UserManager = UserManager()

    USERNAME_FIELD = 'EmailId'
    REQUIRED_FIELDS = ["Name", "Mobile", "Password"]

    class Meta:
        db_table = 'users'
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def get_full_name(self):
        full_name = self.Name
        return full_name

    def get_mobile(self):
        return self.Mobile

    def set_random_password(self):
        password = UserManager().make_random_password()
        self.set_password(password)
        return password

    def __str__(self):
        return self.get_full_name()