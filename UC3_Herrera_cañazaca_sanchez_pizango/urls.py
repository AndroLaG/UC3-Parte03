from django.contrib import admin
from django.urls import path
from miapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),
    path('inicio/', views.index, name = "inicio"),
    path('saludo/',views.saludo, name = "saludo"),
    path('rango/',views.primos_entre_a_y_b,name="rango"),


]
 
