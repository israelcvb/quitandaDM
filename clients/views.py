from django.views.generic import DetailView, ListView
from .models import Client



class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client
