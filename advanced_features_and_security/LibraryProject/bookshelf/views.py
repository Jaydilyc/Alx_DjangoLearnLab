from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from .models import Book
from .forms import ExampleForm


@login_required
@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})


@login_required
@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = ExampleForm()

    return render(request, "bookshelf/form_example.html", {"form": form})


@login_required
@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        form = ExampleForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = ExampleForm(instance=book)

    return render(request, "bookshelf/form_example.html", {"form": form})


@login_required
@permission_required("bookshelf.can_delete", raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect("book_list")

    return render(request, "bookshelf/book_confirm_delete.html", {"book": book})