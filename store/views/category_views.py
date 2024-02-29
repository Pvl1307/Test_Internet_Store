from rest_framework import generics

from store.models import Category
from store.paginators import CategoryPaginator
from store.serializers import CategorySerializer


class CategoryCreateAPIView(generics.CreateAPIView):
    """Эндпоинт создания категории"""
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save()


class CategoryListAPIView(generics.ListAPIView):
    """Эндпоинт просмотра всех категорий"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = CategoryPaginator


class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    """Эндпоинт просмотра определенной категории"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryUpdateAPIView(generics.UpdateAPIView):
    """Эндпоинт редактирования категории"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def perform_update(self, serializer):
        serializer.save()


class CategoryDestroyAPIView(generics.DestroyAPIView):
    """Эндпоинт удаления категории"""
    queryset = Category.objects.all()
