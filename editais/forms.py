from django import  forms
from .models import Pergunta, Edital, Alternativa, Resposta, Inscricao


class EditalForm(forms.ModelForm):
    class Meta:
        model = Edital

class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao


class PerguntaForm(forms.ModelForm):
    class Meta:
        model = Pergunta

class AlternativaForm(forms.ModelForm):
    class Meta:
        model = Alternativa

class RespostaForm(forms.ModelForm):
    class Meta:
        model = Resposta

