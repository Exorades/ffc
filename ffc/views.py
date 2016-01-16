from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
)
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView
from ffc.models import PinSite


class HomePageView(TemplateView):
    pass


class PinSiteListView(ListView):
    queryset = PinSite.objects.all()
    context_object_name = 'pinsites'
    paginate_by = 5
    template_name = 'ffc/site_list.html'


class PinSiteDetailView(TemplateView):
    template_name = 'ffc/site_detail.html'

    def get(self, request, pinsite):
        pinsite_data = get_object_or_404(PinSite, slug=pinsite)
        return render(
            request,
            self.template_name,
            {
                'pinsite': pinsite_data,
            }
        )


class BlogIndexListView(TemplateView):
    template_name = 'ffc/blog_index.html'

    def post_list(self, request, pinsite_data):
        object_list = pinsite_data.blogentry_set.all()
        paginator = Paginator(object_list, 5)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return page, posts

    def get(self, request, pinsite):
        pinsite_data = get_object_or_404(PinSite, slug=pinsite)
        page, posts = self.post_list(request, pinsite_data)
        return render(
            request,
            self.template_name,
            {
                'pinsite': pinsite_data,
                'page': page,
                'posts': posts
            }
        )


class BlogEntryView(TemplateView):
    template_name = 'ffc/blog_entry.html'

    def get(self, request, pinsite, blog_entry_slug):
        blog_entry_data = get_object_or_404(
            PinSite.objects.get(slug=pinsite).blogentry_set,
            slug=blog_entry_slug
        )
        return render(
            request,
            self.template_name,
            {'blog_entry': blog_entry_data}
        )
