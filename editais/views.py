from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Edital, Inscricao


# Create your views here.

class EditalList(ListView):
    template_name = 'edital/list_edital.html'
    model = Edital


class EditalDetailView(DetailView):
    model = Edital


class InscricaolList(ListView):
    template_name = 'inscricao/list_inscricao.html'
    model = Inscricao


class InscricaoDetailView(DetailView):
    model = Inscricao