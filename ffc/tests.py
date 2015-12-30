from django.test import TestCase
from ffc.models import BlogEntry, Homepage, PinSite


class TestModels(TestCase):

    def setUp(self):
        self.homepage1 = Homepage.objects.create(
            name='test1-homepage-name',
            subtitle='test1-homepage-subtilte',
            history='test1-homepage-history'
        )
        self.pinsite1 = PinSite.objects.create(
            name='test1-pinsite',
            slug='test1-pinsite-slug',
            homepage=self.homepage1,
        )
        self.blog_entry1 = BlogEntry.objects.create(
            index=self.pinsite1,
            slug='test1-blogentry-slug',
            name='test1-name',
            subtitle='test1-subtilte',
        )

        self.homepage2 = Homepage.objects.create(
            name='test2-homepage-name',
            subtitle='test2-homepage-subtilte',
            history='test2-homepage-history'
        )
        self.pinsite2 = PinSite.objects.create(
            name='test2-pinsite',
            slug='test2-pinsite-slug',
            homepage=self.homepage1,
        )
        self.blog_entry2 = BlogEntry.objects.create(
            index=self.pinsite2,
            slug='test2-blogentry-slug',
            name='test2-name',
            subtitle='test2-subtilte',
        )

    def test_pisite_get_blog_posts(self):
        self.assertEqual(
            self.pinsite1.get_blog_posts(), [self.blog_entry1]
        )
        self.assertEqual(
            self.pinsite2.get_blog_posts(), [self.blog_entry2]
        )
