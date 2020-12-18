from django.contrib.auth.hashers import make_password
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

# Create your views here.
from accounts.models import User


def create_user_arquivo(request):
    context = {}
    fs = FileSystemStorage()

    if (request.method == 'POST'):

        arq = request.FILES['arquivo']
        fs.save('accounts/'+arq.name, arq)
        #print(arq.read())
        dados = open('media/accounts/'+arq.name, 'r')

        for l in dados:

            aux = l.split()
            user = User()
            user.username = aux[0]
            user.email = aux[1]
            user.cpf = aux[2]
            user.password = make_password(aux[2])
            user.save()


    return render(request,'arquivos/cad.html',context)