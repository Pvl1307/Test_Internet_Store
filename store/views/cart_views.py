from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from store.models import Cart
from store.serializers import CartSerializer


class CartCreateAPIView(generics.CreateAPIView):
    """Эндпоинт создания корзины"""
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartListAPIView(generics.ListAPIView):
    """Эндпоинт просмотра всех корзин"""
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = Cart.objects.filter(user=self.request.user)
        serializer = self.get_serializer(queryset, many=True)
        data = {
            'carts': serializer.data,
            'total_quantity': Cart.total_quantity_for_user(request.user),
            'total_cost': Cart.total_cost_for_user(request.user)
        }
        return Response(data)


class CartRetrieveAPIView(generics.RetrieveAPIView):
    """Эндпоинт просмотра определенной корзины"""
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


class CartUpdateAPIView(generics.UpdateAPIView):
    """Эндпоинт редактирования корзины"""
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        updated_cart = serializer.save()
        updated_cart.owner = self.request.user
        updated_cart.save()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        if instance.user != self.request.user:
            return Response({"detail": "You don't have permission to edit this cart."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class CartDestroyAPIView(generics.DestroyAPIView):
    """Эндпоинт удаления корзины"""
    queryset = Cart.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.products.clear()
        instance.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.user != self.request.user:
            return Response({"detail": "You don't have permission to delete this cart."},
                            status=status.HTTP_403_FORBIDDEN)

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
