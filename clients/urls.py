from django.urls import path
from . import views


app_name = "clients"
urlpatterns = [
    path("", views.ClientListView.as_view(), name="index"),
    path("<int:pk>/cliente/", views.ClientDetailView.as_view(), name="client"),
    path("<int:pk>/cliente/edicao/", views.ClientUpdateView.as_view(), name="change"),
    path("add/", views.ClientCreateView.as_view(), name="add"),
]
