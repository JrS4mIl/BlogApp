from django.shortcuts import render,get_object_or_404
from .models import Category,Blogs


# Create your views here.
def post_by_category(request,category_id):
    posts=Blogs.objects.filter(status='Published',category=category_id)
    category=get_object_or_404(Category,pk=category_id)
    context={
        'posts':posts,
        "category":category,
    }
    return render(request,'post_by_category.html',context)

def single_blog(request,slug):
    blog=get_object_or_404(Blogs,slug=slug,status='Published')
    context={
        "blog":blog,
    }
    return render(request,'blog.html',context)