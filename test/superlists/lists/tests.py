from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        print(repr(expected_html))
        self.assertEqual(response.content.decode(), expected_html)
