from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    """Модель категории"""
    name = models.CharField(max_length=250, verbose_name='Наименование категории')
    slug_name = models.CharField(max_length=250, verbose_name='SLUG', **NULLABLE)
    image = models.ImageField(upload_to='category_images/', verbose_name='Изображение категории')

    def __str__(self):
        return f'{self.name}({self.slug_name})'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategory(models.Model):
    """Модель подкатегории"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories',
                                 verbose_name='Категория')

    name = models.CharField(max_length=250, verbose_name='Наименование подкатегории')
    slug_name = models.CharField(max_length=250, verbose_name='SLUG', **NULLABLE)
    image = models.ImageField(upload_to='subcategory_images/', verbose_name='Изображение подкатегории')

    def __str__(self):
        return f'{self.name}({self.slug_name})'

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Product(models.Model):
    """Модель продукта"""
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='product')
    name = models.CharField(max_length=250, verbose_name='Наименование продукта')
    slug_name = models.CharField(max_length=250, verbose_name='SLUG', **NULLABLE)

    image_small = models.ImageField(upload_to='product_images/small/', verbose_name='Изображение продукта(маленькое)')
    image_medium = models.ImageField(upload_to='product_images/meduim/', verbose_name='Изображение продукта(среднее)')
    image_large = models.ImageField(upload_to='product_images/large/', verbose_name='Изображение продукта(большое)')

    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена товара')

    def __str__(self):
        return f'{self.name}({self.slug_name}): {self.price} rub.'


class Cart(models.Model):
    """Модель для корзины пользователя"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Покупатель')
    products = models.ManyToManyField(Product, through='CartItem', verbose_name='Продукты')

    def __str__(self):
        return f"Cart for {self.user.username}"

    class Meta:
        verbose_name = 'Корзина пользователя'
        verbose_name_plural = 'Корзины пользователей'


class CartItem(models.Model):
    """Модель для товаров в корзине"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Корзина')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in {self.cart}"

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'
