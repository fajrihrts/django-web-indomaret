from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    template_name = 'index.html'
    contex = {
        'title': 'Indomart',
    }   
    return render(request, template_name, contex)

def about(request):
    template_name = 'about.html'
    contex = {
        'title': 'About',
    }   
    return render(request, template_name, contex)

def list(request):
    template_name = 'list.html'
    contex = {
        'title': 'List Produk',
    }   
    return render(request, template_name, contex)

def tambah(request):
    template_name = 'tambah.html'
    contex = {
        'title': 'Tambah Produk',
    }   
    return render(request, template_name, contex)
