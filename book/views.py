from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from .forms import UserForm
from .models import Users
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from .forms import UserForm  # Import your update form
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required







def index(request):
        return render(request, 'index.html',{'user': request.user})





def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Save the user data to the database
            form.save()
            return redirect('/view_users/')  # Redirect to a success page after saving
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})


def success(request):
    return render(request, 'success.html')


def view_users(request):
    users = Users.objects.all()  # Get all users
    context = {'users': users}
    return render(request, 'view_users.html', context)

class UserDeleteViews(DeleteView):
    model = Users
    success_url = reverse_lazy('view_users')

def update_user(request, user_id):
    user = Users.objects.get(pk=user_id)  # Get the user object
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)  # Pre-populate the form
        if form.is_valid():
            form.save()
            return redirect('view_users')  # Redirect to the user list
    else:
        form = UserForm(instance=user)  # Pre-populate the form with user data
    return render(request, 'update_user.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth import login
from .loginform import LoginForm, RegistrationForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Get the authenticated user instance
            login(request, user)
            return redirect('index')  # Redirect to the named route 'index'
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Don't save yet
            user.set_password(form.cleaned_data['password'])  # Hash password before saving
            user.save()
            login(request, user)
            return redirect('login')  # Redirect to the named route 'index'
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout