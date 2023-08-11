from django.db import models

from utils.models import path_and_rename


class Book(models.Model):
    class Status(models.TextChoices):
        MEAP = "MEAP", "MEAP"
        PUBLISH = "PUBLISH", "PUBLISH"

    title = models.CharField(max_length=500, verbose_name="название")
    isbn = models.CharField(
        max_length=13,
        unique=True,
        verbose_name="isbn"
    )
    page_count = models.PositiveIntegerField()
    published_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата публикации",
    )
    jacket = models.ImageField(
        upload_to=path_and_rename("book_jacket/")
    )
    short_description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Краткое описание",
    )
    long_description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание",
    )
    status = models.CharField(
        max_length=7,
        choices=Status.choices,
        default=Status.MEAP,
    )
    authors = models.ManyToManyField(
        "app_book.Author",
        verbose_name="Авторы",
    )
    categories = models.ManyToManyField(
        "app_book.Category",
        verbose_name="Категории",
    )

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        db_table = "books"

    def __str__(self):
        return self.title


class Author(models.Model):
    author = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Автор",
    )

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        db_table = "authors"

    def __str__(self):
        return self.author


class Category(models.Model):
    category = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Категория",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        db_table = "categories"

    def __str__(self):
        return self.category
