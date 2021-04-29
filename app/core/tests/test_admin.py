from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        """runs before each test fucntion"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="hemantsuper@gmail.com",
            password="test123"
        )

        self.client.force_login(self.admin_user)  # so we dont have to maually login while test run
        self.user = get_user_model().objects.create_user(
            email="hemant@gmail.com",
            password="test123",
            name="test user full name"
        )

    def test_user_listed(self):
        """test that user are listed at user page"""
        url = reverse("admin:core_user_changelist")  # given url are defined in django docs
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    # much advance test
    def test_iser_change_page(self):
        """Test That the user chnage page works"""
        url = reverse("admin:core_user_change", args=[self.user.id])  # /admin/core/user/id
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse("admin:core_user_add")  # /admin/core/user/id
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
