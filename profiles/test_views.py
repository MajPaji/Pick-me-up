from django.test import TestCase
from django.contrib.auth.models import User


class TestProfileView(TestCase):

    def test_view_profiles(self):
        test_user = User.objects.create_user(
            username='test_name',
            email='test_mail@mail.com',
            password=None,)

        self.client.force_login(test_user)
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
