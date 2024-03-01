from rest_framework import generics

from store.models import SubCategory
from store.serializers import SubCategorySerializer


class SubCategoryCreateAPIView(generics.CreateAPIView):
    """Эндпоинт создания подкатегории"""
    serializer_class = SubCategorySerializer

    def perform_create(self, serializer):
        serializer.save()


class SubCategoryListAPIView(generics.ListAPIView):
    """Эндпоинт просмотра всех подкатегорий"""
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()


class SubCategoryRetrieveAPIView(generics.RetrieveAPIView):
    """Эндпоинт просмотра определенной подкатегории"""
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()


class SubCategoryUpdateAPIView(generics.UpdateAPIView):
    """Эндпоинт редактирования подкатегории"""
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()

    def perform_update(self, serializer):
        updated_habit = serializer.save()
        updated_habit.owner = self.request.user
        updated_habit.save()


class SubCategoryDestroyAPIView(generics.DestroyAPIView):
    """Эндпоинт удаления подкатегории"""
    queryset = SubCategory.objects.all()
