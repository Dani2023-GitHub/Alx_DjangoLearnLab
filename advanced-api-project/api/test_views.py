from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book, Author

class APITestSetUp(APITestCase):
    def setup(self):
        self.author = Author.objects.create(name="Daniel")
        self.book = Book.objects.create(title="API test", publication_year=2024, author =self.author)

        self.list_url = f'/books/'
        self.create_url = f'/books/create/'
        self.update_url = f'/books/{self.book.id}/update/'
        self.delete_url = f'/books/{self.book.id}/delete/'
        self.detail_url = f'/books/{self.book.id}/'
        print(self.__dict__)
#test functionality of list view
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.dat), 1)
        self.assertEqual(response.data[0]['title'], "API test")

#test functionality of book create view and authentication
    def test_create_book_unauthorized(self):
        data = {"title":"Testing create", 'publication_year':2020, 'author': 'Bob' }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

#test functionality book updating and authentication
    def test_update_book_authenticate(self):
        self.client.login(username="test", password='abc123')
        data = {'title': 'updated book'}
        response = self.client.put(self.update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "updated book")

#test functionality of book deletion view
    def test_delete_book_authenticate(self):
        self.client.login(username="test", password='abc123')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)  
        print(self.__dict__)  
