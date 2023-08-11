from django.shortcuts import render
from django.views import View


class MainView(View):
    def get(self, request):
        return render(request, "main.html")

    def post(self, request):
        return self.get(request)


class Catalog(View):
    def get(self, request, *args, **kwargs):
        return render(request, "book/catalog.html")


class BookDetailView(View):
    def get(self, request, pk):
        return render(request, "book/detail_book.html")
