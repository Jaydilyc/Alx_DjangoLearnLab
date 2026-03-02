
---

## 📄 `retrieve.md`

```markdown
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.id, book.title, book.author, book.publication_year

## Expected output:
## 'Nineteen Eighty-Four'