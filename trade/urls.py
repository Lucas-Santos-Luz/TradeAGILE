from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home, name='home'),
    path('cadastro_clientes/', views.cadastro_clientes, name='cadastro_clientes'),
    path('demonstrativo_tabelas/', views.demonstrativo_tabelas, name='demonstrativo_tabelas'),
    path('galeria_produtos/', views.galeria_produtos, name='galeria_produtos'),
    path('cadastro_fornecedores/', views.cadastro_fornecedores, name='cadastro_fornecedores'),
    path('cadastro_produtos/', views.cadastro_produtos, name='cadastro_produtos'),
    path('realizar_venda/', views.realizar_venda, name='realizar_venda'),
]
