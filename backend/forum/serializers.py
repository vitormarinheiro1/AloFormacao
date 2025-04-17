from rest_framework import serializers
from forum.models import Aluno, Curso, Reclamacao, Comentario
from forum.validators import nome_invalido


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'email', 'password', 'tipo_usuario', 'created_at']
    
    def validate(self, dados):
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({"nome": "O nome só pode conter letras!"})
        return dados

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class ReclamacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reclamacao
        fields = '__all__'


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'
