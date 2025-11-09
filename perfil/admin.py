from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Perfil


@admin.register(Usuario)
class CustomUserAdmin(UserAdmin):
    model = Usuario

    # Campos que aparecem ao visualizar/editar um usuário
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações pessoais', {
            'fields': (
                'first_name',
                'last_name',
                'data_nascimento',
            )
        }),
        ('Permissões', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )

    # Campos que aparecem ao criar um novo usuário
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'first_name',
                'last_name',
                'data_nascimento',
                'password1',
                'password2',
            ),
        }),
    )

    list_display = ('email', 'first_name', 'last_name', 'idade', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    def idade(self, obj):
        return obj.idade
    idade.short_description = 'Idade'


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'nome_social', 'genero')
    search_fields = ('cpf', 'nome_social')