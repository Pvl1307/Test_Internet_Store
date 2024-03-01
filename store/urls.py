from django.urls import path

from store.apps import StoreConfig
from store.views.cart_item_views import CartItemCreateAPIView, CartItemListAPIView, CartItemRetrieveAPIView, \
    CartItemUpdateAPIView, CartItemDestroyAPIView
from store.views.cart_views import CartCreateAPIView, CartListAPIView, CartRetrieveAPIView, CartUpdateAPIView, \
    CartDestroyAPIView
from store.views.category_views import CategoryCreateAPIView, CategoryListAPIView, CategoryRetrieveAPIView, \
    CategoryUpdateAPIView, CategoryDestroyAPIView
from store.views.product_views import ProductCreateAPIView, ProductListAPIView, ProductRetrieveAPIView, \
    ProductUpdateAPIView, ProductDestroyAPIView
from store.views.subcategory_views import SubCategoryCreateAPIView, SubCategoryListAPIView, \
    SubCategoryRetrieveAPIView, SubCategoryUpdateAPIView, SubCategoryDestroyAPIView

app_name = StoreConfig.name

urlpatterns = [
    path('category/create/', CategoryCreateAPIView.as_view(), name='category_create'),
    path('category/list/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/retrieve/<int:pk>/', CategoryRetrieveAPIView.as_view(), name='category_retrieve'),
    path('category/update/<int:pk>/', CategoryUpdateAPIView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDestroyAPIView.as_view(), name='category_delete'),

    path('subcategory/create/', SubCategoryCreateAPIView.as_view(), name='subcategory_create'),
    path('subcategory/list/', SubCategoryListAPIView.as_view(), name='subcategory_list'),
    path('subcategory/retrieve/<int:pk>/', SubCategoryRetrieveAPIView.as_view(), name='subcategory_retrieve'),
    path('subcategory/update/<int:pk>/', SubCategoryUpdateAPIView.as_view(), name='subcategory_update'),
    path('subcategory/delete/<int:pk>/', SubCategoryDestroyAPIView.as_view(), name='subcategory_delete'),

    path('product/create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('product/list/', ProductListAPIView.as_view(), name='product_list'),
    path('product/retrieve/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product_retrieve'),
    path('product/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDestroyAPIView.as_view(), name='product_delete'),

    path('cart/create/', CartCreateAPIView.as_view(), name='cart_create'),
    path('cart/list/', CartListAPIView.as_view(), name='cart_list'),
    path('cart/retrieve/<int:pk>/', CartRetrieveAPIView.as_view(), name='cart_retrieve'),
    path('cart/update/<int:pk>/', CartUpdateAPIView.as_view(), name='cart_update'),
    path('cart/delete/<int:pk>/', CartDestroyAPIView.as_view(), name='cart_delete'),

    path('cart_item/create/', CartItemCreateAPIView.as_view(), name='cart_item_create'),
    path('cart_item/list/', CartItemListAPIView.as_view(), name='cart_item_list'),
    path('cart_item/retrieve/<int:pk>/', CartItemRetrieveAPIView.as_view(), name='cart_item_retrieve'),
    path('cart_item/update/<int:pk>/', CartItemUpdateAPIView.as_view(), name='cart_item_update'),
    path('cart_item/delete/<int:pk>/', CartItemDestroyAPIView.as_view(), name='cart_item_delete'),
]
