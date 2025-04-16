from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, )
    password = models.CharField(max_length=100)
    TIPO_USUARIO = (
        ('AD', 'Admin'),
        ('AL', 'Aluno')
    )
    tipo_usuario = models.CharField(max_length=100, choices = TIPO_USUARIO, null = False, blank = False, default="AL")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    categoria = models.CharField(max_length=100)
    STATUS = (
        ('A', 'Ativo'),
        ('I', 'Inativo')
    )
    status = models.CharField(max_length=10, choices = STATUS, null = False, blank = False, default="A")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Reclamacao(models.Model):
    usuario_id = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso_id = models.ForeignKey(Curso, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    STATUS = (
        ('P', 'Pendente'),
        ('R', 'Resolvida')
    )
    status = models.CharField(max_length=10, choices = STATUS, null = False, blank = False, default="P")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    usuario_id = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    reclamacao_id = models.ForeignKey(Reclamacao, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comentario
