from django.db import models

# Create your models here.


class Book(models.Model):
    book_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    price = models.FloatField()
    shelf = models.CharField(max_length=202)
    borrowed_by = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.book_name} by {self.author_name}"
