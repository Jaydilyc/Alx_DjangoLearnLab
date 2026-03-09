from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# ListView:
# Returns all books.
# Anyone can access this endpoint (authenticated or not).
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# DetailView:
# Returns one book based on its primary key.
# Anyone can access this endpoint.
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# CreateView:
# Allows authenticated users to add a new book.
# Uses the serializer's built-in validation, including the
# custom publication_year validation defined in BookSerializer.
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Save the new book after serializer validation succeeds.
        serializer.save()


# UpdateView:
# Allows authenticated users to modify an existing book.
# Supports PUT/PATCH requests.
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Save the updated book after serializer validation succeeds.
        serializer.save()


# DeleteView:
# Allows authenticated users to delete a book.
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]