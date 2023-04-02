from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField(max_length=1000, blank=False, null=False)
    time_create = models.DateTimeField(default=timezone.datetime.now())

    def __str__(self):
        return self.title


# ke thua tu user va them mot so thuoc tinh cho user
class MyUser(AbstractUser):
    sex_choice = ((0, "Nữ"), (1, "Nam"), (2, "Khác"))
    age = models.IntegerField(default=0)
    sex = models.IntegerField(choices=sex_choice, default=0)
    addess = models.CharField(default='', max_length=255)
