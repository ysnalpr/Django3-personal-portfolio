from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import *

# Create your views here.

def blog(request):
    blogs = Blog.objects.order_by('-date')
    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'blog/blog.html', context)

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        'blog': blog
    }

    return render(request, 'blog/detail.html', context)