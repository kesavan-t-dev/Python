from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        db_column='author'  
    )
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

