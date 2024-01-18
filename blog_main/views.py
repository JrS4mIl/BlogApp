from django.shortcuts import render, redirect
from blogs.models import Category, Blogs
from assignments.models import About
from .forms import RegistrationsForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def home(request):
    categories = Category.objects.all()
    featured_posts = Blogs.objects.filter(is_featured=True, status='Published').order_by('-update_at')
    posts = Blogs.objects.filter(is_featured=False, status='Published')
    about = About.objects.get()
    context = {
        'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts,
        "about": about
    }
    return render(request, 'home.html', context)


def register(request):
    if request.method == "POST":
        form = RegistrationsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationsForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            else:
                return redirect('register')

    form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)
def logout(request):
    auth.logout(request)
    return redirect('home')