from rest_framework import generics

from store.models import Cart
from store.serializers import CartSerializer


class CartCreateAPIView(generics.CreateAPIView):
    """Эндпоинт создания корзины"""
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        serializer.save()


class CartListAPIView(generics.ListAPIView):
    """Эндпоинт просмотра всех корзин"""
    serializer_class = CartSerializer
    queryset = Cart.objects.all()


class CartRetrieveAPIView(generics.RetrieveAPIView):
    """Эндпоинт просмотра определенной корзины"""
    serializer_class = CartSerializer
    queryset = Cart.objects.all()


class CartUpdateAPIView(generics.UpdateAPIView):
    """Эндпоинт редактирования корзины"""
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

    def perform_update(self, serializer):
        updated_habit = serializer.save()
        updated_habit.owner = self.request.user
        updated_habit.save()


class CartDestroyAPIView(generics.DestroyAPIView):
    """Эндпоинт удаления корзины"""
    queryset = Cart.objects.all()
