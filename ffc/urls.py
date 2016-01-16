from django.conf.urls import url
from ffc import views

urlpatterns = [
    url(r'^$', views.PinSiteListView.as_view(), name='pinsite_list'),
    url(
        r'^(?P<pinsite>[-_\w]+)/$',
        views.PinSiteDetailView.as_view(),
        name='pinsite_detail'
    ),
    url(
        r'^(?P<pinsite>[-\w]+)/blog/$',
        views.BlogIndexListView.as_view(),
        name='blog_index'
    ),
    url(
        r'^(?P<pinsite>[-\w]+)/blog/(?P<blog_entry_slug>[-\w]+)$',
        views.BlogEntryView.as_view(),
        name='blog_entry'
    ),

]
