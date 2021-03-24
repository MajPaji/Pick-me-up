from django.test import TestCase


class TestHomeViews(TestCase):

    def test_get_home_page(self):
        """ test redering home page """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html')
