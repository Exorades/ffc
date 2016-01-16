import ipdb
from django import template
register = template.Library()


@register.filter(name='form_field_css')
def add_form_css_and_placeholder(field, placeholder):
    return field.as_widget(
        attrs={'class': 'form-control', 'placeholder': placeholder}
    )


@register.filter
def pdb(element):
    ipdb.set_trace()
    return element
