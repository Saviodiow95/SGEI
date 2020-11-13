from django.urls import path, include

from .views import EditalList, edital_view, InscricaolList, edital_add, edital_delete

app_name='editais'
urlpatterns = [

    #----------------Edital-------------------
    path('', EditalList.as_view(), name='list_edital'),
    path('view/edital/<int:id>', edital_view, name='view_edital'),

    path('add/edital/', edital_add, name="edital_edital"),
    path('delete/edital/<int:id>', edital_delete, name='edital_delete'),

    path('inscricao/', InscricaolList.as_view(), name='list_inscricao'),

]