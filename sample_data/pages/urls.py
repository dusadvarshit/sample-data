from django.urls import path
from pages import views

urlpatterns = [
    path("", views.home, name='home'),
    path("bios", views.bio_index, name='bios'),
]