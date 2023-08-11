from django.urls import path

from .api_views import CategoriesSearchAPI, BookCatalogAPI, BookForDetailAPI


urlpatterns = [
    path("categories/", CategoriesSearchAPI.as_view(),
         name="api_categories"),
    path("catalog/", BookCatalogAPI.as_view(),
         name="api_catalog"),
    path("book_for_detail/<int:pk>/", BookForDetailAPI.as_view(),
         name="api_book_for_detail"),
]