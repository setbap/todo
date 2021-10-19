from django.db.utils import IntegrityError
from django.test import TestCase
from django.contrib.auth import get_user_model


class TestUserModel(TestCase):
    def setUp(self):
        self.email = "a@a.com"
        self.username = "sina"
        self.password = "123sinaAA@@"
        self.User = get_user_model()

    def test_blank_fields(self):
        with self.assertRaises(TypeError):
            self.User.objects.create_user()

        with self.assertRaises(TypeError):
            self.User.objects.create_user(email=self.email)

        with self.assertRaises(TypeError):
            ''' check for email required'''
            self.User.objects.create_user(
                username=self.username, password=self.password)

        with self.assertRaises(ValueError):
            ''' check for email value'''
            self.User.objects.create_user(
                email='',
                username=self.username, password=self.password)

        with self.assertRaises(TypeError):
            ''' check for email required'''
            self.User.objects.create_user(
                email=self.email, password=self.password)

    def test_email_uinque(self):
        self.User.objects.create_superuser(
            username=self.username,
            email=self.email,
            password=self.password,
        )
        with self.assertRaises(IntegrityError):
            self.User.objects.create_superuser(
                username=self.username,
                email="a"+self.email,
                password=self.password,
            )

    def test_simple_user(self):
        """test create simple user succesfull and is not admin"""
        user = self.User.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password,
        )
        self.assertTrue(self.User.objects.filter(
            username=self.username, email=self.email,
        ).exists())
        self.assertTrue(user.check_password(self.password))
        self.assertFalse(user.is_staff)

    def test_admin_user(self):
        """test create admin user succesfull and is  admin"""
        user = self.User.objects.create_superuser(
            username=self.username,
            email=self.email,
            password=self.password,
        )
        self.assertTrue(self.User.objects.filter(
            username=self.username, email=self.email,
        ).exists())
        self.assertTrue(user.check_password(self.password))
        self.assertTrue(user.is_staff)
