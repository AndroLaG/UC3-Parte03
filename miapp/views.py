from django.shortcuts import render,HttpResponse


# Create your views here.
def saludo(request):
    mensaje ="""
        <h1>LENGUAJE DE PROGRAMACIÓN 3</h1>
        <ol class="list-group list-group-numbered">
  <li class="list-group-item">Hans Herrera Castillo</li>
  <li class="list-group-item">Emily Cañazaca Vasquez</li>
  <li class="list-group-item">Andres Sanchez Tucta</li>
    <li class="list-group-item">Flor Pizango Velezmoro</li>

</ol>
    """
    return HttpResponse(mensaje)