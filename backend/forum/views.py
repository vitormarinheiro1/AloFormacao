from forum.models import Aluno, Curso, Reclamacao, Comentario
from forum.serializers import AlunoSerializer, CursoSerializer, ReclamacaoSerializer, ComentarioSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class ReclamacaoViewSet(viewsets.ModelViewSet):
    queryset = Reclamacao.objects.all()
    serializer_class = ReclamacaoSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
