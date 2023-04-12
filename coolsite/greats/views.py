from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *
menu =[
    {'title':'О сайте', 'url_name':'about'},
    {'title':'Добавить статью', 'url_name':'add_page'},
    {'title':'Обратная связь', 'url_name':'contact'},
    {'title':'Войти', 'url_name':'login'},
]
def index(request):
    posts= Greats.objects.all()
    categories=Category.objects.all()
    context= {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница.',
        'cat_selected':0,
        'categories':categories
    }
    return render (request, 'greats/index.html', context=context)
def about(request):
    return render(request, 'greats/about.html', {'menu':menu,'title':'О сайте.'})
# Create your views here.
def addpage(reguest):
    return HttpResponseNotFound("Добавление статьи.")
def contact(reguest):
    return HttpResponseNotFound("Обратная связь.")
def login(reguest):
    return HttpResponseNotFound("Авторизация.")
def show_post(reguest, post_id):
    return HttpResponseNotFound(f"Отображение статьи с id={post_id}")
def pageNotFound(reguest, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def show_category(request,cat_id):
    posts = Greats.objects.filter(cat_id=cat_id)

    if len(posts)==0:
        raise Http404()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,

    }
    return render(request, 'greats/index.html', context=context)