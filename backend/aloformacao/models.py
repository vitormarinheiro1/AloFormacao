from django.db import models


class Usuarios(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30)
    password = models.CharField(max_length=100)
    tipo_usuario = models.CharField(max_length=20)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField()
    categoria = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='ativo')
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name


class Reclamacoes(models.Model):
    pass


class Comentarios(models.Model):
    pass
