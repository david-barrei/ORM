from .models import Libro
from django.views.generic import ListView, DetailView

class Listlibros(ListView):
    
    context_object_name = 'lista_libros'
    template_name = 'libro/lista.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        #Fecha1 
        f1 = self.request.GET.get('fecha1','') 
        #Fecha2
        f2 = self.request.GET.get('fecha2','') 

        if f1 and f2:
            return Libro.objects.buscar_libro2(palabra_clave,f1,f2)
        else:
            return Libro.objects.buscar_libro(palabra_clave)
        
class Listlibros2(ListView):
    
    context_object_name = 'lista_libros'
    template_name = 'libro/lista2.html'

    def get_queryset(self):
        
        return Libro.objects.listar_libros_categoria('2')
    
class LibroDetailView(DetailView):
    model = Libro
    template_name = "libro/detalle.html"