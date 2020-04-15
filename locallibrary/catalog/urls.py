from django.urls import path
from . import views as v
urlpatterns = [
    path('', v.catalog_view, name='index'),
    path('books/', v.BookListView.as_view(), name='book-list'),
    path('book/<slug>', v.BookDetailView.as_view(), name='book-detail'),
    path('authors/', v.AuthorListView.as_view(), name='author-list'),
    path('author/<int:pk>', v.AuthorDetailView.as_view(), name='author-detail'),
]