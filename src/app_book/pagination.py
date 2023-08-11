from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class SearchBookAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            "page": self.page.number,
            "next": self.get_next_link(),
            "previous": self.get_previous_link(),
            "total_page": self.page.paginator.num_pages,
            "count": self.page.paginator.count,
            "results": data,
        })