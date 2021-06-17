from django.contrib import admin
from .models import Aluno

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)


# Register your models here.
admin.site.register(Aluno, Alunos)
