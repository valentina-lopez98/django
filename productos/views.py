<<<<<<< HEAD
# productos/views.py
"""Vistas de la app productos — W02 (placeholder).

CRUD completo se implementa en Espiral 2 (W05-W06).
"""
from django.shortcuts import render


def index(request):
    """Vista de índice de productos.

    Returns:
        HttpResponse con template productos/index.html.
    """
    context = {
        'titulo': 'Productos',
        'descripcion': 'Gestión de inventario y catálogo de productos.',
        'espiral': 'Espiral 2 · W05',
    }
    return render(request, 'productos/index.html', context)
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 14b01055ae40f386e1d9803624f6a074c99e2c30
