from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        """test할 때 준비할 것들  setup!"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="email@email.com",
            password='password123'
        )
        # force_login : client, user의 helper function
        # argument로 client에 로그인하는 함수
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@test.com',
            password='password123',
            name='Test user full name'
        )

    def test_user_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works
        error 수정을 위해 core.admin.py에 fieldsets 추가 """
        url = reverse('admin:core_user_change', args=[self.user.id])
        # /admin/core/user/<ID>
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
