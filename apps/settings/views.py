from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        author_id = request.data.get('author_id')
        if not author_id:
            return Response({"error": "author_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            author = Author.objects.get(id=author_id)
        except Author.DoesNotExist:
            return Response({"error": "Author not found"}, status=status.HTTP_404_NOT_FOUND)

        author_data = {"id": author.id, "name": author.name, "birth_year": author.birth_year}
        r.set(f"author:{author.id}", json.dumps(author_data))

        book = Book.objects.create(
            title=request.data.get('title'),
            release_date=request.data.get('release_date'),
            author=author
        )
        serializer = self.get_serializer(book)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
