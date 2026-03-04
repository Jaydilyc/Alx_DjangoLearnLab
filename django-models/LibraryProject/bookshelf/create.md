```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book

## Expected output:
## (1, '1984', 'George Orwell', 1949)