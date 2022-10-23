from django.urls import path, include
from logistik.views import *

urlpatterns = [
    path('list/', list, name = 'list'),
    path('tambah/', tambah, name = 'tambah'),
    path('edit/<int:id>/', edit, name = 'edit'),
    path('hapus/<int:id>/', hapus, name = 'hapus'),
    path('logistik/', logistik, name = 'logistik'),
]
