## Book API Views

This project uses Django REST Framework generic views to implement CRUD operations for the Book model.

### Endpoints

- `GET /api/books/`  
  Lists all books. Publicly accessible.

- `GET /api/books/<int:pk>/`  
  Retrieves details of a single book. Publicly accessible.

- `POST /api/books/create/`  
  Creates a new book. Requires authentication.

- `PUT /api/books/<int:pk>/update/`  
  Updates an existing book. Requires authentication.

- `DELETE /api/books/<int:pk>/delete/`  
  Deletes a book. Requires authentication.

### Validation

The `BookSerializer` validates that `publication_year` is not in the future.

### Permissions

- Unauthenticated users have read-only access.
- Authenticated users can create, update, and delete books.

## Filtering, Searching, and Ordering

The `BookListView` supports filtering, searching, and ordering using Django REST Framework filter backends.

### Filtering

You can filter books by:

- `title`
- `author`
- `publication_year`

Examples:

- `/api/books/?title=Things Fall Apart`
- `/api/books/?publication_year=1958`
- `/api/books/?author=1`

### Searching

You can search books by:

- `title`
- `author__name`

Examples:

- `/api/books/?search=Things`
- `/api/books/?search=Achebe`

### Ordering

You can order books by:

- `title`
- `publication_year`

Examples:

- `/api/books/?ordering=title`
- `/api/books/?ordering=-publication_year`