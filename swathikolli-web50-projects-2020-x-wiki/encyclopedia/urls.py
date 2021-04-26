from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("random", views.random, name="random"),
    path("search", views.search, name="search"),
    path("newpage", views.newpage, name="newpage"),
    path("submitted", views.submitted, name="submitted"),
    path("cancel", views.cancel, name="cancel"),
    path("edit", views.edit, name="edit"),
     path("editted", views.editted, name="editted"),
    path("delete", views.delete, name="delete"),
    path("owner", views.owner, name="owner"),
    path("wiki/<str:name>", views.wiki_entries, name="wiki_entries")
    

]
