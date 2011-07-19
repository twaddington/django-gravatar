from django import template

# Get template.Library instance
register = template.Library()

def gravatar_url(email, size, default, rating, secure):
    # ...
    pass

def gravatar_img(email, size, default, rating, secure):
    # ...
    pass

def gravatar(*args, **kwargs):
    # ...
    return gravatar_img(*args, **kwargs)
    

register.simple_tag(gravatar_url)
register.simple_tag(gravatar_img)

# Simple alias
register.simple_tag(gravatar)
