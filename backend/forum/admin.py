from django.contrib import admin
from forum.models import Aluno, Curso, Reclamacao, Comentario


class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'password', 'tipo_usuario', 'created_at')
    list_display_links = ('id', 'nome')
    list_per_page = 20
    search_fields = ('nome', 'email')

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)

admin.site.register(Curso, Cursos)

class Reclamacoes(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)

admin.site.register(Reclamacao, Reclamacoes)

class Comentarios(admin.ModelAdmin):
    list_display = ('id', 'comentario')
    list_display_links = ('id', 'comentario')
    search_fields = ('comentario',)

admin.site.register(Comentario, Comentarios)
