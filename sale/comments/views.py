from django.shortcuts import render,  get_object_or_404
from action.models import Action
from .models import Comment
from django.views.generic import ListView, CreateView

# Create your views here.
class CommentsView(ListView):
    model = Comment
    template_name  = 'comments/comments.html'
    context_object_name = 'comments'


class CommentsPartnerView(ListView):
    model = Comment
    template_name  = 'comments/partner_comments.html'
    context_object_name = 'comments'
    queryset = Comment.objects.all()

    def get_queryset(self):
        action = get_object_or_404(Action, pk = self.kwargs.get('pk'))
        return Action.objects.filter(partner=action)



    
