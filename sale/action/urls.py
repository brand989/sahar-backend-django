from django.urls import path
from . import views


urlpatterns = [
   
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/action_list/', views.ActionView.as_view(), name='action_list'),
    path('catalog/action_list/<int:pk>/', views.ActionCategoryView.as_view(), name='action_category_list'),
    path('catalog/action_list/detail/<int:pk>/', views.ActionDetailView.as_view(), name='action_detail'),
    path('catalog/action_list/detail/<int:pk>/creat_comments', views.CreatCommentsView.as_view(), name='creat_comments'),
    path('comment/<int:pk>/update/', views.comment_update, name='comments-update'),
    path('comment/', views.CommentView.as_view(), name='comment'),
    path('comment/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),
    path('comment/<int:pk>/delete/', views.DeleteCommentView.as_view(), name='comment-delete'),
    path('feedback/', views.feedback, name='feedback'),
    path('about/', views.about, name='about'),
    path('partners/', views.partners, name='partners'),
    path('get_card/', views.get_card, name='get_card'),
]
