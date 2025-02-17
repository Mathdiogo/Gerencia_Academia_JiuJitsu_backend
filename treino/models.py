from django.db import models

# Create your models here.

faixa_choices = (
        ('B', 'Branca'),
        ('A', 'Azul'),
        ('R', 'Roxa'),
        ('M', 'Marrom'),
        ('P', 'Preta'),
    )# colocamos aqui fora para as 2 classes terem acesso

class Alunos(models.Model): #PARA MAIORES DE 18 ANOS
    
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField(null=True, blank=True)
    faixa = models.CharField(max_length=1, choices=faixa_choices, default='B')


    def __str__(self):
        return self.nome
    
class Aulas_concluidas(models.Model):
    aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    faixa_atual = models.CharField(max_length=1, choices=faixa_choices, default='B')

    def __str__(self):
        return self.aluno.nome