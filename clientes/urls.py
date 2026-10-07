<<<<<<< HEAD
# clientes/urls.py
"""URLs de la app clientes — W02."""
from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.index, name='inicio'),
    # Espiral 2 W05:
    # path('lista/',          views.ProductoListView.as_view(),   name='lista'),
    # path('nuevo/',          views.ProductoCreateView.as_view(), name='crear'),
    # path('<int:pk>/',       views.ProductoDetailView.as_view(), name='detalle'),
    # path('<int:pk>/editar/',views.ProductoUpdateView.as_view(), name='editar'),
]
=======
# productos/urls.py
"""URLs de la app productos — W01 (mínimo funcional)."""
from django.urls import path
from django.http import HttpResponse

app_name = 'productos'


def bienvenida_clientes(request):
    """Vista temporal de bienvenida para la app clientes."""
    return HttpResponse(
        "<h2>📦 Módulo Productos</h2>"
        "<p>En construcción — Espiral 2 (W04)</p>",
        content_type='text/html; charset=utf-8'
    )


urlpatterns = [
    path('', bienvenida_clientes, name='inicio'),
]
>>>>>>> 14b01055ae40f386e1d9803624f6a074c99e2c30
