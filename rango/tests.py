from django.test import TestCase, RequestFactory, Client
from .models import WebSiteCategory, Video
from django.contrib.auth.models import User
from django.urls import reverse
from . import views
import re


# Create your tests here.
class WebSiteCategoryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        WebSiteCategory.objects.create(name="Java", views=0, likes=0)

    def test_str_return_value(self):
        web_site_category = WebSiteCategory.objects.get(name="Java").name
        self.assertEquals(web_site_category, 'Java')


class AuthTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(username='test_user', email='test@test.com', password='testuserpassword')

    # test index page
    def test_index_without_login(self):
        request = self.factory.get(reverse('rango:index'))
        response = views.index(request)
        content = response.content.decode()

        self.assertEqual(response.status_code, 200)
        self.assertTrue('<h3 class="text-center">Top 5 Viewd Category</h3>' in content,
                        f"Index page doesn't show Top 5 Viewd Category")
        self.assertTrue(' <li><a href="/accounts/login/">Login</a></li>' in content,
                        f"User has logged in, we are now testing index without logging in")

    def test_index_with_login(self):
        class MockUser:
            username = self.user.username
            password = self.user.password
            is_authenticated = True

        request = self.factory.get(reverse('rango:index'))
        request.user = MockUser()
        response = views.index(request)
        content = response.content.decode()
        # print(content)
        self.assertEquals(response.status_code, 200)
        self.assertTrue('<li><a href="/accounts/logout/">Loguut</a></li>' in content, f"should login")
        self.assertTrue(f"<h3>Welcome {request.user.username}</h3>" in content, f"not login")


class VideoFunctionTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(username='test_user', email='test@test.com', password='testuserpassword')
        self.is_authenticated = True

    def test_add_video(self):
        class MockUser:
            username = self.user.username
            password = self.user.password
            is_authenticated = True

        data = {
            'video_title': 'Flutter Tutorial - Bottom Navigation Bar | The Right Way [2021] Without Routes',
            'iframe_url': '<iframe width="560" height="315" src="https://www.youtube.com/embed/xoKqQjSDZ60" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
        }

        request = self.factory.post(reverse('rango:add_video'), data=data)
        request.user = MockUser()
        response = views.add_video(request)
        # after add video, the video object should be added to database
        data_in_db = Video.objects.get(title=data['video_title'])
        self.assertEquals(response.status_code, 302, "not redirected to video page")
        self.assertEquals(data_in_db.iframe_url, data['iframe_url'], msg=f"Title not match with iframe_url")

    def test_video_view(self):


        data = [
            {
                'video_title': 'Flutter Tutorial - Bottom Navigation Bar | The Right Way [2021] Without Routes',
                'iframe_url': '<iframe width="560" height="315" src="https://www.youtube.com/embed/xoKqQjSDZ60" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
            },
            {
              'video_title' : 'Flutter Tutorial - How To Use Hex Color Codes & RGB Colors & Transparent Colors [2021]',
                'iframe_url': '<iframe width="560" height="315" src="https://www.youtube.com/embed/3Fb3bFSOJWA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
            },
        ]
        for d in data:
            Video.objects.create(user=self.user, title=d['video_title'], iframe_url=d['iframe_url'])

        request = self.factory.get(reverse('rango:videos'))
        request.user = self.user
        response = views.videos(request)
        content = response.content.decode('utf-8')
        user_video_list = Video.objects.filter(user__username=request.user.username)

        if len(user_video_list) == 0:
            self.assertTrue(f"<strong>There is no videos added by {request.user.username}</strong>" in content,
                            f"this user has videos in his video page")
        else:
            video = user_video_list[0]
            pattern = r'src=.+"\s[titlescrolling]'
            substr = re.search(pattern, video.iframe_url)
            url = substr.group().split(' ')[0].split('"')[1]
            self.assertEqual(response.status_code, 200, msg=f"Failed because of status: {response.status_code}")
            self.assertTrue(f"<h1>Videos</h1>" in content, f"This is not Video pages")
            self.assertTrue(f"<h3>Welcome {request.user.username}'s Video List</h3>" in content,
                            f"This is not Video pages")
            self.assertTrue(f"<label>{data[0]['video_title']}</label>" in content, f"No video title in this page")
            self.assertTrue(f"""                <iframe width="620" height="370" src="{url}"
                        title="YouTube video player" frameborder="0"
                        seamless="seamless"
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                        sandbox="allow-top-navigation allow-same-origin allow-forms allow-scripts"
                        allowfullscreen></iframe""" in content, f"No video embedded in this page")





