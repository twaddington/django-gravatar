import hashlib
import urllib

from django.conf import settings

GRAVATAR_URL = 'http://www.gravatar.com/'
GRAVATAR_SECURE_URL = 'https://secure.gravatar.com/'

# These options can be used to change the default image if no gravatar is found
GRAVATAR_DEFAULT_IMAGE_404 = '404'
GRAVATAR_DEFAULT_IMAGE_MYSTERY_MAN = 'mm'
GRAVATAR_DEFAULT_IMAGE_IDENTICON = 'identicon'
GRAVATAR_DEFAULT_IMAGE_MONSTER = 'monsterid'
GRAVATAR_DEFAULT_IMAGE_WAVATAR = 'wavatar'
GRAVATAR_DEFAULT_IMAGE_RETRO = 'retro'

# These options can be used to restrict gravatar content
GRAVATAR_RATING_G = 'g'
GRAVATAR_RATING_PG = 'pg'
GRAVATAR_RATING_R = 'r'
GRAVATAR_RATING_X = 'x'

# Get user defaults from settings.py
GRAVATAR_DEFAULT_SIZE = getattr(settings, 'GRAVATAR_DEFAULT_SIZE', 80)
GRAVATAR_DEFAULT_IMAGE = getattr(settings, 'GRAVATAR_DEFAULT_IMAGE',
        GRAVATAR_DEFAULT_IMAGE_MYSTERY_MAN)
GRAVATAR_DEFAULT_RATING = getattr(settings, 'GRAVATAR_DEFAULT_RATING',
        GRAVATAR_RATING_G)
GRAVATAR_DEFAULT_SECURE = getattr(settings, 'GRAVATAR_DEFAULT_SECURE', True)

def get_gravatar_url(email, size=GRAVATAR_DEFAULT_SIZE, default=GRAVATAR_DEFAULT_IMAGE,
        rating=GRAVATAR_DEFAULT_RATING, secure=GRAVATAR_DEFAULT_SECURE):
    """
    Builds a url to a gravatar from an email address.

    :param email: The email to fetch the gravatar for
    :param size: The size (in pixels) of the gravatar to fetch
    :param default: What type of default image to use if the gravatar does not exist
    :param rating: Used to filter the allowed gravatar ratings
    :param secure: If True use https, otherwise plain http
    """
    if secure:
        url_base = GRAVATAR_SECURE_URL
    else:
        url_base = GRAVATAR_URL

    # Calculate the email hash
    email_hash = hashlib.md5(email.strip().lower()).hexdigest()

    # Build querystring
    query_string = urllib.urlencode({
        's': str(size),
        'd': default,
        'r': rating,
    })

    # Build url
    url = '{base}avatar/{hash}.jpg?{qs}'.format(base=url_base,
            hash=email_hash, qs=query_string)

    return url

def has_gravatar(email):
    """
    Returns True if the user has a gravatar, False if otherwise
    """
    # Request a 404 response if the gravatar does not exist
    url = get_gravatar_url(email, default=GRAVATAR_DEFAULT_IMAGE_404)

    # Verify an OK response was received
    return 200 == urllib.urlopen(url).getcode()
