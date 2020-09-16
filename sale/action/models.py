from django.db import models

# Create your models here.
class Section (models.Model):
	name = models.CharField(max_length=100)
	img = models.ImageField(default='default.jpg', upload_to='action_img')

class Category (models.Model):
	name = models.CharField(max_length=100)
	section = models.ForeignKey(Section, on_delete=models.CASCADE)
   

class Action (models.Model):
	title = models.CharField(max_length=100)
	sale = models.CharField(max_length=10)
	phone = models.CharField(max_length=20)
	site = models.CharField(max_length=30)
	adress = models.CharField(max_length=100)
	url_adress = models.CharField(max_length=500)
	text = models.TextField()
	img = models.ImageField(default='default.jpg', upload_to='action_img/detail/')
	img_title = models.ImageField(default='default.jpg', upload_to='action_img/detail/')
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	type_sale = models.CharField(max_length=10)
