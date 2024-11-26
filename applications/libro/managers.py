import datetime

from django.db import models
from django.db.models import Q, Count


class LibroManager(models.Manager):

    def buscar_libro(self,kword):

        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=("2020-01-05","2023-12-20")
        )
        return resultado


    def buscar_libro2(self,kword,fecha1, fecha2):
        date1 = datetime.datetime.strptime(fecha1,"%Y,%m,%d").date()
        date2 = datetime.datetime.strptime(fecha2,"%Y,%m,%d").date()

        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=(date1,date2)
        )
        return resultado
    
    def listar_libros_categoria(self, categoria):

        return self.filter(
            categoria__id = categoria
        ).order_by("titulo")
    
    def add_autor_libro(self, libro_id, autor):
        
        libro = self.get(id=libro_id)
        libro.autores.add(autor)
        return libro 

    def libros_num_prestamos(self):
        resultado = self.aggregate( # Devuelve un diccionario
            num_prestamos= Count('libro_prestamo')
        )

        return resultado
class CategoriaManager(models.Manager):

    def categoria_por_autor(self, autor):

        return self.filter(
            categoria_libro__autores__id=autor
        ).distinct()
    

    def listar_categoria_libros(self):#Conteo de cuantos libros tiene por categoria
        resultado = self.annotate(
            num_libros= Count('categoria_libro')
        )
        
        return resultado