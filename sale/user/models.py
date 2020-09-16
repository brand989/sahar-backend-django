from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='acrtion_img/user_images/default.jpg', upload_to='acrtion_img/user_images')
    nomber_phone = models.CharField(max_length=10)
    nomber_card = models.CharField(null=True, max_length=10)
