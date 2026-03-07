from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]

    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title.strip()) < 2:
            raise forms.ValidationError("Title must be at least 2 characters long.")
        return title

    def clean_author(self):
        author = self.cleaned_data["author"]
        if len(author.strip()) < 2:
            raise forms.ValidationError("Author name must be at least 2 characters long.")
        return author