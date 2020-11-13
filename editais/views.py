from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView


from .forms import EditalForm, PerguntaForm
from .models import Edital, Inscricao, Pergunta




#Edital área
class EditalList(ListView):
    template_name = 'edital/list_edital.html'
    model = Edital


def edital_view(request, id):
    context = {}
    edital= get_object_or_404(Edital, pk=id)
    perguntas = edital.pergunta_set.all()
    context['edital'] = edital
    context['perguntas'] = perguntas
    return render(request,'edital/view_edital.html',context)

def edital_add(request):
    form_Pergunta_factory = inlineformset_factory(Edital, Pergunta, form=PerguntaForm, min_num=1, extra=1)
    edital = Edital()
    context = {}

    if request.method == 'POST':
        form = EditalForm(request.POST or None, request.FILES or None, instance=edital, prefix='edital')
        pergunta_form = form_Pergunta_factory(request.POST or None, request.FILES or None, instance=edital, prefix='perguntas')

        print('---------')
        print(request)

        if form.is_valid() and pergunta_form.is_valid():
            form = form.save(commit=False)
            form.save()
            pergunta_form.save()
            return redirect('/editais/')
        else:
            context['form'] = EditalForm(request.POST or None, request.FILES or None, instance=edital, prefix='edital')
            context['form_Perguntas'] = form_Pergunta_factory(request.POST or None, request.FILES or None,instance=edital, prefix='perguntas')

    else:
        context['form'] = EditalForm( instance=edital, prefix='edital')
        context['form_Perguntas'] = form_Pergunta_factory(instance=edital, prefix='perguntas')


    return render(request,'edital/add_edital.html', context)


def edital_delete(request, id):
    edital = get_object_or_404(Edital, pk=id)
    edital.delete()

    return redirect('/editais/')






#Inscrição área
class InscricaolList(ListView):
    template_name = 'inscricao/list_inscricao.html'
    model = Inscricao

class InscricaoDetailView(DetailView):
    model = Inscricao



