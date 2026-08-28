from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='Nom d utilisateur', max_length=150)
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(label='Nom d utilisateur', max_length=150)
    name = forms.CharField(label='Nom complet', max_length=150)
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Ce nom d utilisateur est deja utilise.')
        return username
    