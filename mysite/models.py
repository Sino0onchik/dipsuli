from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=123)
    image = models.ImageField(upload_to='images/category')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-created_at']


class Product(models.Model):
    title = models.CharField(max_length=123)
    mini_desc = models.CharField(max_length=250)
    description = models.TextField()
    article = models.CharField(max_length=123)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to='images/products/')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-price']


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    session_key = models.CharField(max_length=255)

    def total_price(self):
        return self.quantity * self.product.price


class Order(models.Model):
    items = models.ManyToManyField(CartItem, blank=True, null=True)
    fullname = models.CharField(max_length=123)
    address = models.CharField(max_length=123)
    phone = models.CharField(max_length=123)
    price = models.PositiveIntegerField(blank=True, default=0)
    status = models.CharField(max_length=123, choices=(
        ('Готово', 'Готово'),
        ('Не готово', 'Не готово'),
        ('Отменен', 'Отменен')), default='Не готово'
                              )
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order - {self.fullname}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']
