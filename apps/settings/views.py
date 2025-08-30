from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from .filters import BookFilter, AuthorFilter

import redis
import json


r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)



class DefaultPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 100



def cache_author(author: Author):
    author_data = {
        "id": author.id,
        "name": author.name,
        "birth_year": author.birth_year,
    }
    r.set(f"author:{author.id}", json.dumps(author_data))


def delete_author_from_cache(author_id: int):
    r.delete(f"author:{author_id}")


class AuthorCreateMixin:
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            author = self.get_queryset().last()
            cache_author(author)
        return response


class AuthorUpdateMixin:
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code in (status.HTTP_200_OK, status.HTTP_202_ACCEPTED):
            author = self.get_object()
            cache_author(author)
        return response


class AuthorDestroyMixin:
    def destroy(self, request, *args, **kwargs):
        author = self.get_object()
        response = super().destroy(request, *args, **kwargs)
        if response.status_code == status.HTTP_204_NO_CONTENT:
            delete_author_from_cache(author.id)
        return response


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter

    def create(self, request, *args, **kwargs):
        author_id = request.data.get("author_id")
        if not author_id:
            return Response({"error": "author_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            author = Author.objects.get(id=author_id)
        except Author.DoesNotExist:
            return Response({"error": "Author not found"}, status=status.HTTP_404_NOT_FOUND)

        cache_author(author)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=author)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AuthorViewSet(
    AuthorCreateMixin,
    AuthorUpdateMixin,
    AuthorDestroyMixin,
    viewsets.ModelViewSet
):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = AuthorFilter
