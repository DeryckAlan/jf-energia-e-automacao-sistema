from django.db import models
from Projeto.models import Projeto, Painel

# Create your models here.
class QRcode(models.Model):
    id = models.IntegerField(primary_key = True, auto_created=True)
    nome = models.CharField(max_length = 200)
    link = models.TextField()
    
    #foreign key para paineis e projetos
    projeto_nome = models.ForeignKey(Projeto, on_delete=models.PROTECT ,null=True)
    painel_nome = models.ForeignKey(Painel,  on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return self.nome
    