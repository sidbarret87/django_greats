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
    posts= Greats.objects.all().order_by('title')
    context= {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница.'
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

