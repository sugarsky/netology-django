from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    tags = models.ManyToManyField('Tag', through='Scope', verbose_name='Теги')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at',]

    def __str__(self):
        return self.title


class Tag(models.Model):

    name = models.CharField(max_length=64, verbose_name='Название')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name

class Scope(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья', related_name='Scope')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Тег', related_name='Scope')
    is_main = models.BooleanField(default=False, verbose_name='Основной')

    class Meta:
        ordering = ['-is_main', 'article']