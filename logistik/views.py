from django.shortcuts import render, redirect
from logistik.models import Produk, Kategori
from django.http import HttpResponse

def list (request):
    template_name = 'list.html'
    produk = Produk.objects.all()
    context = {
        'title': 'List Produk',
        'produk': produk,
    }   
    return render(request, template_name, context,)

def logistik (request):
    template_name = 'logistik.html'
    produk = Produk.objects.all()
    context = {
        'title': 'Logistik',
        'produk': produk,
    }   
    return render(request, template_name, context)

def tambah (request):
    template_name = 'tambah.html'
    kategori = Kategori.objects.all()
    if request.method == 'POST':
        input_kategori = request.POST.get('kategori')
        input_nama = request.POST.get('nama')
        input_harga = request.POST.get('harga')
        input_stok = request.POST.get('stok')
        input_deskripsi = request.POST.get('deskripsi')

        get_kategori = Kategori.objects.get(nama = input_kategori)
        Produk.objects.create(
            nama = input_nama,
            harga = input_harga,
            stok = input_stok,
            deskripsi = input_deskripsi,
            kategori = get_kategori,
        )
        return redirect('list')

    context = {
        'title': 'Tambah Produk',
        'kategori': kategori,
    }   
    return render(request, template_name, context)

def edit (request, id):
    template_name = 'tambah.html'
    get_produk = Produk.objects.get(id = id)
    kategori = Kategori.objects.all()
    if request.method == 'POST':
        input_kategori = request.POST.get('kategori')
        input_nama = request.POST.get('nama')
        input_harga = request.POST.get('harga')
        input_stok = request.POST.get('stok')
        input_deskripsi = request.POST.get('deskripsi')

        get_kategori = Kategori.objects.get(nama = input_kategori)

        get_produk.nama = input_nama
        get_produk.harga = input_harga
        get_produk.stok = input_stok
        get_produk.deskripsi = input_deskripsi
        get_produk.kategori = get_kategori
        get_produk.save()       
        return redirect('list')

    context = {
        'title': 'Edit Produk',
        'get_produk': get_produk,
        'kategori': kategori,
    }   
    return render(request, template_name, context)

def hapus (request, id):
    Produk.objects.filter(id = id).delete()
    return redirect('list')
