from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *
menu =['О сайте','Добавить статью', 'Обратная связь', "Войти"]
def index(request):
    posts= Greats.objects.all().order_by('title')
    return render (request, 'greats/index.html', {'posts':posts,'menu':menu,'title':'Главная страница.'})
def about(request):
    return render(request, 'greats/about.html', {'menu':menu,'title':'О сайте.'})
def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")
# Create your views here.
def pageNotFound(reguest, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
def archive(request,year):
    if int(year)>2023:
    # инструкция raise позволяет программисту принудительно вызвать
    # указанную функцию
        return redirect('home', permanent=False)
    return HttpResponse(f"<h1>Архив по  годам</h1><p>{year}</p>")
