from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from store.models import CartItem, Cart
from store.serializers import CartItemSerializer


class CartItemCreateAPIView(generics.CreateAPIView):
    """Эндпоинт создания товаров в корзине"""
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        cart = Cart.objects.get(user=self.request.user)
        serializer.save(cart=cart)


class CartItemListAPIView(generics.ListCreateAPIView):
    """Эндпоинт просмотра всех товаров в корзине и добавления новых товаров"""
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)

    def perform_create(self, serializer):
        cart = Cart.objects.get(user=self.request.user)
        serializer.save(cart=cart)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = {
            'cart_items': serializer.data,
            'total_quantity': Cart.total_quantity_for_user(request.user),
            'total_cost': Cart.total_cost_for_user(request.user)
        }
        return Response(data)


class CartItemRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Эндпоинт просмотра, изменения и удаления товаров в корзине"""
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(cart__user=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.cart.user != self.request.user:
            return Response({"detail": "You don't have permission to delete this cart item."},
                            status=status.HTTP_403_FORBIDDEN)

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartItemUpdateAPIView(generics.UpdateAPIView):
    """Эндпоинт редактирования товаров в корзине"""
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

    def perform_update(self, serializer):
        serializer.save(cart__user=self.request.user)


class CartItemDestroyAPIView(generics.DestroyAPIView):
    """Эндпоинт удаления товаров в корзине"""
    queryset = CartItem.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.products.clear()
        instance.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.cart.user != self.request.user:
            return Response({"detail": "You don't have permission to delete this cart item."},
                            status=status.HTTP_403_FORBIDDEN)

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
