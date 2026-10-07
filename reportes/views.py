<<<<<<< HEAD
# reportes/views.py
"""Vistas de la app reportes — W02 (placeholder)."""
from django.shortcuts import render


def index(request):
    """Vista de índice de reportes."""
    context = {
        'titulo': 'Reportes',
        'descripcion': 'Dashboard, KPIs y exportación de datos.',
        'espiral': 'Espiral 7 · W19',
    }
    return render(request, 'reportes/index.html', context)
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 14b01055ae40f386e1d9803624f6a074c99e2c30
