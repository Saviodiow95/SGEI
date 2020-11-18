from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView


from .forms import EditalForm, PerguntaForm, AlternativaForm
from .models import Edital, Inscricao, Pergunta, Alternativa


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
    form_Pergunta_factory = inlineformset_factory(Edital, Pergunta, form=PerguntaForm, extra=1)
    edital = Edital()
    context = {}

    if request.method == 'POST':
        form = EditalForm(request.POST or None, request.FILES or None, instance=edital, prefix='edital')
        pergunta_form = form_Pergunta_factory(request.POST or None, request.FILES or None, instance=edital, prefix='perguntas')



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


def  edital_edit(request, id):
    form_Pergunta_factory = inlineformset_factory(Edital, Pergunta, form=PerguntaForm, extra=1)
    context = {}
    edital = get_object_or_404(Edital, pk=id)

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
            context['form_Perguntas'] = form_Pergunta_factory(request.POST or None, request.FILES or None,
                                                              instance=edital, prefix='perguntas')

    else:
        context['form'] = EditalForm(instance=edital, prefix='edital')
        context['form_Perguntas'] = form_Pergunta_factory(instance=edital, prefix='perguntas')


    return render(request,'edital/add_edital.html', context)



def edital_delete(request, id):
    edital = get_object_or_404(Edital, pk=id)
    edital.delete()

    return redirect('editais:edital_list')



#------------------- Perguntas ---------------------

def pergunta_add(request, id_edital):
    form_alternativa_factory = inlineformset_factory(Pergunta, Alternativa, form=AlternativaForm, extra=1)

    edital = get_object_or_404(Edital, pk=id_edital)
    pergunta = Pergunta()
    pergunta.edital = edital
    context = {}

    if request.method == 'POST':


        form = PerguntaForm(request.POST or None, request.FILES or None, instance=pergunta, prefix='pergunta')
        alternativa_form = form_alternativa_factory(request.POST or None, request.FILES or None, instance=pergunta,
                                                    prefix='alternativa')


        if form.is_valid() and alternativa_form.is_valid():
            form = form.save(commit=False)
            form.save()
            alternativa_form.save()

            return redirect('editais:edital_view',id =edital.id)
        else:
            context['edital'] = edital
            context['form'] = PerguntaForm(request.POST or None, request.FILES or None, instance=pergunta,
                                           prefix='pergunta')
            context['form_alternativa'] = form_alternativa_factory(request.POST or None, request.FILES or None,
                                                                   instance=pergunta, prefix='alternativa')

    else:
        context['edital'] = edital
        context['form'] = PerguntaForm(instance=pergunta, prefix='pergunta')
        context['form_alternativa'] = form_alternativa_factory(instance=pergunta, prefix='alternativa')

    return render(request, 'pergunta/add_pergunta.html', context)









#Inscrição área
class InscricaolList(ListView):
    template_name = 'inscricao/list_inscricao.html'
    model = Inscricao

def inscricao_view(request, id):
    context = {}
    inscricao= get_object_or_404(Inscricao, pk=id)

    context['inscricao'] = inscricao

    return render(request,'inscricao/view_inscricao.html',context)



