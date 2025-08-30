import django_filters
from .models import Book, Author


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")
    author = django_filters.CharFilter(field_name="author__name", lookup_expr="icontains")
    year = django_filters.NumberFilter(field_name="release_date", lookup_expr="year")
    year_gte = django_filters.NumberFilter(field_name="release_date", lookup_expr="year__gte")
    year_lte = django_filters.NumberFilter(field_name="release_date", lookup_expr="year__lte")

    class Meta:
        model = Book
        fields = ["title", "author", "year", "year_gte", "year_lte"]


class AuthorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")
    birth_year = django_filters.NumberFilter(field_name="birth_year")
    birth_year_gte = django_filters.NumberFilter(field_name="birth_year", lookup_expr="gte")
    birth_year_lte = django_filters.NumberFilter(field_name="birth_year", lookup_expr="lte")

    class Meta:
        model = Author
        fields = ["name", "birth_year", "birth_year_gte", "birth_year_lte"]
