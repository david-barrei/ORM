import datetime

from django.db import models
from django.db.models import Q, Count, Avg,Sum


class PrestamoManager(models.Manager):

    def libros_promedio_edades(self):
        resultado = self.filter( 
            libro__id='5'
        ).aggregate(
            promedio_edad=Avg('lector__edad'),#Operaciones matematicas  promedio = Avg
            sum_edad= Sum('lector__edad')
        )
        return resultado

    def num_libros_prestados(self):
        resultado = self.values(
            'libro'
        ).annotate(
            num_prestamos= Count('libro')
        )

        for r in resultado:
            print('=========')
            print(r, r['num_prestamos'])

        return resultado