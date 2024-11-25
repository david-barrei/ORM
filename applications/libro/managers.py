from django.db import models
from django.db.models import Q

class LibroManager(models.Manager):

    def buscar_libro(self,kword):

        resultado = self.filter(titulo__icontains=kword)
        return resultado