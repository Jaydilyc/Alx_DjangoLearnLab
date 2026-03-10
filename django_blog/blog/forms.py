from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Tag


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text='Enter tags separated by commas')

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        post = super().save(commit=False)

        if commit:
            post.save()

            tags_input = self.cleaned_data.get('tags', '')
            tag_names = [tag.strip() for tag in tags_input.split(',') if tag.strip()]

            post.tags.clear()
            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                post.tags.add(tag)

        return post

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            self.fields['tags'].initial = ', '.join(
                tag.name for tag in self.instance.tags.all()
            )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']