from django.db import models
from django.urls import reverse


class Greats(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="Фото")
    time_create=models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update=models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published=models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категории")


    class Meta:
        verbose_name="Выдающиеся люди"
        verbose_name_plural='Выдающиеся люди'
        ordering=['-time_create','title'] # если первое поле имеет
        # равные значения то включается сортировка по второму полю title
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id':self.pk})

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id':self.pk})
    class Meta:
        verbose_name="Категория"
        verbose_name_plural='Категории'
        ordering=['id']
# Create your models here.
    def __str__(self):
        return self.name