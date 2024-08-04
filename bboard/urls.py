from django.urls import path

from bboard import views

urlpatterns = [
    path("", views.index, name="index")
]
