from django.db import models
from applications.autor.models import Autor
from .managers import LibroManager, CategoriaManager
# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return str(self.id) + "-" + self.nombre
    
    objects =  CategoriaManager()
    
class Libro(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE, related_name='categoria_libro')
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(max_length=30)
    fecha = models.DateField("Fecha de lanzaiento")
    portada = models.ImageField(upload_to="Portada")
    visitas = models.PositiveIntegerField()

    objects = LibroManager()

    class Meta:
        verbose_name = 'Libro'
        verbose_name_libros = 'Libro'

    def __str__(self):
        return str(self.id) + '-' + self.titulo


