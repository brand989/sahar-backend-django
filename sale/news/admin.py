from django.contrib import admin
from .models import News, Text, Slider_main, Slider_small, Img


# Register your models here.
admin.site.register(News)
admin.site.register(Text)
admin.site.register(Slider_main)
admin.site.register(Slider_small)
admin.site.register(Img)

