from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import LoginForm
from .forms import RegisterForm
def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Connexion reussi')
                return redirect('home')
            else :
                messages.error(request,"Il y'a un problème")
            
            
        
    return render(request, 'admin/auth/login.html', {'form':form})
    
def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['name'],
                password=form.cleaned_data['password'],
            )
            messages.success(request, 'Compte crée avec succès')
            return redirect('login')
        else:
            messages.error(request, "Le formulaire n'est pas valide")
            
    return render(request, 'admin/auth/register.html', {'form':form})

def Admin_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.username=='Elixir_Groupe':
                auth_login(request, user)
                messages.success(request,'Connexion réussi!')            
                return redirect('dashboard')
            messages.error(request, "Identifiants du personnel incorrects.")
    return render(request, 'admin/auth/personnels.html', {'form': form})
def logout_view(request):
    logout(request)
    messages.success(request, "Déconnexion réussie.")
    return redirect('login')
    
