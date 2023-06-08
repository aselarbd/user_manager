from django.test import TestCase

from server.accounts.models import CustomUser


class TestModels(TestCase):
    def test_CustomUser_model(self) -> None:
        user_data = {
            'email': 'test@cs.com',
            'password': 'test1234',
            'first_name': 'FName',
            'last_name': 'LName',
            'date_of_birth': '2023-06-07',
        }

        user = CustomUser(**user_data)

        self.assertEqual(user.first_name, 'FName')
        self.assertEqual(user.last_name, 'LName')
        self.assertEqual(user.email, 'test@cs.com')
        self.assertEqual(user.date_of_birth, '2023-06-07')
