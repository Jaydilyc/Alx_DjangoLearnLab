from relationship_app.models import Author, Book, Library


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
    """Retrieve the librarian for a library."""
    library = Library.objects.get(name=library_name)

    # We used related_name="librarian" in the OneToOneField
    librarian = library.librarian

    print(f"Librarian for {library.name}: {librarian.name}")