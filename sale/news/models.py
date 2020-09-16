from django.db import models
from django.utils import timezone
from action.models import Action


# Create your models here.


class News (models.Model):
    title = models.TextField() 
    text = models.TextField() 
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
    
    def __str__(self):
        return self.title

class Text (models.Model):
    title = models.TextField() 
    text = models.TextField() 

    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Тексты'
    
    def __str__(self):
        return self.title


class Slider_main (models.Model):
    img = models.ImageField(default='default.jpg', upload_to='action_img/slider_main/')
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    active = models.BooleanField()
    title = models.TextField() 

    class Meta:
        verbose_name = 'Главный слайдер'
        verbose_name_plural = 'Главный слайдер'
    
    def __str__(self):
        return self.title




class Slider_small (models.Model):
    img = models.ImageField(default='default.jpg', upload_to='action_img/slider_small/')
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    active = models.BooleanField()


    class Meta:
        verbose_name = 'Боковый баннер'
        verbose_name_plural = 'Боковые баннеры'
    
    def __str__(self):
        return self.action.title


class Img(models.Model):
    img = models.ImageField(default='default.jpg', upload_to='action_img/news/')
    title = models.TextField() 

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
    
    def __str__(self):
        return self.title