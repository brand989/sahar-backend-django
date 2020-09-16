from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from action.models import Action

# Create your models here.


class Comment(models.Model):
    text = models.TextField() 
    partner = models.ForeignKey(Action, on_delete=models.CASCADE)
    avtor = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)