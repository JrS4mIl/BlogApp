from django.shortcuts import render,get_object_or_404
from .models import Category,Blogs
from django.db.models import Q

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
def search(request):
    keyword=request.GET.get('keyword')
    blogs=Blogs.objects.filter(Q(title__icontains=keyword)|Q(short_description__icontains=keyword)|Q(blog_body__icontains=keyword),status='Published')
    context={
        'blogs':blogs,
        'keyword':keyword
    }

    return render(request,'search.html',context)