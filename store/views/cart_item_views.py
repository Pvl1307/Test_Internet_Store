from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from store.models import CartItem, Cart
from store.serializers import CartItemSerializer


class CartItemCreateAPIView(generics.CreateAPIView):
    """Эндпоинт создания товаров в корзине"""
    serializer_class = CartItemSerializer

    def perform_create(self, serializer):
        serializer.save(cart__user=self.request.user)


class CartItemListAPIView(generics.ListAPIView):
    """Эндпоинт просмотра всех товаров в корзине"""
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


class CartItemRetrieveAPIView(generics.RetrieveAPIView):
    """Эндпоинт просмотра определенных товаров в корзине"""
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()


class CartItemUpdateAPIView(generics.UpdateAPIView):
    """Эндпоинт редактирования товаров в корзине"""
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

    def perform_create(self, serializer):
        serializer.save(cart__user=self.request.user)


class CartItemDestroyAPIView(generics.DestroyAPIView):
    """Эндпоинт удаления товаров в корзине"""
    queryset = CartItem.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.products.clear()
        instance.save()
