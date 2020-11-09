from django.contrib import admin
from .models   import Edital, Pergunta, Alternativa, Inscricao, Resposta

# Register your models here.
admin.site.register(Edital)
admin.site.register(Pergunta)
admin.site.register(Alternativa)
admin.site.register(Inscricao)
admin.site.register(Resposta)
