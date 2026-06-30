from django.urls import path

from . import views

urlpatterns = [

    path("", views.dashboard, name="dashboard"),

    path("artworks/", views.artwork_list, name="artwork_list"),

    path("add/", views.add_artwork, name="add_artwork"),

    path("edit/<int:pk>/", views.edit_artwork, name="edit_artwork"),

    path("delete/<int:pk>/", views.delete_artwork, name="delete_artwork"),

]