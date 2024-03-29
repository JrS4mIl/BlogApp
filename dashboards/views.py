from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Category, Blogs
from django.contrib.auth.decorators import login_required
from .form import CategoryForm, BlogPostForm,AddUserForm,EditUserForm,EditBlogForm
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your views her
@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blogs.objects.all().count()
    context = {
        'category_count': category_count,
        'blogs_count': blogs_count,

    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required(login_url='login')
def categories(request):
    return render(request, 'dashboard/categories.html')


@login_required(login_url='login')
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/add_category.html', context)


@login_required(login_url='login')
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)

    context = {
        'form': form,
        'category': category
    }
    return render(request, 'dashboard/edit_category.html', context)


@login_required(login_url='login')
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')


@login_required(login_url='login')
def posts(request):
    posts = Blogs.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'dashboard/posts.html', context)

@login_required(login_url='login')
def add_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            title=form.cleaned_data['title']
            post.slug=slugify(title)+'-'+str(post.id)
            post.save()
            return redirect('posts')
        else:
            print('form is invalid')
    form = BlogPostForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_post.html', context)
@login_required(login_url='login')
def edit_post(request,pk):
    post=get_object_or_404(Blogs,pk=pk)
    if request.method=='POST':
        form = EditBlogForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post=form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts')



    form=EditBlogForm(instance=post)
    context = {
        'form': form,
        'post':post
    }

    return render(request,'dashboard/edit_post.html',context)
def delete_post(request,pk):
    post=get_object_or_404(Blogs,pk=pk)
    post.delete()
    return redirect('posts')
def users(request):
    users=User.objects.all()
    context={
        'users':users
    }

    return render(request,'dashboard/users.html',context)
def add_user(request):
    if request.method=='POST':
        form=AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    form=AddUserForm()

    context={
        'form':form
    }
    return render(request,'dashboard/add_user.html',context)

def edit_user(request,pk):
    user=get_object_or_404(User,pk=pk)
    if request.method=='POST':
        form=EditUserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    form=EditUserForm(instance=user)
    context = {
        'form': form,
        "user":user
    }
    return render(request,'dashboard/edit_user.html',context)
def delete_user(request,pk):
    user=get_object_or_404(User,pk=pk)
    user.delete()
    return redirect('users')