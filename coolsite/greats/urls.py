from django.urls import path
from greats.views import *

urlpatterns = [
    path('', index),
    path('cats/',categories)
]

