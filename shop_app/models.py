from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class CategoryModel(models.Model):
    """Модель категории товаров"""
    name = models.CharField('Наименование', max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop_app:product_list_by_category', args=[self.slug])


class ProductModel(models.Model):
    """Модель каталога товаров"""
    SHIRT_SIZES = (
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    COLOUR = (
        ('Белый', 'Белый'),
        ('Черный', 'Черный'),
        ('Бежевый', 'Бежевый'),
    )
    category = models.ForeignKey(CategoryModel, related_name='products', on_delete=models.CASCADE)
    name = models.CharField('Наименование', max_length=50, db_index=True)
    slug = models.SlugField('URL', max_length=50, db_index=True)
    image = models.ImageField('Изображение', upload_to='products/', blank=True)
    description = models.TextField('Описание', blank=True)
    summary = models.TextField('Краткое описание', blank=True)
    specific = models.TextField('Характеристики', max_length=200, blank=True)
    size = models.CharField('Размер', max_length=2, choices=SHIRT_SIZES, blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField('Запас')
    available = models.BooleanField('Наличие', default=True)
    colour = models.CharField('Цвет', max_length=20, choices=COLOUR, blank=True)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop_app:products', args=[self.id, self.slug])


class FeedBackModel(models.Model):
    """Модель обратной связи"""
    name = models.CharField('Имя', max_length=30)
    email = models.EmailField('E-mail')
    subject = models.CharField('Тема', max_length=15)
    message = models.TextField('Сообщение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратные связи'


class UserDressModel(AbstractUser):
    """Модель Пользователя"""
    GENDER = (
        ('муж', 'муж'),
        ('жен', 'жен')
    )
    name = models.CharField('Имя', max_length=30)
    middle_name = models.CharField('Второе имя', blank=True, null=True, max_length=20)
    first_login = models.DateTimeField(null=True)
    phone = models.CharField('Номер телефона', max_length=15)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)
    bio = models.TextField('О себе', blank=True, null=True)
    social = models.CharField('Соц. сеть', max_length=200, blank=True, null=True)
    birthday = models.DateField('День рождения', blank=True, null=True)
    gender = models.CharField('Пол', max_length=6, choices=GENDER, default='')


class Basket(models.Model):
    """Модель корзины"""
    user = models.ForeignKey(UserDressModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'Корзина пользователя {self.user.name} | Продукт {self.product.name}'

    def sum(self):  # Общая сумма товаров (одного наименования)
        return self.quantity * self.product.price

    def total_quantity(self):  # Общее количество товаров в корзине!
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.quantity for basket in baskets)

    def total_sum(self):  # Общая сумма товаров в корзине!
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.sum() for basket in baskets)


class AboutModel(models.Model):
    """Модель О нас (о бренде)"""
    heading = models.CharField('Заголовок', max_length=20, db_index=True)
    description = models.TextField('Содержание', blank=True)
    image = models.ImageField('Изображение', upload_to='products/about/', blank=True)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
