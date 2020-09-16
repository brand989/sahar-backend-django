from django.shortcuts import render,  get_object_or_404
from action.models import Action
from .models import News, Slider_small
from django.views.generic import ListView, DetailView


# Create your views here.
class NewsView(ListView):
    model = News
    template_name  = 'news/news.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 2

    def get_context_data(self, **kwards):
            ctx = super(NewsView ,self).get_context_data(**kwards)
            ctx['slider_small']=Slider_small.objects.filter(active = True)[:3]

            return ctx



class NewsDetailView (DetailView): 
    model = News
   
    def get_context_data(self, **kwards):
            ctx = super(NewsDetailView ,self).get_context_data(**kwards)
            ctx['news']=News.objects.exclude(pk = self.kwargs['pk']).order_by('-date')[:3]
            ctx['slider_small']=Slider_small.objects.filter(active = True)[:3]

            return ctx

