from rest_framework import serializers
from forum.models import Aluno, Curso, Reclamacao, Comentario

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'email', 'password', 'tipo_usuario', 'created_at']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nome', 'descricao']

class ReclamacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reclamacao
        fields = ['id', 'titulo', 'descricao']

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id', 'comentario']
