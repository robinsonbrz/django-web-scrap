from django.test import TestCase
from django.urls import reverse


class MovierankURLsTest(TestCase):
    def test_home_movierank_url_is_correct(self):
        home_url = reverse('movierank:home')
        self.assertEqual(home_url, '/')
