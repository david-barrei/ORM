
from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):

    def buscar_autor(self,kword):

        resultado = self.filter(nombre__icontains=kword)
        return resultado

    def buscar_autor2(self,kword):

        resultado = self.filter(
            Q(nombre__icontains=kword) | Q(apellidos__icontains=kword)
            )

        return resultado

    def buscar_autor3(self,kword):

        resultado = self.filter(
            Q(nombre__icontains=kword) | Q(apellidos__icontains=kword)
            ).exclude(edad=25)

        return resultado

    def buscar_autor4(self,kword):

        resultado = self.filter( #Matoy o menor 
            edad__gt=30,
            edad__lt=65
        )
        return resultado





