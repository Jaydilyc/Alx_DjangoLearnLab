from django.db import models

# Create your models here.
# Author model stores the name of the author.
# One author can write multiple books.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model stores information about books written by authors.
# The ForeignKey creates a one-to-many relationship:
# One Author → Many Books.
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books"
    )

    def __str__(self):
        return self.title