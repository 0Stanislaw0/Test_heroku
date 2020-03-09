import unittest

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.test import APITestCase


class SigninTest(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(email='stas.yyyy20gmail.com',
                                                         password='123',
                                                        )
        self.user.save()
    # 681d81caebe70e7c8c8237ab3249997ea5edd539

    def test_correct(self):
        user = authenticate(email='stas.yyyy20gmail.com', password='123')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(email='wrong@asd1', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(email='stas.yyyy20gmailcom', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)


# class SignInViewTest(TestCase):
#
#     def setUp(self):
#         self.client.post('user/', {'username': 'tests',
#                                    'password1': '12test12',
#                                    'password2': '12test12',
#                                    'email': 'stas.yyyy@mail.ru'})
#
#     def tearDown(self):
#         get_user_model().objects.filter(username='tests').delete()
#
#     def test_correct(self):
#         self.client.login(username='tests', password='12test12')
#
#
# class UserOurRegistration(TestCase):
#
#     def test_base_form(self):
#         self.assertEqual(list(UserOurRegistration.base_fields), ['username', 'password1', 'password2', 'email'])
