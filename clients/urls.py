from django.urls import path
from . import views


app_name = "clients"
urlpatterns = [
    path("", views.ClientListView.as_view(), name="clients"),
    path("<int:pk>/cliente/", views.ClientDetailView.as_view(), name="client")
]