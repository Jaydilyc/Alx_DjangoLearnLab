from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from .models import Book


@login_required
@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})


@login_required
@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        publication_year = request.POST.get("publication_year")

        Book.objects.create(
            title=title,
            author=author,
            publication_year=publication_year
        )
        return HttpResponse("Book created successfully")

    return render(request, "bookshelf/book_form.html")


@login_required
@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.publication_year = request.POST.get("publication_year")
        book.save()
        return HttpResponse("Book updated successfully")

    return render(request, "bookshelf/book_form.html", {"book": book})


@login_required
@permission_required("bookshelf.can_delete", raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        return HttpResponse("Book deleted successfully")

    return render(request, "bookshelf/book_confirm_delete.html", {"book": book})