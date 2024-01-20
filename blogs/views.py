from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from .models import Category,Blogs,Comment
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
    if request.method=='POST':
        comment=Comment()
        comment.user=request.user
        comment.blog=blog
        comment.commet=request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)

    comments=Comment.objects.filter(blog=blog)
    comment_count=comments.count()
    print(comments)
    context={
        "blog":blog,
        'comments':comments,
        'comment_count':comment_count
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