from django.db import models
import uuid #for unique book instances
from django.urls import reverse #Generate detail URLS

# Create your models here.
class Genre(models.Model):
    """ Create a genre model for selecting in the admin"""
    name = models.CharField(max_length=250, help_text='Enter genre(e.g Fiction)')

    def __str__(self):
        """Get the Model object string for genre"""
        return f'Genre: {self.name}'

class Language(models.Model):
    """Model for Languages"""
    name = models.CharField(max_length=200, help_text='Enter book language(e.g English, Swahili etc)')

    def __str__(self):
        """String object for language"""
        return f'Language: {self.name}'

class Book(models.Model):
    """ Create a Book model """
    BOOK_STATUS_CHOICES = (
       ( 'N','New'),
       ( 'U','Used'),
    )
    BEST_SELLER_RANK_LIMIT = 50

    title = models.CharField(max_length=250)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    chart_rank = models.IntegerField()
    book_status = models.CharField(
        max_length=4,
        choices=BOOK_STATUS_CHOICES,
        default='N',
    )
    summary = models.TextField(max_length=1000, help_text='Enter book description')
    isbn = models.CharField('ISBN', max_length=13, help_text='<a href="https://www.isbn-international.org/content/what-isbn">ISBN</a>')
    genre = models.ManyToManyField(Genre, help_text='Select Genre')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def is_best_seller(self):
        """Check if the book is a best seller """
        if self.chart_rank > BEST_SELLER_RANK_LIMIT:
            return True

    def get_absolute_url(self):
        """Return the detail book url"""
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        return f'Title: {self.title}'


class BookInstance(models.Model):
    """ Specific instance of the book with details on availability and date expected"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique Book ID')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('O', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(
        max_length=1,
        choices = LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability'
    )

    class Meta:
        ordering = ['due_back']
    
    def __str__(self):
        return f'ID: {self.id}, Book: {self.book.title}'

class Author(models.Model):
    """Model for the author of book """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Return URL for author"""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """Return the String object for Author"""
        return f'Author: {self.first_name}, {self.last_name}'



