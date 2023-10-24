from django.shortcuts import render,HttpResponse
from blog.models import Post,Category
# Create your views here.

def home(request):

    posts = Post.objects.all()[:5]
    # print(posts)
    cats = Category.objects.all()
    data = {
        'post':posts,
        'cat':cats
    }
    return render(request,'home.html',data)

def posts(request,url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    print(post)
    return render(request,'posts.html',{'post':post,'cat':cats})

def category(request,url):
    cat = Category.objects.get(url=url)
    post = Post.objects.filter(cat=cat)
    print(post)
    return render(request,'category.html',{'posts':post,'cats':cat})