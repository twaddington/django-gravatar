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
You can pip install the app directly from GitHub:

::

    $ pip install git+git://github.com/twaddington/django-gravatar.git#egg=DjangoGravatar

Alternatively, you can now install directly from PyPi!

::

    $ pip install django-gravatar2

Make sure you install `django-gravatar2 <http://pypi.python.org/pypi/django-gravatar2>`_ as
there are several other incompatible django-gravatar libraries available.

Add django_gravatar to your INSTALLED_APPS in settings.py:

::

    INSTALLED_APPS = (
        # ...
        'django_gravatar',
    )

Basic Usage
===========
Use in code:

::

    from django_gravatar.helpers import get_gravatar_url, has_gravatar

    url = get_gravatar_url('alice@example.com', size=150)
    gravatar_exists = has_gravatar('bob@example.com')

Use in templates:

::

    {% load gravatar %}

    {% gravatar_url user.email 150 %}
    # https://secure.gravatar.com/avatar/hash.jpg?size=150

    {% gravatar user.email 150 %}
    # <img class="gravatar" src="https://secure.gravatar.com/avatar/hash.jpg?size=150" width="150" height="150" alt="" />

    {% gravatar user.email 150 "user@example.com" %}
    # <img class="gravatar" src="https://secure.gravatar.com/avatar/hash.jpg?size=150" width="150" height="150" alt="user@example.com" />

Configuring
===========
The following options can be configured in your settings.py:

GRAVATAR_URL            # Gravatar base url. Defaults to 'http://www.gravatar.com/'

GRAVATAR_SECURE_URL     # Gravatar base secure https url. Defaults to 'https://secure.gravatar.com/'

GRAVATAR_DEFAULT_SIZE   # Gravatar size in pixels. Defaults to '80'

GRAVATAR_DEFAULT_IMAGE  # An image url or one of the following: 'mm', 'identicon', 'monsterid', 'wavatar', 'retro'. Defaults to 'mm'

GRAVATAR_DEFAULT_RATING # One of the following: 'g', 'pg', 'r', 'x'. Defaults to 'g'

GRAVATAR_DEFAULT_SECURE # True to use https by default, False for plain http. Defaults to True

Contributing
============
Feel free to `fork django-gravatar <https://github.com/twaddington/django-gravatar>`_
on GitHub! We'd love to see your pull requests. Please make sure you run
tests before submitting a patch.
