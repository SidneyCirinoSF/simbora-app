from django.urls import path

from . import views

urlpatterns = [
    path('cadastro-login/', views.cadastro_login,name='cadastro_login'),
]