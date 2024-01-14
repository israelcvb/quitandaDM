from django.urls import path
from . import views


app_name = "clients"
urlpatterns = [
    path("", views.ClientListView.as_view(), name="index"),
    path("<int:pk>/cliente/", views.ClientDetailView.as_view(), name="client"),
    path("<int:pk>/cliente/edicao/", views.ClientUpdateView.as_view(), name="change"),
    path("novo/", views.ClientCreateView.as_view(), name="add"),
    path("<int:pk>/cliente/remocao/", views.ClientDeleteView.as_view(), name="delete"),
]
