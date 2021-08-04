import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_me.settings')
import django
django.setup()

from rango.models import WebSiteCategory, UserCategory, Page
from django.contrib.auth.models import User

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


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()