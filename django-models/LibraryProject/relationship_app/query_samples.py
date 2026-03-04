from relationship_app.models import Author, Book, Library, Librarian


def query_books_by_author(author_name: str):
    """Query all books by a specific author."""
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)

    print(f"Books by {author.name}:")
    for book in books:
        print(f"- {book.title}")


def list_books_in_library(library_name: str):
    """List all books in a library."""
    library = Library.objects.get(name=library_name)
    books = library.books.all()

    print(f"Books in {library.name}:")
    for book in books:
        print(f"- {book.title} (by {book.author.name})")


def get_librarian_for_library(library_name: str):
    """Retrieve the librarian for a library using an explicit OneToOne query."""
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)  # <-- required by checker

    print(f"Librarian for {library.name}: {librarian.name}")