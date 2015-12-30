from django.conf.urls import url
from django.views.generic import TemplateView
from ffc_admin import views

urlpatterns = [
    url(
        r'^$',
        TemplateView.as_view(template_name='ffc_admin/admin.html'),
        name='admin'
    ),
    url(
        r'^create_site/$',
        views.CreatePinSiteView.as_view(),
        name='create_site'
    ),
    url(
        r'^homepage_edit/$',
        views.EditHomepageView.as_view(),
        name='homepage_edit'
    ),
    url(
        r'^blog_entry_edit/$',
        views.EditBlogEntryView.as_view(),
        name='blog_entry_edit'
    ),
    url(
        r'^create_user/$',
        views.CreateUserView.as_view(),
        name='create_user'
    ),
    url(
        r'^create_blog_entry/$',
        views.CreateBlogEntryView.as_view(),
        name='create_blog_entry'
    ),

    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
]
