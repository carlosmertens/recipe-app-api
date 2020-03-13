from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTest(TestCase):

    def setUp(self):
        """Setup superuser and regular user.

        Test for listing users in Django admin.
        """
        # Create super user and force log in for testing
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@mertens-applications.com',
            password='Password123'
        )
        self.client.force_login(self.admin_user)
        # Create regular user
        self.user = get_user_model().objects.create_user(
            email='user@mertens-applications.com',
            password='Password123',
            name='Test User 1'
        )

    def test_users_listed(self):
        """Test users are listed on user page"""
        # Create URL
        url = reverse('admin:core_user_changelist')
        # Create Response
        res = self.client.get(url)

        # Create Assertions
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test the user edit page is working"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test to create user page is working"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
