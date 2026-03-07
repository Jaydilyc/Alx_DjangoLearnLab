# Permissions and Groups Setup

## Custom Permissions
The `Book` model in `bookshelf/models.py` defines these custom permissions:

- can_view
- can_create
- can_edit
- can_delete

## Groups
The following groups were created in Django admin:

- Viewers
- Editors
- Admins

## Permission Assignment
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: can_view, can_create, can_edit, can_delete

## Views Protected
- `book_list` uses `bookshelf.can_view`
- `book_create` uses `bookshelf.can_create`
- `book_edit` uses `bookshelf.can_edit`
- `book_delete` uses `bookshelf.can_delete`

## Testing
Users were assigned to groups and tested to confirm that access is restricted according to permissions.