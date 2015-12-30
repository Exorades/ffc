from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify


class PinSite(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(unique=True, editable=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='sites',
        editable=False
    )

    def get_absolute_url(self):
        return reverse('ffc:pinsite_detail', args=[self.slug])

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(PinSite, self).save(*args, **kwargs)


class Homepage(models.Model):
    site = models.OneToOneField(PinSite)
    name = models.CharField(max_length=64, unique=True, editable=False)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    history = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = '{} homepage'.format(self.site.name)
        super(Homepage, self).save(*args, **kwargs)


class BlogEntry(models.Model):
    index = models.ForeignKey(PinSite)
    slug = models.SlugField(unique=True, editable=False)
    name = models.CharField(max_length=100)
    subtitle = models.TextField(max_length=250, blank=True, null=True)
    body = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='blog_posts'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = '{}-{}'.format(self.index.id, slugify(self.name))
        super(BlogEntry, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class META:
        verbose_name = 'Blog Entry'
        verbose_name_plural = 'Blog Entries'
