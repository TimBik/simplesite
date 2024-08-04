from django.urls import path

from bboard import views
from bboard.views import BbCreateView

urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    path("<int:rubric_id>/", views.by_rubric, name="by_rubric"),
    path("", views.index, name="index"),
]
