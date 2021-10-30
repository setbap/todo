from django.test import TestCase
from django.contrib.auth import get_user_model
from api.models import Todo


class TagTest(TestCase):

    def setUp(self):
        email = "a@a.com"
        username = "sina"
        password = "123sinaAA@@"
        User = get_user_model()
        self.user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
        )
