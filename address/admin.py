from django.contrib import admin
from .models import Endereco

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('rua', 'numero', 'cidade', 'estado', 'cep')
    search_fields = ('rua', 'cidade', 'estado', 'cep')