from rest_framework import serializers
from forum.models import Aluno, Curso, Reclamacao, Comentario


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'email', 'password', 'tipo_usuario', 'created_at']
    
    def validate_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError("O nome só pode conter letras!")
        return nome

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
