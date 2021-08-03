from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(verbose_name='avatar', upload_to='profile_images', blank=True)
    background_img = models.ImageField(verbose_name='bg_img', upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username



class WebSiteCategory(models.Model):
    name = models.CharField(verbose_name='Category', max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'WebSiteCategories'


    def __str__(self):
        return self.name


class UserCategory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='category_name', max_length=128, null=False)
    # define an alias for specific user_category: username_categoryname
    alias = models.CharField(verbose_name='user_category', max_length=128)

    class Meta:
        verbose_name_plural = 'User Categories'

    def __str__(self):
        return self.name


class Page(models.Model):
    web_site_category = models.ForeignKey(WebSiteCategory, on_delete=models.CASCADE)
    user_category = models.ForeignKey(UserCategory, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='title', max_length=128)
    url = models.URLField(verbose_name='url')
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

