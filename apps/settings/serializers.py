from rest_framework import serializers
from .models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), write_only=True, source="author"
    )
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ["id", "title", "release_date", "author", "author_id"]

    def to_representation(self, instance):

        rep = super().to_representation(instance)
        rep["author_id"] = instance.author.id if instance.author else None
        return rep
