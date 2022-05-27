from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings
# Create your models here.


class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})


class CustomUser(AbstractUser):
    objects = CustomUserManager()


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Booking(BaseModel):
    description = models.CharField(max_length=250)
    value = models.DecimalField(max_digits=14, decimal_places=2)
    currency = models.CharField(max_length=3, default='EUR')
    date = models.DateField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    @property
    def short_description(self):
        """returns the first 30 characters of the description"""
        return self.description if len(self.description) < 30 else (self.description[:26] + ' ...')

    def __str__(self):
        return 'Booking: {}'.format(self.id)
