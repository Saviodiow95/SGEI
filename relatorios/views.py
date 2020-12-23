from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .utils import Render 
from editais.models import Edital,Inscricao




def relatorioedital(request,id):
    
    context={}
    edital = get_object_or_404(Edital, pk=id)
    context['edital']=edital

    return Render.render('relatorio/inscricoes/inscricoes_edital.html', context)

def pdf_inscricaoDetelhada(request,id):

    context = {}
    inscricao= get_object_or_404(Inscricao, pk=id)

    context['inscricao'] = inscricao

    return Render.render('relatorio/aluno/aluno_inscri.html', context)


   
