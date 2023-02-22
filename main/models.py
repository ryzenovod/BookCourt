from django.db import models


class book(models.Model):
    title = models.CharField('Название', max_length=50)
    book = models.TextField('Описание')

    #image = models.ImageField('Изображение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
