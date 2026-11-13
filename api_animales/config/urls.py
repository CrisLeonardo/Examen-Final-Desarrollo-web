from django.urls import include, path
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from animales.views import AnimalViewSet

# El router crea las rutas para listar, guardar y consultar por identificador.
router = DefaultRouter()
router.register('animales', AnimalViewSet, basename='animal')

urlpatterns = [
    path('', RedirectView.as_view(url='/api/animales/', permanent=False), name='inicio'),
    path('api/', include(router.urls)),
]
