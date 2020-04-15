from django.shortcuts import render
from . models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.
def catalog_view(request):
    count_books = Book.objects.all().count()
    count_instances = BookInstance.objects.all().count()

    #Available books
    count_available_book_instances = BookInstance.objects.filter(status__exact='a').count()

    #Count authors
    count_authors = Author.objects.all().count()

    #context
    context = {
        'number_of_books': count_books,
        'number_of_instances': count_instances,
        'number_of_available_instances': count_available_book_instances,
        'number_of_authors': count_authors,
    }
    return render(request, 'catalog/catalog.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    # context_object_name = 'book_list'
    # queryset = Book.objects.all()
    # template_name = 'catalog/books/books_list.html'

class BookDetailView(generic.DetailView):
    model = Book
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2

class AuthorDetailView(generic.DetailView):
    model = Author