from rest_framework.viewsets import ModelViewSet
from .models import Animal
from .serializers import AnimalSerializer


class AnimalViewSet(ModelViewSet):
    # ModelViewSet incluye las operaciones de consultar, crear, editar y eliminar.
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
