from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),

    path("gallery/", views.blog_list, name="gallery"),

    path(
        "gallery/<slug:slug>/",
        views.blog_detail,
        name="blog_detail",
    ),
]