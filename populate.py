import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_me.settings')
import django
django.setup()

from rango.models import WebSiteCategory, UserCategory, Page, Video
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site

def populate():
    # creating pages data
    python_pages = [
       {'title': 'Official Python Tutorial',
        'url': 'http://docs.python.org/3/tutorial/',
        'views': 12,
        'likes': 34
        },
       {'title': 'How to Think like a Computer Scientist',
        'url': 'http://www.greenteapress.com/thinkpython/',
        'views': 23,
        'likes': 63,
        },
       {'title': 'Learn Python in 10 Minutes',
        'url': 'http://www.korokithakis.net/tutorials/python/',
        'views': 34,
        'likes': 87,
        },]

    django_pages = [
        {'title': 'Official Django Tutorial',
         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views': 45,
         'likes': 36,
         },
        {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com/',
         'views': 56,
         'likes': 64,
         },
        {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/',
         'views': 67,
         'likes': 93,
         }
    ]

    # create WebSiteCategories
    website_categories = {
        'python': {'pages': python_pages, 'views': 12, 'likes': 23},
        'django': {'pages': django_pages, 'views': 64, 'likes': 32},
        'golang': {'pages': [], 'views': 55, 'likes': 45},
        'flutter': {'pages': [], 'views': 62, 'likes': 78},
        'gin': {'pages': [], 'views': 98, 'likes': 63},
    }

    add_website_category(website_categories)
    for c in WebSiteCategory.objects.all():
        for p in Page.objects.filter(web_site_category=c):
            print(f"- {c}: {p}")

    host = 'http://127.0.0.1:8000'
    third_party = [['Google', 'google', '975913225146-kli9v7upjr2rr8te03ehrbuh6lk3oh8t.apps.googleusercontent.com', '51_TsWnabM7oZYh5cLxewPm4', host],
           ['Github', 'github', '7b601069dfcf98816b94', '66e4c37e4ba25a79de52e488295e14a0f80b263d', host]]

    try:
        new_site = Site.objects.get(domain='example.com')
        new_site.domain = host
        new_site.name = host
        new_site.save()
    except:
        new_site = Site.objects.get_or_create(domain=host)[0]
        new_site.save()

    for item in third_party:
        third_party_provider(item[0], item[1], item[2], item[3], item[4])



def third_party_provider(provider, name, client_id, secret, domain):
    site = Site.objects.filter(domain=domain)
    s = SocialApp.objects.get_or_create(provider=provider, name=name, client_id=client_id, secret=secret)[0]
    s.sites.set(site)
    s.save()
    return s

def add_website_category(website_categories):
    default_user_category = create_default_user_category()
    for cat_name, cat_data in website_categories.items():
        cat = WebSiteCategory.objects.get_or_create(name=cat_name)[0]
        cat.views = cat_data['views']
        cat.likes = cat_data['likes']
        cat.save()
        for page_data in cat_data['pages']:
            page = Page.objects.get_or_create(web_site_category=cat, title=page_data['title'], user_category=default_user_category)[0]
            page.url = page_data['url']
            page.views = page_data['views']
            page.likes = page_data['likes']
            page.save()



def create_default_user_category():
    default_user = User.objects.get_or_create(username='default')[0]
    default_user_category = UserCategory.objects.get_or_create(user=default_user, name='default')[0]
    return default_user_category




def import_video():
    data = [
        {
            'video_title': 'Flutter Tutorial - Bottom Navigation Bar | The Right Way [2021] Without Routes',
            'iframe_url': '<iframe width="560" height="315" src="https://www.youtube.com/embed/xoKqQjSDZ60" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
        },
        {
            'video_title': 'Flutter Tutorial - How To Use Hex Color Codes & RGB Colors & Transparent Colors [2021]',
            'iframe_url': '<iframe width="560" height="315" src="https://www.youtube.com/embed/3Fb3bFSOJWA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
        },
    ]

    user = User.objects.get_or_create(username='user_has_video', email='user@video.com', password='testuser')[0]
    for d in data:
        video = Video.objects.get_or_create(user=user)[0]
        video.title = d['video_title']
        video.iframe_url = d['iframe_url']
        print(video.title, video.iframe_url)
        video.save()


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
    import_video()





