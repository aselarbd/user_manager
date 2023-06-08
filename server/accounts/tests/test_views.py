from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory, TestCase
from django.test.client import Client
from django.urls import reverse
from knox.models import AuthToken

from server.accounts.models import CustomUser
from server.accounts.views.user_login_post import user_login_view
from server.accounts.views.user_register_post import user_register_view


class TestViews(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = CustomUser.objects.create_user(email='user@cs.com', password='password')
        self.client = Client()
        self.middleware = SessionMiddleware(get_response=self.client.get)
        self.token = AuthToken.objects.create(user=self.user)

    def test_user_register_view_success(self) -> None:
        url = reverse('register')
        data = {
            'email': 'test@cs.com',
            'password': 'test1234',
            'first_name': 'FName',
            'last_name': 'LName',
            'date_of_birth': '2023-06-07',
        }

        request = self.factory.post(url, data)
        response = user_register_view(request)
        self.assertEqual(response.status_code, 201)

    def test_user_register_view_failure(self) -> None:
        url = reverse('register')
        data = {
            'email': 'test@cs.com',
            'password': 'test1234',
            'first_name': 'FName',
            'last_name': 'LName',
        }

        request = self.factory.post(url, data)
        response = user_register_view(request)
        self.assertEqual(response.status_code, 400)

    def test_user_login_view_success(self) -> None:
        url = reverse('login')
        data = {'email': 'user@cs.com', 'password': 'password'}
        request = self.factory.post(url, data)

        self.middleware.process_request(request)
        request.session.save()

        response = user_login_view(request)

        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data)
        self.assertIn('expire', response.data)

    def test_user_login_view_failure(self) -> None:
        url = reverse('login')
        data = {'email': 'user@cs.com', 'password': 'password_wrong'}
        request = self.factory.post(url, data)

        self.middleware.process_request(request)
        request.session.save()

        response = user_login_view(request)

        self.assertEqual(response.status_code, 400)
