from django.urls import path

from .views import Catalog, BookDetailView


urlpatterns = [
    path("catalog/", Catalog.as_view(), name="categories"),
    path("<int:pk>/", BookDetailView.as_view(), name="detail_book"),
]