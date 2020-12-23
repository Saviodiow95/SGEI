from django.urls import path, include

from accounts.views import create_user_arquivo, perfil, list_users

app_name='accounts'

urlpatterns = [
    path('user/arquivo/', create_user_arquivo, name='create_user_arquivo'),
    path('user/perfil/', perfil, name='perfil_user'),
    path('user/list/', list_users, name='list_user'),
]
