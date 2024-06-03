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

from django.contrib.auth.mixins import LoginRequiredMixin








def index(request):
        return render(request, 'index.html',{'user': request.user})





@login_required
def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user_instance = form.save(commit=False)
            user_instance.user = request.user  # Associate the user
            user_instance.save()
            return redirect('view_users')  # Redirect to a success page after saving
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})

def success(request):
    return render(request, 'success.html')


def view_users(request):
    users = Users.objects.filter(user=request.user)  # Get only the logged-in user's data
    context = {'users': users}
    return render(request, 'view_users.html', context)

class UserDeleteViews(LoginRequiredMixin, DeleteView):
    model = Users
    success_url = reverse_lazy('view_users')

    def get_queryset(self):
        # Ensure users can only delete their own data
        return Users.objects.filter(user=self.request.user)

def update_user(request, user_id):
    user_instance = Users.objects.get(pk=user_id, user=request.user)  # Get the user object
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user_instance)  # Pre-populate the form
        if form.is_valid():
            form.save()
            return redirect('view_users')  # Redirect to the user list
    else:
        form = UserForm(instance=user_instance)  # Pre-populate the form with user data
    return render(request, 'update_user.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .loginform import LoginForm, RegistrationForm


from django.shortcuts import render
def home(request):
    return render(request, 'home.html', {'user': request.user})

def about(request):
    return render(request, 'about.html')



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