from django.test import SimpleTestCase
from django.urls import resolve, reverse
from knox.views import LogoutAllView, LogoutView

from server.accounts.views.user_login_post import user_login_view
from server.accounts.views.user_register_post import user_register_view


class TestUrls(SimpleTestCase):
    def test_register_url_resolved(self) -> None:
        url = reverse('register')
        self.assertEqual(resolve(url).func, user_register_view)

    def test_login_url_resolved(self) -> None:
        url = reverse('login')
        self.assertEqual(resolve(url).func, user_login_view)

    def test_logout_url_resolved(self) -> None:
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class, LogoutView)

    def test_logout_all_url_resolved(self) -> None:
        url = reverse('logout_all')
        self.assertEqual(resolve(url).func.view_class, LogoutAllView)
