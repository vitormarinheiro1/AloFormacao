from forum.models import Aluno, Curso, Reclamacao, Comentario
from forum.serializers import AlunoSerializer, CursoSerializer, ReclamacaoSerializer, ComentarioSerializer
from rest_framework import viewsets, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all().order_by("id")
    serializer_class = AlunoSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_filters = ['nome']
    search_fields = ['nome', 'email']


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by("id")
    serializer_class = CursoSerializer


class ReclamacaoViewSet(viewsets.ModelViewSet):
    queryset = Reclamacao.objects.all().order_by("id")
    serializer_class = ReclamacaoSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all().order_by("id")
    serializer_class = ComentarioSerializer
