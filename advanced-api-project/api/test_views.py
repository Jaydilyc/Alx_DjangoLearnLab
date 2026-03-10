from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        """
        Set up test data for all test methods.
        Creates a user, author, and sample books for testing.
        """
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )

        self.author = Author.objects.create(name='Chinua Achebe')

        self.book1 = Book.objects.create(
            title='Things Fall Apart',
            publication_year=1958,
            author=self.author
        )

        self.book2 = Book.objects.create(
            title='No Longer at Ease',
            publication_year=1960,
            author=self.author
        )

        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', kwargs={'pk': self.book1.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book1.pk})

    def test_list_books(self):
        """
        Test that all books can be listed successfully.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_single_book(self):
        """
        Test that a single book can be retrieved successfully.
        """
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Things Fall Apart')

    def test_create_book_authenticated(self):
        """
        Test that an authenticated user can create a book.
        """
        self.client.login(username='testuser', password='testpassword123')

        data = {
            'title': 'Arrow of God',
            'publication_year': 1964,
            'author': self.author.id
        }

        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, 'Arrow of God')

    def test_create_book_unauthenticated(self):
        """
        Test that an unauthenticated user cannot create a book.
        """
        data = {
            'title': 'Arrow of God',
            'publication_year': 1964,
            'author': self.author.id
        }

        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        """
        Test that an authenticated user can update a book.
        """
        self.client.login(username='testuser', password='testpassword123')

        data = {
            'title': 'Things Fall Apart Updated',
            'publication_year': 1958,
            'author': self.author.id
        }

        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Things Fall Apart Updated')

    def test_update_book_unauthenticated(self):
        """
        Test that an unauthenticated user cannot update a book.
        """
        data = {
            'title': 'Things Fall Apart Updated',
            'publication_year': 1958,
            'author': self.author.id
        }

        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_authenticated(self):
        """
        Test that an authenticated user can delete a book.
        """
        self.client.login(username='testuser', password='testpassword123')

        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_delete_book_unauthenticated(self):
        """
        Test that an unauthenticated user cannot delete a book.
        """
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_filter_books_by_title(self):
        """
        Test filtering books by title.
        """
        response = self.client.get(self.list_url, {'title': 'Things Fall Apart'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Things Fall Apart')

    def test_search_books_by_title(self):
        """
        Test searching books by title.
        """
        response = self.client.get(self.list_url, {'search': 'Things'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_author_name(self):
        """
        Test searching books by author name.
        """
        response = self.client.get(self.list_url, {'search': 'Achebe'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_order_books_by_publication_year(self):
        """
        Test ordering books by publication year.
        """
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 1958)
        self.assertEqual(response.data[1]['publication_year'], 1960)