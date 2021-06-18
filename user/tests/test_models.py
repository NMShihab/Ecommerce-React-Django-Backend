from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successfull(self):
        """Test creating a user with new email"""

        email ="test@gmail.com"
        password = "test@123"
        user = get_user_model().objects.create_user(
            email =email,
            password=password
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_create_super_user_with_email_successfull(self):
        """Test creating a super user with new email"""

        email ="test@gmail.com"
        password = "test@123"
        user = get_user_model().objects.create_superuser(
            email =email,
            password=password
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
