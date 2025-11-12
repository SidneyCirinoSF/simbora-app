from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from datetime import date
from .models import Usuario 


IDADE_MINIMA_ANOS = 18

class UsuarioCreationForm(UserCreationForm):
    data_nascimento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Data de Nascimento'
    )

    class Meta:
        # Usa o modelo de usuário personalizado
        model = Usuario
        
        fields = ('email', 'username', 'first_name', 'last_name', 'data_nascimento')
        # Se você estiver usando o AbstractUser, 'username' já vem no UserCreationForm base,
        # mas você o incluiu em REQUIRED_FIELDS, então garantimos que está aqui.

   
   
    def clean_data_nascimento(self):
        data_nascimento = self.cleaned_data.get('data_nascimento')

        if data_nascimento:
            hoje = date.today()
            
    
            if data_nascimento > hoje:
                raise forms.ValidationError("Data de nascimento inválida: Não pode ser uma data futura.")
            
           
            idade = hoje.year - data_nascimento.year
            if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
                idade -= 1
                
            if idade < IDADE_MINIMA_ANOS:
                raise forms.ValidationError(f"Usuário deve ter pelo menos {IDADE_MINIMA_ANOS} anos.")

        return data_nascimento

    def save(self, commit=True):
        user = super().save(commit=False)
        
        if commit:
            user.save()
        return user