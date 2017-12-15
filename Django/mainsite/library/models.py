
from django.db import models
from django.utils import timezone



class Author(models.Model):
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.author


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    publish_date = models.CharField(max_length=200)

    def __str__(self):  # this controls how things are displayed in the admin panel
        return self.title

    # def __str__(self):
    #     return self.publish_date

class Checkout(models.Model):
    book = models.ForeignKey(Book)
    user = models.CharField(max_length=200)
    checkout = models.BooleanField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.book.__str__()

