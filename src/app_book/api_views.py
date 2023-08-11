from django.db.models import Q, Prefetch
from rest_framework import generics
from rest_framework.response import Response

from .models import Category, Book, Author
from .pagination import SearchBookAPIListPagination
from .serializers import CategoriesSerializer, BookSerializer


class CategoriesSearchAPI(generics.ListAPIView):
    serializer_class = CategoriesSerializer
    queryset = Category.objects.all()


class BookCatalogAPI(generics.ListAPIView):
    serializer_class = BookSerializer
    pagination_class = SearchBookAPIListPagination

    def get_queryset(self):
        title = self.request.query_params.get("title")
        author = self.request.query_params.get("author")
        status = self.request.query_params.get("status")
        category = [self.request.query_params.get("category")]

        filters_book = dict()

        if title:
            filters_book["title"] = (Q(title__icontains=title))
        if author:
            filters_book["author"] = (Q(authors__author__icontains=author))
        if status:
            filters_book["status"] = (Q(status=status))
        if None not in category:
            filters_book["category"] = (Q(categories__category__in=category))

        query = Book.objects.prefetch_related(
            Prefetch("authors", queryset=Author.objects.all()),
            Prefetch("categories", queryset=Category.objects.all()),
        ).filter(*filters_book.values()).distinct()

        return query


class BookForDetailAPI(generics.RetrieveAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        pass

    def retrieve(self, request, *args, **kwargs):
        query = Book.objects.prefetch_related(
            Prefetch("authors", queryset=Author.objects.all()),
            Prefetch("categories", queryset=Category.objects.all()),
        ).get(id=self.kwargs["pk"])

        queryset = BookSerializer(query)
        return Response(queryset.data)

