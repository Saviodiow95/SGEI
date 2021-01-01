from django.contrib.auth.hashers import make_password
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

# Create your views here.
from accounts.models import User


def perfil(request):
    context ={}
    user = request.user

    context['user'] = user
    return render(request,'user/perfil.html', context)

def create_user_arquivo(request):
    context = {}
    fs = FileSystemStorage()

    if (request.method == 'POST'):

        arq = request.FILES['arquivo']


        fs.save('accounts/' + arq.name, arq)

        caminho = 'media/accounts/' + arq.name


        dados = open(caminho, 'r')

        for l in dados:
            aux = l.split()
            user = User()
            user.username = aux[0]
            user.email = aux[1]
            user.cpf = aux[2]
            user.password = make_password(aux[2])
            user.save()

        dados.close()
        import os
        from SGEI.settings import BASE_DIR

        os.remove(BASE_DIR / caminho)

        return redirect('accounts:list_user')

    return render(request,'arquivos/cad.html',context)




def list_users(request):
    context={}

    users = User.objects.filter(is_staff=False)

    context['list_user'] = users

    return render(request,'user/list_user.html',context)