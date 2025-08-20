from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=155, verbose_name="Автор")
    birth_year = models.IntegerField(verbose_name="Год рождения")  # только год

    def __str__(self):
        return self.name

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
        return f"{self.title} - {self.author.name}"

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
