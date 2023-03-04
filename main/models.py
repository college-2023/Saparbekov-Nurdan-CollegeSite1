from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField('Название категории', max_length=255)
    image = models.ImageField('Изображение', upload_to='media/categories')
    slug = models.SlugField('Slug', max_length=255, unique=True)

    def __str__(self):
        return self.name


class Images(models.Model):
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    image = models.ImageField('Изображение инструмента', upload_to='media/instruments/')
    item = models.ForeignKey('Item', on_delete=models.DO_NOTHING, verbose_name='Инструмент', related_name='item_images')

    def __str__(self):
        return str(self.image)


class Company(models.Model):
    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    name = models.CharField("Название компании", max_length=255)
    slug = models.SlugField('Slug', max_length=255, unique=True)

    def __str__(self):
        return self.name


class Material(models.Model):
    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'

    name = models.CharField('Навзание материала', max_length=255)
    slug = models.SlugField('Slug', max_length=255)

    def __str__(self):
        return self.name


class Type(models.Model):
    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы инструментов'
    name = models.CharField('Название', max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    COLOR_CHOICES = (
        ('Белый', 'Белый'),
        ('Черный', 'Черный')
    )

    class Meta:
        verbose_name = 'Инструмент'
        verbose_name_plural = 'Инструменты'

    title = models.CharField('Название инструмента', max_length=255)
    slug = models.SlugField('Slug', unique=True, help_text='Данное поле заполняется автоматически')
    description = models.TextField('Описание/характеристика')
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, verbose_name='Компания')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='Категория')
    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING, verbose_name='Тип')
    colors = models.CharField('Цвет', choices=COLOR_CHOICES, max_length=255)
    material = models.ForeignKey(Material, on_delete=models.DO_NOTHING, verbose_name='Материал')
    size = models.FloatField("Размер")
    price = models.FloatField('Цена')

    def __str__(self):
        return self.title



