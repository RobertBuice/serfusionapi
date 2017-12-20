from rest_framework import pagination
from rest_framework.response import Response
from django.conf import settings


class LimitPagination(pagination.PageNumberPagination):

    def get_paginated_response(self, data):
        return Response({
            'per_page': settings.REST_FRAMEWORK['PAGE_SIZE'],
            'current_page': self.page.number,
            'last_page': self.page.paginator.num_pages,
            'next_page_url': self.get_next_link(),
            'prev_page_url': self.get_previous_link(),
            'from': data[0]['id'],
            'to': data[len(data) - 1]['id'],
            'total': self.page.paginator.count,
            'data': data
        })
