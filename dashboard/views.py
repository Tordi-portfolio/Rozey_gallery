from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from gallery.models import Blog
from gallery.forms import BlogForm


@login_required
def dashboard(request):

    posts = Blog.objects.count()

    latest = Blog.objects.all()[:5]

    return render(request, "dashboard/dashboard.html", {
        "posts": posts,
        "latest": latest,
    })


@login_required
def artwork_list(request):

    artworks = Blog.objects.all()

    return render(request, "dashboard/artwork_list.html", {
        "artworks": artworks,
    })


@login_required
def add_artwork(request):

    form = BlogForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("artwork_list")

    return render(request, "dashboard/add_artwork.html", {
        "form": form,
    })


@login_required
def edit_artwork(request, pk):

    artwork = get_object_or_404(Blog, pk=pk)

    form = BlogForm(
        request.POST or None,
        request.FILES or None,
        instance=artwork,
    )

    if form.is_valid():
        form.save()
        return redirect("artwork_list")

    return render(request, "dashboard/add_artwork.html", {
        "form": form,
    })


@login_required
def delete_artwork(request, pk):

    artwork = get_object_or_404(Blog, pk=pk)

    if request.method == "POST":
        artwork.delete()
        return redirect("artwork_list")

    return render(request, "dashboard/delete.html", {
        "artwork": artwork,
    })