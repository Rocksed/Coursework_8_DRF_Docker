from rest_framework.pagination import PageNumberPagination


class MyPagination(PageNumberPagination):
    page_size = 5  # Количество элементов на странице