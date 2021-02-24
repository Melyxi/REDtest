from django.test.client import Client
from django.core.management import call_command
from django.test import TestCase
from authapp.models import User


class TestMainappSmoke(TestCase):
    def setUp(self):
        call_command('flush', '--noinput')
        self.client = Client()

        self.superuser = User.objects.create_superuser(username='developer', email='12@r.ru', password='developer')

        self.user = User.objects.create_user(username='admin', email='121@r.ru', password='123test123', role='ADMIN')

        self.user = User.objects.create_user(username='user', email='1213@r.ru', password='123test123', role='USER')

    def test_mainapp_urls(self):
        # тест для гостя

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_anonymous)
        response = self.client.get('/administrator/')
        self.assertEqual(response.status_code, 404)

        response = self.client.get('/developer/')
        self.assertEqual(response.status_code, 404)

        response = self.client.get('/user/')
        self.assertEqual(response.status_code, 404)

        # данные пользователя
        self.client.login(username='user', password='123test123')

        # логинимся
        response = self.client.get('/auth/login/')
        print(response)
        self.assertFalse(response.context['user'].is_anonymous)
        # self.assertEqual(response.context['user'], self.user)

        # главная после логина
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/user/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/administrator/')
        self.assertEqual(response.status_code, 404)

        response = self.client.get('/developer/')
        self.assertEqual(response.status_code, 404)



        # данные администратора
        self.client.login(username='admin', password='123test123')

        # логинимся
        response = self.client.get('/auth/login/')
        self.assertFalse(response.context['user'].is_anonymous)

        # главная после логина
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/administrator/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/user/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/developer/')
        self.assertEqual(response.status_code, 404)

        # Данные разработчика
        self.client.login(username='developer', password='developer')
        # логинимся
        response = self.client.get('/auth/login/')
        self.assertFalse(response.context['user'].is_anonymous)

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/administrator/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/user/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/developer/')
        self.assertEqual(response.status_code, 200)

