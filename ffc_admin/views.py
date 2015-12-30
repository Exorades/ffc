from django.shortcuts import render
from django.views.generic import TemplateView

from ffc.models import Homepage, PinSite
from ffc_admin.forms import (
    CreateBlogEntryForm,
    CreatePinSiteForm,
    CreateUserForm,
    EditBlogEntryForm,
    EditHomepageForm,
)


class CreatePinSiteView(TemplateView):
    template_name = 'ffc_admin/site_create.html'

    def get(self, request):
        form = CreatePinSiteForm(initial={'author': request.user})
        return render(
            request,
            self.template_name,
            {'form': form}
        )

    def post(self, request):
        created = False
        form = CreatePinSiteForm(request.POST)
        if form.is_valid() and request.user.is_authenticated():
            data = form.cleaned_data
            site = PinSite.objects.create(
                name=data['name'],
                author=request.user
            )
            Homepage.objects.create(
                name='{} homepage'.format(site.name),
                subtitle=None,
                history=None,
                site=site
            )
            created = True

        return render(
            request, self.template_name, {'form': form, 'created': created}
        )


class EditHomepageView(TemplateView):
    template_name = 'ffc_admin/homepage_edit.html'

    def get(self, request):
        form = EditHomepageForm()
        return render(
            request, self.template_name, {'form': form}
        )

    def post(self, request):
        edited = False
        form = EditHomepageForm(request.POST)
        if form.is_valid() and request.user.is_authenticated():
            data = form.cleaned_data
            homepage = data['homepage']
            homepage.subtitle = data['subtitle']
            homepage.history = data['history']
            homepage.save()
            edited = True
        return render(
            request, self.template_name, {'form': form, 'edited': edited}
        )


class CreateUserView(TemplateView):
    template_name = 'ffc_admin/user_create.html'

    def get(self, request):
        form = CreateUserForm()
        return render(
            request, self.template_name, {'form': form}
        )

    def post(self, request):
        created = False
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            created = True
        return render(
            request, self.template_name, {'form': form, 'created': created}
        )


class CreateBlogEntryView(TemplateView):
    template_name = 'ffc_admin/create_blog_entry.html'

    def get(self, request):
        form = CreateBlogEntryForm(initial={'author': request.user})
        return render(
            request, self.template_name, {'form': form}
        )

    def post(self, request):
        created = False
        form = CreateBlogEntryForm(request.POST)
        if form.is_valid() and request.user.is_authenticated():
            form.save()
            created = True
        return render(
            request, self.template_name, {'form': form, 'created': created}
        )


class EditBlogEntryView(TemplateView):
    template_name = 'ffc_admin/edit_blog_entry.html'

    def get(self, request):
        form = EditBlogEntryForm()
        return render(
            request, self.template_name, {'form': form}
        )

    def post(self, request):
        edited = False
        form = EditBlogEntryForm(request.POST)
        if form.is_valid() and request.user.is_authenticated():
            data = form.cleaned_data
            blog_entry = data['blog_entry']
            blog_entry.subtitle = data['subtitle']
            blog_entry.body = data['body']
            blog_entry.save()
            edited = True
        return render(
            request, self.template_name, {'form': form, 'edited': edited}
        )

# class EditUserView(TemplateView):
#     template_name = 'ffc_admin/user_edit.html'

#     def get(self, request):
#         form = EditUserForm(instance=request.user)
#         return render(
#             request, self.template_name, {'form': form}
#         )

#     def post(self, request):
#         edited = False
#         form = EditUserForm(request.POST, instance=request.user)
#         if form.is_valid():
#             data = form.cleaned_data
#         return render(
#             request, self.template_name, {'form': form, 'edited': edited}
#         )
