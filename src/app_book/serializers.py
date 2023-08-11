from rest_framework import serializers

from .models import Category, Book, Author


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategoriesForBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("category",)


class AuthorsForBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("author",)


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorsForBookSerializer(read_only=True, many=True)
    categories = CategoriesForBookSerializer(read_only=True, many=True)

    class Meta:
        model = Book
        fields = ("id", "title", "isbn", "page_count", "published_date",
                  "jacket", "short_description", "long_description", "status",
                  "authors", "categories", )
