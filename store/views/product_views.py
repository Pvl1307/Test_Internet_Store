from rest_framework import generics

from store.models import Product
from store.paginators import ProductPaginator
from store.serializers import ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    """Эндпоинт создания продукта"""
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save()


class ProductListAPIView(generics.ListAPIView):
    """Эндпоинт просмотра всех продуктов"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = ProductPaginator


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """Эндпоинт просмотра определенного продукта"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductUpdateAPIView(generics.UpdateAPIView):
    """Эндпоинт редактирования продукта"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def perform_update(self, serializer):
        serializer.save()


class ProductDestroyAPIView(generics.DestroyAPIView):
    """Эндпоинт удаления продукта"""
    queryset = Product.objects.all()
