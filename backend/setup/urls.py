from django.contrib import admin
from django.urls import path, include
from forum.views import AlunoViewSet, CursoViewSet, ReclamacaoViewSet, ComentarioViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunoViewSet, basename='Alunos')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('reclamacao', ReclamacaoViewSet, basename='Reclamacao')
router.register('comentario', ComentarioViewSet, basename='Comentario')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
