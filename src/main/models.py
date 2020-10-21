from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class BotPlaceManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Bot place must have an email address')

        bot_place = self.model(
            email=self.normalize_email(email),
        )

        bot_place.set_password(password)
        bot_place.save(using=self._db)
        return bot_place

    def create_superuser(self, email, password=None):
        bot_place = self.create_user(
            email,
            password,
        )

        bot_place.is_admin = True
        bot_place.save(using=self._db)
        return bot_place


class BotPlace(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    # self_slag = models.CharField(max_length=10)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = BotPlaceManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'<{self.email}>'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
