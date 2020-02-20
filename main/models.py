from django.db import models

# Create your models here.
class Postagem(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=1000)
    data = models.DateTimeField(auto_now=True)
    autor = models.CharField(max_length=100)

    def __str__(self):
        return '%s %s' % (self.titulo, self.data)
