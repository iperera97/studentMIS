from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


# Custom user manager
class UserManager(BaseUserManager):

    # create a user
    def create_user(self, email, is_active=True, is_staff=False, is_admin=False, password=None):

        if not email:
            raise ValueError("user must have an email address")
        elif not password:
            raise ValueError("user must have strong password")
        else:
            # create user
            user = self.model(
                email=self.normalize_email(email),
                active=is_active,
                staff=is_staff,
                admin=is_admin
            )
            user.set_password(password)
            user.save(using=self._db)
            return user

    # create super user
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=email,
            password=password,
            is_staff=True,
            is_admin=True
        )

        return user

    # create staff user
    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email=email,
            password=password,
            is_staff=True,
        )

        return user


# Custom user model
class User(AbstractBaseUser):

    # PROPERTIES
    email = models.EmailField(max_length=254, unique=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    register = models.DateTimeField(auto_now_add=True)
    # avatar = models.

    # Additional Info
    USERNAME_FIELD = 'email'
    objects = UserManager()

    # Methods
    def __str__(self):
        return "({}) {}".format(self.pk, self.email)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
