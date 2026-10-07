<<<<<<< HEAD
# clientes/views.py
"""Vistas de la app clientes — W02 (placeholder)."""
from django.shortcuts import render


def index(request):
    """Vista de índice de clientes."""
    context = {
        'titulo': 'Clientes',
        'descripcion': 'Gestión de cartera de clientes.',
        'espiral': 'Espiral 2 · W04',
    }
    return render(request, 'clientes/index.html', context)
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 14b01055ae40f386e1d9803624f6a074c99e2c30
