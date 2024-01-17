from django.shortcuts import render
from blogs.models import  Category,Blogs
from assignments.models import About
def home(request):

    categories=Category.objects.all()
    featured_posts=Blogs.objects.filter(is_featured=True,status='Published').order_by('-update_at')
    posts=Blogs.objects.filter(is_featured=False,status='Published')
    about = About.objects.get()
    context={
        'categories':categories,
        'featured_posts':featured_posts,
        'posts':posts,
        "about":about
    }
    return  render(request,'home.html',context)

