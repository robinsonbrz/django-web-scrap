from django.test import TestCase
from django.urls import resolve, reverse
from movierank import views


class MovierankViewsTest(TestCase):
    def test_movierank_home_view_function_is_correct(self):
        home_url = reverse('movierank:home')
        view = resolve(home_url)
        self.assertIs(view.func, views.home)                                                                   


    def test_movierank_home_view_returns_status_code_200_ok(self):
        # self.client.get é o q o cliente solicita ao clicar
        response = self.client.get(reverse('movierank:home'))
        self.assertEqual(response.status_code, 200)


    def test_movierank_home_view_loads_correct_template(self):
        response = self.client.get(reverse('movierank:home'))
        self.assertTemplateUsed(response, 'movierank/pages/home.html')
