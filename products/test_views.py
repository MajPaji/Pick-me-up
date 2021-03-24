from django.test import TestCase
from .models import Product
from django.contrib.auth.models import User


class TestProductsViews(TestCase):

    def test_get_products_all_page_page(self):
        """ test for rendering the products page """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_product_detail_page(self):
        product = Product.objects.create(
            name='Test Name',
            price='11.11',
            description='Test Description',
            prtype='Test Type'
        )
        response = self.client.get(f'/products/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_get_add_product_page(self):
        test_admin_user = User.objects.create_user(
            username='test_name',
            email='test_email@email.com',
            password=None,
            is_superuser=True,
            )

        self.client.force_login(test_admin_user)
        response = self.client.get('/products/add_product/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_product.html')

    def test_get_edit_product_page(self):
        test_admin_user = User.objects.create_user(
            username='test_name',
            email='test_email@email.com',
            password=None,
            is_superuser=True,
            )

        product = Product.objects.create(
            name='Test Name',
            price='11.11',
            description='Test Description',
            prtype='Test Type'
        )

        self.client.force_login(test_admin_user)
        response = self.client.get(f'/products/edit_product/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_product.html')

    def test_can_add_product(self):
        test_admin_user = User.objects.create_user(
            username='test_name',
            email='test_email@email.com',
            password=None,
            is_superuser=True,
            )

        self.client.force_login(test_admin_user)
        response = self.client.post('/products/add_product/', {
            'name': 'Test Name',
            'price': '11.11',
            'description': 'Test Description',
            'prtype': 'Test Type',
        })
        self.assertRedirects(response, '/products/1/')

    def test_can_delete_product(self):
        test_admin_user = User.objects.create_user(
            username='test_name',
            email='test_email@email.com',
            password=None,
            is_superuser=True,
            )

        product = Product.objects.create(
            name='Test Name',
            price='11.11',
            description='Test Description',
            prtype='Test Type'
        )

        self.client.force_login(test_admin_user)
        response = self.client.get(f'/products/delete_product/{product.id}/')
        self.assertRedirects(response, '/products/')
        existing_product = Product.objects.filter(id=product.id)
        self.assertEqual(len(existing_product), 0)

    def test_can_edit_product(self):
        test_admin_user = User.objects.create_user(
            username='test_name',
            email='test_email@email.com',
            password=None,
            is_superuser=True,
            )

        product = Product.objects.create(
            name='Test Name',
            price='11.11',
            description='Test Description',
            prtype='Test Type'
        )

        self.client.force_login(test_admin_user)
        response = self.client.post(f'/products/edit_product/{product.id}/', {
            'name': 'Edited Test Name',
            'price': '99.99',
            'description': 'Edited Test Description',
            'prtype': 'Edited Test Type',
        })
        self.assertRedirects(response, '/products/1/')
        updated_product = Product.objects.get(id=product.id)
        self.assertEqual(updated_product.name, 'Edited Test Name')

