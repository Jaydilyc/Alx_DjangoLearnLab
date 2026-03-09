from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    # List all books
    path('books/', BookListView.as_view(), name='book-list'),

    # Get a single book by ID
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Create a new book
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Update book
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),

    # Delete book
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]