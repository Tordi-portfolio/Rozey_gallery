from django.shortcuts import render, get_object_or_404

from .models import Blog, Category


def home(request):

    featured = Blog.objects.filter(featured=True)[:6]

    latest = Blog.objects.all()[:6]

    categories = Category.objects.all()

    return render(
        request,
        "home.html",
        {
            "featured": featured,
            "latest": latest,
            "categories": categories
        }
    )

def blog_list(request):

    blogs = Blog.objects.all()

    return render(request, "blog/blog_list.html", {
        "blogs": blogs
    })


def blog_detail(request, slug):

    blog = get_object_or_404(Blog, slug=slug)

    return render(request, "blog/blog_detail.html", {
        "blog": blog
    })