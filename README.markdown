django-gravatar
================
A lightweight django-gravatar app. Includes helper methods for interacting with gravatars outside of template code.

Features
========
- Helper methods for constructing a gravatar url and checking an email for an existing gravatar
- Templatetags for generating a gravatar url or gravatar <img> tag.
- Full test suite!

Installing
==========
Add django_gravatar to your INSTALLED_APPS in settings.py:

    INSTALLED_APPS = (
        # ...
        'django_gravatar',
    )

Basic Usage
===========
Use in code:

    from django_gravatar.helpers import get_gravatar_url, has_gravatar
    
    url = get_gravatar_url('alice@example.com', size=150)
    gravatar_exists = has_gravatar('bob@example.com')

Use in templates:

    {% load gravatar %}

    {% gravatar_url user.email 150 %}
    # https://secure.gravatar.com/avatar/hash.jpg?size=150

    {% gravatar_img user.email 150 %}
    # <img class="gravatar" src="https://secure.gravatar.com/avatar/hash.jpg?size=150" width="150" height="150" alt="" />

Configuring
===========
The following options can be configured in your settings.py:

GRAVATAR_DEFAULT_SIZE   # Gravatar size in pixels. Defaults to '80'
GRAVATAR_DEFAULT_IMAGE  # An image url or one of the following: 'mm', 'identicon', 'monsterid', 'wavatar', 'retro'. Defaults to 'mm'
GRAVATAR_DEFAULT_RATING # One of the following: 'g', 'pg', 'r', 'x'. Defaults to 'g'
GRAVATAR_DEFAULT_SECURE # True to use https by default, False for plain http. Defaults to True

TODO
====
- Add support for local caching of gravatars
