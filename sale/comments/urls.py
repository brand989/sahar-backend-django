from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.CommentsView.as_view(), name='comments'),

]