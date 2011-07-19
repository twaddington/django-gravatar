from django import template

from django_gravatar.helpers import get_gravatar_url, has_gravatar as has_gravatar_helper, GRAVATAR_DEFAULT_SIZE

# Get template.Library instance
register = template.Library()

def gravatar_url(email, size=GRAVATAR_DEFAULT_SIZE):
    """ Builds a gravatar url from an email """
    return get_gravatar_url(email=email, size=size)

def gravatar(email, size=GRAVATAR_DEFAULT_SIZE, alt_text='', css_class='gravatar'):
    """ Builds an gravatar <img> tag from an email """
    url = get_gravatar_url(email=email, size=size)

    return '<img class="{css_class}" src="{src}" width="{width}" height="{height}" alt="{alt}" />'.format(\
        css_class=css_class, src=url, width=size, height=size, alt=alt_text)

register.simple_tag(gravatar_url)
register.simple_tag(gravatar)
