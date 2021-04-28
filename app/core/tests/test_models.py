from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user woth email is successful"""
        email = "hemant@gmail.com"
        password = "test123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test the email for new user is normalized"""
        email = "hemant@GMAIL.com"
        password = "test123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_superuser(self):
        """test creating new superuser"""
        user = get_user_model().objects.create_superuser(
            "super@gmail.com",
            "super123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
