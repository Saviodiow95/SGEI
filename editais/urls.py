from django.urls import path, include

from .views import EditalList, InscricaolList

app_name='editais'
urlpatterns = [
    path('', EditalList.as_view(), name="list_edital"),
    path('inscricao/', InscricaolList.as_view(), name="list_inscricao"),
]