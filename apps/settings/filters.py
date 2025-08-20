import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")
    author = django_filters.CharFilter(field_name="author", lookup_expr="icontains")
    year = django_filters.NumberFilter(field_name="release_date", lookup_expr="year")
    year_gte = django_filters.NumberFilter(field_name="release_date", lookup_expr="year__gte")
    year_lte = django_filters.NumberFilter(field_name="release_date", lookup_expr="year__lte")

    class Meta:
        model = Book
        fields = ["title", "author", "year", "year_gte", "year_lte"]
