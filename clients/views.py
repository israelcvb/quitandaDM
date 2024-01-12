from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from .models import Client



class ClientCreateView(CreateView):
    model = Client
    fields = ["name", "birth_date", "gender", "address", "email", "phone", "occurrences"]
    success_url = reverse_lazy("clients:index")


class ClientDetailView(DetailView):
    model = Client



class ClientListView(ListView):
    model = Client



class ClientUpdateView(UpdateView):
    model = Client
    fields = ["name", "birth_date", "gender", "address", "email", "phone",
              "last_purchase_date", "status", "occurrences"]
    success_url = reverse_lazy("clients:index")
