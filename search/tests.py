from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User
from . import views
from rango.models import Page
from django.urls import reverse
from django.shortcuts import render


# Create your tests here.
class SearchFunctionTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(username='test_user', email='test@test.com', password='testuserpassword')
        self.is_authenticated = True

    def test_search(self):
        search_item = 'django'
        request = self.factory.get(reverse('search:search'), data={'search': search_item})
        request.user = self.user
        response = views.search_do(request)
        content = response.content.decode()

        self.assertEquals(response.status_code, 200, f"Failed because of status code:{response.status_code}")
        self.assertTrue(f"<h1>Select Page: {search_item}</h1>" in content,
                        f"Search function failed to pass search item to backend")

        result = Page.objects.filter(title__icontains=search_item)
        for data in result:
            self.assertTrue(data.title in content, f"搜索结果不存在")
