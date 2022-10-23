from django.contrib import admin
from logistik.models import *
# Register your models here.
admin.site.register(Kategori)
class ProdukAdmin(admin.ModelAdmin):
    list_display = ('nama', 'harga', 'stok', 'deskripsi', 'kategori')
admin.site.register(Produk, ProdukAdmin)