from rest_framework import viewsets

# from djoser.views import UserViewSet
from .models import Cat, Owner
from .serializers import CatSerializer, OwnerSerializer, CatListSerializer
# from .serializers import CustomUserSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    def get_serializer_class(self):
        # Если запрошенное действие(action) — 
        # получение списка объектов('list')
        if self.action == 'list':
            # ...то применяем CatListSerializer
            return CatListSerializer
        # А если запрошенное действие — не 'list', применяем CatSerializer
        return CatSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


# class CustomUserViewSet(UserViewSet):
#     ...
