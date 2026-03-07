from django import forms
from .models import Book


class ExampleForm(forms.Form):
    title = forms.CharField(max_length=200)
    author = forms.CharField(max_length=100)
    publication_year = forms.IntegerField()

    def clean_title(self):
        title = self.cleaned_data.get("title")

        if len(title.strip()) < 2:
            raise forms.ValidationError("Title must be at least 2 characters long.")

        return title


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]