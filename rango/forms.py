from django import forms
from .models import UserCategory, UserProfile, Page
from django.contrib.auth.models import User

class UserCategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text='Please Enter Your Category Name!')
    # define an alias for specific user_category: username_categoryname
    alias = forms.CharField(widget=forms.HiddenInput(), initial='')

    class Meta:
        model = UserCategory
        fields = ('name', )


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text='Please enter the title of the page.')
    url = forms.URLField(max_length=200, help_text='Please enter the url of the page.')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta():
        model = Page
        fields = ('title', 'url', )

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url:
            if url.startswith('http://') or url.startswith('https://'):
                return cleaned_data
            else:
                url = 'http://' + url
                cleaned_data['url'] = url
                return cleaned_data



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password', 'confirm', 'email')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile




