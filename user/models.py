import uuid
from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

cpf_validator = RegexValidator(
    regex=r'^(\d{3}\.?\d{3}\.?\d{3}-?\d{2})$',
    message='Digite um CPF válido (com ou sem pontuação).'
)

class Usuario(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome_completo = models.CharField(max_length=255)
    #primeiro_nome -> chamar por first_name (padrão do django)
    #ultimo_nome -> chamar por last_name (padrão do django)
    nome_social = models.CharField(max_length=100, blank=True, null=True)
    cpf = models.CharField(
        max_length=14,
        unique=True,
        validators=[cpf_validator],
        help_text='Digite um CPF válido (com ou sem pontuação).'
    )
    data_nascimento = models.DateField() # - fazer um validador para esta bomba pra evitar erros tanto no superuser quanto no user padrao
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True) # precisa instalar a biblioteca Pillow (pip install Pillow)
    imagem_url = models.URLField(blank=True, null=True) # PEGA IMAGEM HOSPEDADA NA NET
    genero = models.CharField(
    max_length=30,
    choices=[
            ('MASCULINO', 'Masculino'),
            ('FEMININO', 'Feminino'),
            ('TRANS_MASCULINO', 'Transmasculino'),
            ('TRANS_FEMININO', 'Transfeminino'),
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
        'address.Endereco',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='usuarios'
    )

    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'cpf', 'nome_completo', 'data_nascimento']

    def __str__(self):
        return self.nome_completo or self.email
    
    def clean(self): #valida data de nascimento
        super().clean()
        if self.data_nascimento > date.today():
            raise ValidationError("Data de nascimento inválida.")

    @property
    def idade(self):
        hoje = date.today()
        idade = hoje.year - self.data_nascimento.year
        if (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day): #se ainda n fez aniversario este ano, corrige com -1
            idade -= 1
        return idade