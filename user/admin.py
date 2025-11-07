from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class CustomUserAdmin(UserAdmin):
    model = Usuario

    # Campos que aparecem ao visualizar/editar um usuário
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações pessoais', {
            'fields': (
                'nome_completo',
                'nome_social',
                'cpf',
                'data_nascimento',
                'genero',
                'foto_perfil',
                'imagem_url',
                'endereco',
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

    # Campos que aparecem ao criar um novo usuário no admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'cpf',
                'nome_completo',
                'data_nascimento',
                'password1',
                'password2',
                'endereco'
            ),
        }),
    )

    # Campos exibidos na listagem
    list_display = ('email', 'nome_completo', 'cpf', 'genero', 'is_staff')
    search_fields = ('email', 'nome_completo', 'cpf')
    ordering = ('email',)