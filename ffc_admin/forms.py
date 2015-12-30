from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ffc.models import BlogEntry, Homepage, PinSite


class CreatePinSiteForm(forms.ModelForm):
    class Meta:
        model = PinSite
        fields = ['name']


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class EditHomepageForm(forms.ModelForm):
    homepage = forms.ModelChoiceField(queryset=Homepage.objects.all())

    class Meta:
        model = Homepage
        fields = ('subtitle', 'history')


class EditBlogEntryForm(forms.ModelForm):
    blog_entry = forms.ModelChoiceField(queryset=BlogEntry.objects.all())

    class Meta:
        model = BlogEntry
        fields = ('subtitle', 'body')


class CreateBlogEntryForm(forms.ModelForm):
    index = forms.ModelChoiceField(queryset=PinSite.objects.all())

    class Meta:
        model = BlogEntry
        fields = ('name', 'subtitle', 'body', 'index', 'author')
        widgets = {'author': forms.HiddenInput()}

# class EditUserForm(UserChangeForm):

#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name')
