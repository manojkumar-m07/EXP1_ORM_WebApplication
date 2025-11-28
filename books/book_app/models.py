from django.db import models
from django.contrib import admin

# Create your models here.
class Book(models.Model):
    book_title = models.CharField(max_length=100, help_text="Enter Book Title")
    publication_date = models.DateField()
    isbn_number = models.IntegerField(help_text="Enter the ISBN Number")
    author_name = models.CharField(max_length=50, help_text="Enter Author Name")


class BookAdmin(admin.ModelAdmin):
    list_display = ['book_title', 'author_name', 'publication_date', 'isbn_number']