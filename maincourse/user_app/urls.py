# admin/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('developer/', views.developer, name='develop'),
    path('settings/', views.seting, name='settings'),
]

##############################
# urlpatterns = [
#     path('blog/<int:year>/', views.year_archive),
# ]

# Этот URL-шаблон соответствует любому URL, начинающемуся с blog/ за которым следует целое число, и заканчивающемся /
# Этот целочисленный параметр будет передан во view функцию year_archive() в качестве аргумента year.

# Сопоставление URL-адресов с помощью регулярных выражений:

# urlpatterns = [
#     re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$', views.article_detail,
# name='article_detail'),
# ]