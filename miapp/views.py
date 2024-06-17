from django.shortcuts import render,HttpResponse


def index(request):
    mensaje="""
        <h1>Inicio</h1>
    """
    return HttpResponse(mensaje)


def saludo(request):
    mensaje ="""
        <h1>Bienvenidos al curso</h1>
        <h2>Mg. Flor Elizabeth Cerdán León</h2>
        <h3>Todo lo puedo en Cristo que me fortalece</h3>
    """
    return HttpResponse(layout + mensaje)




def primos_entre_a_y_b(a, b):
    if a > b:
        a, b = b, a

    def es_primo(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    primos = [num for num in range(a, b + 1) if es_primo(num)]
    return primos

# Valores de prueba
a = 1
b = 20
print(primos_entre_a_y_b(a, b))

