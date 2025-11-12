import uuid
from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from encrypted_model_fields.fields import EncryptedCharField

cpf_validator = RegexValidator(
    regex=r'^(\d{3}\.?\d{3}\.?\d{3}-?\d{2})$',
    message='Digite um CPF válido (com ou sem pontuação).'
)

class Usuario(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    data_nascimento = models.DateField() # - fazer um validador/formatador para esta bomba pra evitar erros tanto no superuser quanto no user padrao

    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'data_nascimento']

    def __str__(self):
        return self.nome_completo or self.email
    
    @property
    def nome_completo(self): #retorna o nome completo a partir do first_name e last_name que já são nativos do django
        return f"{self.first_name} {self.last_name}".strip()
    
    def clean(self): #valida data de nascimento
        super().clean()
        hoje = date.today()
        if self.data_nascimento > date.today():
            raise ValidationError("Data de nascimento inválida.")
        if (hoje - self.data_nascimento).days < 18 * 365: #ajustar para a idade mínima definida nos requisitos pelo pessoal de produto
            raise ValidationError("Usuário deve ter pelo menos 18 anos.")

    @property
    def idade(self):
        hoje = date.today()
        idade = hoje.year - self.data_nascimento.year
        if (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day): #se ainda n fez aniversario este ano, corrige com -1
            idade -= 1
        return idade
    
class Perfil(models.Model):
    nome_social = models.CharField(max_length=100, blank=True, null=True)

    cpf = EncryptedCharField( #instalar django-encrypted-model-fields para garantir a segurança do cpf (pip install django-encrypted-model-fields, e lembrar de colocar uma chave secreta la no settings (antes do deploy tem q trocar e criar variavel no .env))
        max_length=14,
        unique=True,
        blank=True,
        null=True,
        validators=[cpf_validator],
        help_text='Digite um CPF válido (com ou sem pontuação).'
    )

    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True) # precisa instalar a biblioteca Pillow (pip install Pillow)

    imagem_url = models.URLField(blank=True, null=True) # PEGA IMAGEM HOSPEDADA NA NET

    descricao = models.TextField(
        max_length=500,
        blank=True,
        null=True,
    )

    is_pcd = models.BooleanField(
        default=False
    )

    neurodiversidade = models.BooleanField(
        default=False
    )

    genero = models.CharField(
        max_length=30,
        choices=[
                ('HOMEM_CIS', 'Homem cis'),
                ('MULHER_CIS', 'Mulher cis'),
                ('HOMEM_TRANS', 'Homem Trans'),
                ('MULHER_TRANS', 'Mulher Trans'),
                ('NAO_BINARIO', 'Não-binário'),
                ('AGENERO', 'Agênero'),
                ('GENERO_FLUIDO', 'Gênero fluido'),
                ('OUTRO', 'Outro'),
                ('NAO_INFORMAR', 'Prefiro não informar'),
            ],
            blank=True,
            null=True
    )

    endereco = models.ForeignKey(
        'core.Endereco',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='perfis'
    )

    usuario = models.OneToOneField(
        'Usuario',
        on_delete=models.SET_NULL, #Pode trocar pra CASCADE se quiser deletar o perfil quando deletar o usuario
        null=True,
        blank=True,
        related_name='perfil'
    )