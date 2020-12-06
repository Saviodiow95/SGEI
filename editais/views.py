from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView


from .forms import EditalForm, PerguntaForm, AlternativaForm
from .models import Edital, Inscricao, Pergunta, Alternativa, Resposta


#Edital área

# administração
class EditalListAdm(ListView):
    template_name = 'edital/list_edital.html'
    model = Edital


def edital_view_adm(request, id):
    context = {}
    edital= get_object_or_404(Edital, pk=id)
    perguntas = edital.pergunta_set.all()
    context['edital'] = edital
    context['perguntas'] = perguntas
    return render(request,'edital/view_edital.html',context)

def edital_add(request):
    edital = Edital()
    context = {}

    if request.method == 'POST':
        form = EditalForm(request.POST or None, request.FILES or None, instance=edital, prefix='edital')

        if form.is_valid():
            form = form.save(commit=False)

            edital = form.save()

            return redirect('editais:edital_list')
        else:
            context['form'] = EditalForm(request.POST or None, request.FILES or None, instance=edital, prefix='edital')


    else:
        context['form'] = EditalForm( instance=edital, prefix='edital')



    return render(request,'edital/add_edital.html', context)


def  edital_edit(request, id):
    context = {}
    edital = get_object_or_404(Edital, pk=id)

    if request.method == 'POST':
        form = EditalForm(request.POST or None, request.FILES or None, instance=edital, prefix='edital')



        if form.is_valid():
            form = form.save(commit=False)
            form.save()


            return redirect('editais:edital_view', id=edital.id)
        else:
            context['form'] = EditalForm(request.POST or None, request.FILES or None, instance=edital, prefix='edital')


    else:
        context['form'] = EditalForm(instance=edital, prefix='edital')



    return render(request,'edital/add_edital.html', context)



def edital_delete(request, id):
    edital = get_object_or_404(Edital, pk=id)
    edital.delete()

    return redirect('editais:edital_list')


###Alunos
class EditalList(ListView):
    template_name = 'edital/list_edital_inscri.html'
    model = Edital

def edital_view(request, id):
    context = {}
    edital= get_object_or_404(Edital, pk=id)
    context['edital'] = edital
    return render(request,'edital/view_edital_inscri.html',context)







#------------------- Perguntas ---------------------

def pergunta_add(request, id_edital):
    form_alternativa_factory = inlineformset_factory(Pergunta, Alternativa, form=AlternativaForm)

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


def pergunta_edit(request, id):
    form_alternativa_factory = inlineformset_factory(Pergunta, Alternativa, form=AlternativaForm)
    pergunta = get_object_or_404(Pergunta, pk=id)
    edital = pergunta.edital

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

    return render(request, 'pergunta/edit_pergunta.html', context)


def pergunta_delete(request, id):
    pergunta = get_object_or_404(Pergunta, pk=id)
    edital = pergunta.edital
    pergunta.delete()

    return redirect('editais:edital_view',id =edital.id)





#Inscrição área
class InscricaolList(ListView):
    template_name = 'inscricao/list_inscricao.html'
    model = Inscricao

def inscricao_view(request, id):
    context = {}
    inscricao= get_object_or_404(Inscricao, pk=id)

    context['inscricao'] = inscricao

    return render(request,'inscricao/view_inscricao.html',context)


def inscricao_do(request,id_edital):

    context = {}
    respostas = {}
    edital = get_object_or_404(Edital, pk=id_edital)
    context['edital'] = edital
    inscricao = Inscricao()
    inscricao.edital = edital
    inscricao.user = request.user
    if(request.method == 'POST'):


        inscricao.save()
        for pergunta in edital.pergunta_set.all():
            aux = request.POST.get('pergunta-' + str(pergunta.id))
            resp = Resposta(inscricao=inscricao)

            if pergunta.is_aberta:
                resp.resposta_aberta = aux
            else:
                alt = Alternativa.objects.get(id=int(aux))
                resp.alternativa = alt

            if pergunta.has_arquivo:

                arq = request.FILE.get('arquivo-' + str(pergunta.id))
                resp.arquivo = arq

            #resp.save()


    return render(request, 'inscricao/do_inscricao.html', context)

