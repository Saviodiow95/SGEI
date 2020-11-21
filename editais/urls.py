from django.urls import path, include

from .views import EditalListDetails, EditalList, edital_view, InscricaolList, edital_add, edital_delete, edital_edit, \
    inscricao_view, \
    pergunta_add, pergunta_edit, pergunta_delete

app_name='editais'
urlpatterns = [

    #----------------Edital-------------------
    path('', EditalListDetails.as_view(), name='edital_list'),
    path('view/edital/<int:id>', edital_view, name='edital_view'),
    path('add/edital/', edital_add, name="edital_add"),
    path('edit/edital/<int:id>', edital_edit, name="edital_edit"),
    path('delete/edital/<int:id>', edital_delete, name='edital_delete'),

    path('alunos/edital/list/', EditalList.as_view(), name='edital_list_inscri'),


    #----------------Pergunta-------------------
    path('add/pergunta/<int:id_edital>', pergunta_add, name="pergunta_add"),
    path('edit/pergunta/<int:id>', pergunta_edit, name="pergunta_edit"),
    path('delete/pergunta/<int:id>', pergunta_delete, name='pergunta_delete'),


    #----------------Incrições-------------------
    path('inscricao/', InscricaolList.as_view(), name='inscricao_list'),
    path('view/inscricao/<int:id>', inscricao_view, name='inscricao_view'),

]