from django.urls import path, include

from accounts.views import create_user_arquivo

app_name='accounts'

urlpatterns = [
    path('user/arquivo/', create_user_arquivo, name='create_user_arquivo'),
]
