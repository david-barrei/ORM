from .models import Libro
from django.views.generic import ListView

class Listlibros(ListView):
    
    context_object_name = 'lista_libros'
    template_name = 'libro/lista.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','') 
        return Libro.objects.buscar_libro(palabra_clave)