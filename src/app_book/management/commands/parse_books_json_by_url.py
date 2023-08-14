import json
import os
import sys

from datetime import datetime

from django.core.files import File
from django.core.management import BaseCommand

from app_book.models import Book, Author, Category
from utils.management.download_file import download_file
from utils.management.download_image import download_image


class Command(BaseCommand):
    help = "Парсинг json-файла для заполнения базы данных..."

    def add_arguments(self, file_url):
        file_url.add_argument("file_url", type=str)

    def handle(self, *args, **options):
        toolbar_width = 50

        sys.stdout.write(f"Processing... │{' ' * toolbar_width}│")
        sys.stdout.flush()
        sys.stdout.write(
            "\b" * (toolbar_width + 1))

        file_url = options.get("file_url")

        file_path = download_file(file_url, "books.json")

        category_is_new: Category = Category.objects.filter(
            category="New"
        ).first()

        if not category_is_new:
            category_is_new = Category.objects.create(
                category="New"
            )

        with open(file_path, "r") as file:
            books = json.load(file)

        progress = len(books)
        last_point = 0

        for book, counter in zip(books, range(progress)):
            isbn = book.get("isbn")

            if not isbn:
                continue

            if Book.objects.filter(isbn=isbn):
                last_point = self.progress_bar(counter, progress, last_point)
                continue

            authors: list = self.get_or_create_authors(book["authors"])
            categories: list = book["categories"]

            if len(categories) == 0:
                categories.append(category_is_new.id)
            else:
                categories: list = self.get_or_create_categories(categories)

            date = book.get("publishedDate")

            if date:
                date = datetime.strptime(date["$date"].split("T")[0], "%Y-%m-%d")

            instance = Book.objects.create(
                title=book.get("title"),
                isbn=book.get("isbn"),
                page_count=book.get("pageCount"),
                published_date=date,
                short_description=book.get("shortDescription"),
                long_description=book.get("longDescription"),
                status=book.get("status"),
            )
            instance.authors.set(authors)
            instance.categories.set(categories)

            if book.get("thumbnailUrl") is not None:
                book_jacket = download_image(
                    book.get("thumbnailUrl"),
                    "../../../media/book_jacket",
                    instance.id,
                )

                if book_jacket is not None:
                    with open(book_jacket, mode="rb") as f:
                        instance.jacket = File(f, name=book_jacket)
                        instance.save()
                        os.remove(book_jacket)

            last_point = self.progress_bar(counter, progress, last_point)

        sys.stdout.write("░│\n")
        sys.stdout.write("Parsing completed!\n")

    @staticmethod
    def get_or_create_authors(authors: list) -> list:
        res_authors = list()

        for name in authors:
            if len(name.strip()) < 1:
                continue

            author: Author = Author.objects.filter(author=name).first()

            if author is None:
                author: Author = Author.objects.create(author=name)

            res_authors.append(author.id)

        return res_authors

    @staticmethod
    def get_or_create_categories(categories: list) -> list:
        res_categories = list()

        for name in categories:
            if len(name.strip()) < 1:
                continue

            category: Category = Category.objects.filter(
                category__icontains=name
            ).first()

            if category is None:
                category: Category = Category.objects.create(
                    category=name
                )

            res_categories.append(category.id)

        return res_categories

    @staticmethod
    def progress_bar(counter: int, progress: int, last_point: int) -> int:
        checkpoint = round(counter / progress, 2) * 100

        if (checkpoint % 2 == 0 and checkpoint != last_point) \
                or last_point == 0:
            last_point = checkpoint
            sys.stdout.write("░")
            sys.stdout.flush()

        return last_point
