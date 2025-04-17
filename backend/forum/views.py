from forum.models import Aluno, Curso, Reclamacao, Comentario
from forum.serializers import AlunoSerializer, CursoSerializer, ReclamacaoSerializer, ComentarioSerializer
from rest_framework import viewsets, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_filters = ['nome']

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class ReclamacaoViewSet(viewsets.ModelViewSet):
    queryset = Reclamacao.objects.all()
    serializer_class = ReclamacaoSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
