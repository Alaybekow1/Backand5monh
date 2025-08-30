from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date


class Author(models.Model):
    name = models.CharField(max_length=155, verbose_name="Автор")
    birth_year = models.PositiveSmallIntegerField(
        verbose_name="Год рождения",
        validators=[MinValueValidator(1000), MaxValueValidator(date.today().year)]
    )

    def __str__(self):
        return f"{self.name} ({self.birth_year})"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Book(models.Model):
    title = models.CharField(max_length=155, verbose_name="Заголовок")
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books",
        verbose_name="Автор"
    )
    release_date = models.DateField(verbose_name="Дата выхода")

    def __str__(self):
        return f"{self.title} ({self.release_date.year}) - {self.author.name}"

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


