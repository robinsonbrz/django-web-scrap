from django.test import TestCase
from django.urls import resolve, reverse

from movierank import views


class MovierankURLsTest(TestCase):
    def test_home_movierank_url_is_correct(self):
        home_url = reverse('movierank:home')
        self.assertEqual(home_url, '/')


class MovierankViewsTest(TestCase):
    def test_movierank_home_view_function_is_correct(self):
        home_url = reverse('movierank:home')
        view = resolve(home_url)
        self.assertIs(view.func, views.home)


