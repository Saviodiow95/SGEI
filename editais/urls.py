from django.urls import path, include

from .views import EditalList, edital_view, InscricaolList, edital_add, edital_delete, edital_edit, inscricao_view, \
    pergunta_add

app_name='editais'
urlpatterns = [

    #----------------Edital-------------------
    path('', EditalList.as_view(), name='edital_list'),
    path('view/edital/<int:id>', edital_view, name='edital_view'),
    path('add/edital/', edital_add, name="edital_add"),
    path('edit/edital/<int:id>', edital_edit, name="edital_edit"),
    path('delete/edital/<int:id>', edital_delete, name='edital_delete'),

    #----------------Edital-------------------
    path('add/pergunta/<int:id_edital>', pergunta_add, name="pergunta_add"),



    #----------------Incrições-------------------
    path('inscricao/', InscricaolList.as_view(), name='inscricao_list'),
    path('view/inscricao/<int:id>', inscricao_view, name='inscricao_view'),

]