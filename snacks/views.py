from django.views.generic import ListView, DetailView
from .models import Snacks

class SnackListView(ListView):
  template_name = 'snack_list.html'
  model = Snacks
