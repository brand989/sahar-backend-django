from django.shortcuts import render,  get_object_or_404
from .models import Section, Category, Action
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from comments.models import Comment
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentUpdateForm, ContactForm, PartnersForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from news.models import News, Text, Slider_main, Slider_small

# Create your views here.

def index(request):

    data = {
        'title':'САХАР | Проект рекламного агентства Креатив',
        'news' : News.objects.order_by('-date')[:3],
        'text' : Text.objects.filter(title='Главная страница'),
        'slider_main' : Slider_main.objects.all(),
        'slider_small' : Slider_small.objects.filter(active = True)[:3],
        'count_action' : Action.objects.count()
    }

    return render(request, 'action/index.html', data )

def about(request):
    data = {
        'title':'САХАР | Проект рекламного агентства Креатив',
        'news' : News.objects.order_by('-date')[:3],
        'text' : Text.objects.filter(title='О проекте '),
        'slider_small' : Slider_small.objects.filter(active = True)[:3],
    }

    return render(request, 'action/about.html', data )


def catalog(request):
    data = {
        'section' : Section.objects.all(),
        'category' : Category.objects.all(),
        'action' : Action.objects.all(),
        'title': 'Страница каталог'
    }

    return render(request, 'action/catalog.html', data)

class ActionView(ListView):
    model = Action
    template_name  = 'action/action_list.html'
    context_object_name = 'action'


class ActionCategoryView(ListView):
    template_name = 'action/action_category_list.html'
    model = Action
    context_object_name = 'action'
    queryset = Action.objects.all()

    def get_queryset(self):
        categor = get_object_or_404(Category, pk = self.kwargs.get('pk'))
        return Action.objects.filter(category=categor)

    def get_context_data(self, **kwards):
        ctx = super(ActionCategoryView ,self).get_context_data(**kwards)
        ctx['title']= get_object_or_404(Category, pk = self.kwargs.get('pk'))
        
        return ctx

class ActionDetailView(DetailView):
    template_name = 'action/action_detail.html'
    model = Action
    context_object_name = 'action'

    def get_context_data(self, **kwards):
        ctx = super(ActionDetailView ,self).get_context_data(**kwards)
        ctx['comments']=Comment.objects.filter(partner=self.get_object())
        

        return ctx

class CreatCommentsView (CreateView):
    model = Comment
    fields = ['text' ]
    get_absolute_url = 'index'

    def form_valid(self, form):
        form.instance.avtor=self.request.user
        form.instance.partner= get_object_or_404(Action, pk = self.kwargs.get('pk'))
        self.object = form.save()
        return redirect('index')

    
class CommentView(ListView):
    model = Comment
    template_name  = 'action/comment.html'
    context_object_name = 'comment'


class CommentDetailView(DetailView):
    model = Comment
    template_name  = 'action/comment-detail.html'
    context_object_name = 'comment'


class UpdateCommentsView(UpdateView):
    model = Comment
    fields = ['text']

    def form_valid(self, form):
        form.instance.avtor=self.request.user
        form.instance.partner= get_object_or_404(Action, pk = self.kwargs.get('pk'))
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()


def comment_update(request):
    if request.method == "POST":
        form = CommentUpdateForm(request.POST, instance=request.comment)
        if form.is_valid():  
            form.save()
            return redirect('index')
    else:
        form = CommentUpdateForm(instance=request.comment)


    return render(request, 'action/comment_update.html', {'form': form })


class DeleteCommentView(DeleteView):
    model = Comment
    success_url = '/'


def feedback(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
      
        if form.is_valid():
            email_subject = ' Сообщение через контактную форму '
            email_body = "С сайта отправлено новое сообщение\n\n" \
                         "Имя отправителя: %s \n" \
                         "номер отправителя: %s \n\n" \
                         "Сообщение: \n" \
                         "%s " % \
            (form.cleaned_data['name'], form.cleaned_data['nomber'], form.cleaned_data['message'])
            from_email = 'info@lisa.com.ru'
            send_mail(email_subject, email_body, from_email, ['brand989@gmail.com'], fail_silently=False)
            return redirect('index')
        else:
            return HttpResponse('Убедитесь, что все поля введены и действительны')
    else:
        form = ContactForm(initial={'name': ' ','nomber':' ','message ':''})
        return render(request, 'action/feedback.html', {'form': form }) 


def partners(request):
    if request.method == "POST":
        form = PartnersForm(request.POST)
      
        if form.is_valid():
            email_subject = ' Сообщение через контактную форму '
            email_body = "С сайта отправлено заявка на партнерство\n\n" \
                         "название компании: %s \n" \
                         "Имя отправителя: %s \n" \
                         "номер отправителя: %s \n\n" \
                         "Сообщение: \n" \
                         "%s " % \
            (form.cleaned_data['company'], form.cleaned_data['name'], form.cleaned_data['nomber'], form.cleaned_data['message'])
            from_email = 'info@lisa.com.ru'
            send_mail(email_subject, email_body, from_email, ['brand989@gmail.com'], fail_silently=False)
            return redirect('index')
        else:
            return HttpResponse('Убедитесь, что все поля введены и действительны')
    else:
        form = PartnersForm(initial={'company': ' ','name': ' ','nomber':' ','message ':''})
        data = {
        'title':'САХАР | Проект рекламного агентства Креатив',
        'news' : News.objects.order_by('-date')[:3],
        'text' : Text.objects.filter(title='ПАРТНЕРАМ'),
        'form': form,
    }
        return render(request, 'action/partners.html', data ) 

def get_card(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
      
        if form.is_valid():
            email_subject = ' Сообщение через контактную форму '
            email_body = "С сайта отправлено заявка на карту\n\n" \
                         "Имя отправителя: %s \n" \
                         "номер отправителя: %s \n\n" \
                         "Сообщение: \n" \
                         "%s " % \
            ( form.cleaned_data['name'], form.cleaned_data['nomber'], form.cleaned_data['message'])
            from_email = 'info@lisa.com.ru'
            send_mail(email_subject, email_body, from_email, ['brand989@gmail.com'], fail_silently=False)
            return redirect('index')
        else:
            return HttpResponse('Убедитесь, что все поля введены и действительны')
    else:
        form = ContactForm(initial={'name': ' ','nomber':' ','message ':''})
        data = {
        'title':'САХАР | Проект рекламного агентства Креатив',
        'news' : News.objects.order_by('-date')[:3],
        'text' : Text.objects.filter(title='Получить карту'),
        'form': form,
        }
        return render(request, 'action/get_card.html', data ) 