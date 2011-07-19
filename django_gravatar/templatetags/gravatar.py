from django import template

# Get template.Library instance
register = template.Library()

def gravatar_url(email, size):
    """ Builds a gravatar url from an email """
    # ...
    pass

def gravatar_img(email, size, default, rating, secure):
    """ Builds an gravatar <img> tag from an email """
    # ...
    pass

def gravatar(*args, **kwargs):
    """ Alias for gravatar_img """
    # ...
    return gravatar_img(*args, **kwargs)
    

register.simple_tag(gravatar_url)
register.simple_tag(gravatar_img)
register.simple_tag(gravatar)
