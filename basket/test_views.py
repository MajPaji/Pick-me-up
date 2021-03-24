from django.test import TestCase


class TestBasketViews(TestCase):

    def test_get_basket_page(self):
        response = self.client.get('/basket/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket/basket.html')

