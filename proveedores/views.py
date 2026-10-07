<<<<<<< HEAD
# proveedores/views.py
"""Vistas de la app proveedores — W02 (placeholder)."""
from django.shortcuts import render


def index(request):
    """Vista de índice de proveedores."""
    context = {
        'titulo': 'Proveedores',
        'descripcion': 'Red de proveedores de mercancía.',
        'espiral': 'Espiral 2 · W04',
    }
    return render(request, 'proveedores/index.html', context)
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 14b01055ae40f386e1d9803624f6a074c99e2c30
