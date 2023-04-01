from django.contrib import admin

from .models import * # точка означает что файл в текущей папке

class GreatsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title','content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Greats, GreatsAdmin)
admin.site.register(Category, CategoryAdmin)
