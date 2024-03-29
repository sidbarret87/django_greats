from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *
menu =[
    {'title':'О сайте', 'url_name':'about'},
    {'title':'Добавить статью', 'url_name':'add_page'},
    {'title':'Обратная связь', 'url_name':'contact'},
    {'title':'Войти', 'url_name':'login'},
]
class GreatsHome(ListView):
    model = Greats
    template_name = 'greats/index.html'
    context_object_name = 'posts'


    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu']=menu
        context['title']="Главная страница"
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Greats.objects.filter(is_published=True)
# def index(request):
#     posts= Greats.objects.all()
#     categories=Category.objects.all()
#     context= {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Главная страница.',
#         'cat_selected':0,
#         'categories':categories
#     }
#     return render (request, 'greats/index.html', context=context)
def about(request):
    return render(request, 'greats/about.html', {'menu':menu,'title':'О сайте.'})
# Create your views here.
# def addpage(request):
#      if request.method=='POST':
#          form = AddPostForm(request.POST, request.FILES)
#          if form.is_valid():
#              #print(form.cleaned_data)
#
#                  form.save()
#                  return redirect('home')
#
#      else:
#          form = AddPostForm()
#      return render(request, 'greats/addpage.html',{'form':form,'menu':menu, 'title':'Добавление статьи'})
class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'greats/addpage.html'
    success_url = reverse_lazy('home')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        context['menu'] = menu
        return context
def contact(reguest):
    return HttpResponseNotFound("Обратная связь.")
def login(reguest):
    return HttpResponseNotFound("Авторизация.")
# def show_post(request, post_slug):
#     post = get_object_or_404(Greats, slug=post_slug)
#     context ={
#         'post':post,
#         'menu':menu, # Главное меню
#         'title': post.title, # Заголовок
#         'cat_selected':post.cat_id # номер выбранной рубрики
#     }
#     return render(request, 'greats/post.html',context=context)
class ShowPost(DetailView):
    model = Greats.
    template_name = 'greats/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name ='post'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context
def pageNotFound(reguest, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

class GreatsCategory(ListView):
    model = Greats
    template_name = 'greats/index.html'
    context_object_name = 'posts'
    allow_empty = False
    def get_queryset(self):
        return Greats.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - '+str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context

# def show_category(request,cat_id):
#     posts = Greats.objects.filter(cat_id=cat_id)
#
#     if len(posts)==0:
#         raise Http404()
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Отображение по рубрикам',
#         'cat_selected': cat_id,
#
#     }
#     return render(request, 'greats/index.html', context=context)