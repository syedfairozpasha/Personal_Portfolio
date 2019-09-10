from django.shortcuts import render,get_object_or_404

from .models import Blog

blogs = Blog.objects

def BlogHandler(request):
    return render(request,'blogs\BlogsHomePage.html',{"blogs": blogs})

def detailblogs(request,blog_id):
    detailblog = get_object_or_404(Blog,pk=blog_id)
    return render(request,'blogs\DetailBlog.html',{"detailblog":detailblog})
