from django.forms import inlineformset_factory
from django.shortcuts import render
from django.views.generic import DetailView, ListView


from .forms import EditalForm, PerguntaForm
from .models import Edital, Inscricao, Pergunta


# Create your views here.

class EditalList(ListView):
    template_name = 'edital/list_edital.html'
    model = Edital


class EditalDetailView(DetailView):
    model = Edital


def addEdital(request):
    form_Pergunta_factory = inlineformset_factory(Edital,Pergunta,form=PerguntaForm,extra=3)
    context = {}
    context['form'] = EditalForm()
    context['formPerguntas'] = form_Pergunta_factory()


    return render(request,'edital/add_edital.html', context)




class InscricaolList(ListView):
    template_name = 'inscricao/list_inscricao.html'
    model = Inscricao

class InscricaoDetailView(DetailView):
    model = Inscricao



