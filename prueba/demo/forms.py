from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomTextInput(forms.widgets.TextInput):
    def __init__(self, placeholder_text='', *args, **kwargs):
        super().__init__(*args, **kwargs)

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(label='Correo', widget=CustomTextInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(label='Nombre', widget=CustomTextInput(attrs={'placeholder': 'Nombre de usuario'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña'}))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        return username
