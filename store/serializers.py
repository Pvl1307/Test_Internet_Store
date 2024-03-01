from pytils.translit import slugify
from rest_framework import serializers

from store.models import Category, SubCategory, Product, CartItem, Cart


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('id', 'category', 'name', 'slug_name', 'image')

    def create(self, validated_data):
        validated_data['slug_name'] = slugify(validated_data['name'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.slug_name = slugify(instance.name)
        instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug_name', 'image', 'subcategories')

    def create(self, validated_data):
        validated_data['slug_name'] = slugify(validated_data['name'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.slug_name = slugify(instance.name)
        instance.save()
        return instance


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'subcategory', 'name', 'slug_name', 'image_small', 'image_medium', 'image_large', 'price')

    def create(self, validated_data):
        validated_data['slug_name'] = slugify(validated_data['name'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.slug_name = slugify(instance.name)
        instance.save()
        return instance


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('id', 'product', 'cart', 'quantity')


class CartSerializer(serializers.ModelSerializer):
    products = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'user', 'products')
