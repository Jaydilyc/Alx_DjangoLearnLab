
*(Note: the `1` may be different depending on your DB, that’s normal.)*

---

## 📄 `update.md`

```markdown
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title