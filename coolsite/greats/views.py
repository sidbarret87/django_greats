from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

def index(request):
    return HttpResponse("Страница приложения greats.")

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
