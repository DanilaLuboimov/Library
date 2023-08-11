from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Book, Author, Category


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "isbn", "get_book_jacket",)
    list_filter = ("categories", "authors",)

    def get_book_jacket(self, object):
        if object.jacket:
            return mark_safe(f"<img src='{object.jacket.url}' width=150>")

    get_book_jacket.short_description = "обложка книги"


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "author",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category",)


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
