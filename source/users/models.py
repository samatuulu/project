from django.contrib.auth.models import User
from django.db import models


class UserData(models.Model):
    user = models.OneToOneField(User, related_name='user_data', verbose_name='User', on_delete=models.CASCADE)
    about = models.TextField(max_length=1000, null=True, blank=True, verbose_name='About')

    def __str__(self):
        return self.user.pk

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
