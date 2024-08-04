from django import forms
from .models import Cliente, Fornecedor, Produto
from django.contrib.auth.models import User

# Formulário para o modelo Cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente  # Define o modelo associado ao formulário
        fields = '__all__'  # Inclui todos os campos do modelo Cliente no formulário

from django import forms
from django.contrib.auth.forms import UserCreationForm

# Formulário de registro de usuário usando UserCreationForm
class RegisterForm(UserCreationForm):
    class Meta:
        model = User  # Define o modelo associado ao formulário
        fields = ['username', 'password1', 'password2']  # Campos incluídos no formulário

# Formulário para o modelo Fornecedor
class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor  # Define o modelo associado ao formulário
        fields = '__all__'  # Inclui todos os campos do modelo Fornecedor no formulário

# Formulário para o modelo Produto
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto  # Define o modelo associado ao formulário
        fields = '__all__'  # Inclui todos os campos do modelo Produto no formulário
