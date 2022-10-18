import hashlib

from django.conf import settings

from .compat import HTTPError, Request, URLError, urlencode, urlopen

# This option controls whether a file extension is included
GRAVATAR_FORCE_EXTENSION = getattr(settings, "GRAVATAR_FORCE_EXTENSION", False)

# These options can be used to change the default image if no gravatar is found
GRAVATAR_DEFAULT_IMAGE_404 = "404"
GRAVATAR_DEFAULT_IMAGE_MYSTERY_MAN = "mm"
GRAVATAR_DEFAULT_IMAGE_IDENTICON = "identicon"
GRAVATAR_DEFAULT_IMAGE_MONSTER = "monsterid"
GRAVATAR_DEFAULT_IMAGE_WAVATAR = "wavatar"
GRAVATAR_DEFAULT_IMAGE_RETRO = "retro"

# These options can be used to restrict gravatar content
GRAVATAR_RATING_G = "g"
GRAVATAR_RATING_PG = "pg"
GRAVATAR_RATING_R = "r"
GRAVATAR_RATING_X = "x"

# Get Gravatar base url from settings.py
GRAVATAR_URL = getattr(settings, "GRAVATAR_URL", "http://www.gravatar.com/")
GRAVATAR_SECURE_URL = getattr(
    settings, "GRAVATAR_SECURE_URL", "https://secure.gravatar.com/"
)
GRAVATAR_AGNOSTIC_URL = getattr(
    settings, "GRAVATAR_AGNOSTIC_URL", "//www.gravatar.com/"
)

# Get user defaults from settings.py
GRAVATAR_DEFAULT_SIZE = getattr(settings, "GRAVATAR_DEFAULT_SIZE", 80)
GRAVATAR_DEFAULT_IMAGE = getattr(
    settings, "GRAVATAR_DEFAULT_IMAGE", GRAVATAR_DEFAULT_IMAGE_MYSTERY_MAN
)
GRAVATAR_DEFAULT_RATING = getattr(
    settings, "GRAVATAR_DEFAULT_RATING", GRAVATAR_RATING_G
)
GRAVATAR_DEFAULT_SECURE = getattr(settings, "GRAVATAR_DEFAULT_SECURE", None)


def calculate_gravatar_hash(email):
    # Calculate the email hash
    if len(email.strip()) == 0:
        return "0000"
    enc_email = email.strip().lower().encode("utf-8")
    email_hash = hashlib.md5(enc_email).hexdigest()
    return email_hash


def get_gravatar_url(
    email,
    size=GRAVATAR_DEFAULT_SIZE,
    extension: bool = GRAVATAR_FORCE_EXTENSION,
    default=GRAVATAR_DEFAULT_IMAGE,
    rating=GRAVATAR_DEFAULT_RATING,
    secure=GRAVATAR_DEFAULT_SECURE,
):
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
    elif secure is None:
        url_base = GRAVATAR_AGNOSTIC_URL
    else:
        url_base = GRAVATAR_URL

    # Calculate the email hash
    email_hash = calculate_gravatar_hash(email)

    # Build extension string
    if extension:
        extension_string = ".jpg"
    else:
        extension_string = ""

    # Build querystring
    query_string = urlencode(
        {
            "s": str(size),
            "d": default,
            "r": rating,
        }
    )

    # Build url
    url = f"{url_base}avatar/{email_hash}{extension_string}?{query_string}"

    return url


def has_gravatar(email):
    """
    Returns True if the user has a gravatar, False if otherwise
    """
    # Request a 404 response if the gravatar does not exist
    url = get_gravatar_url(email, default=GRAVATAR_DEFAULT_IMAGE_404)

    # Verify an OK response was received
    try:
        request = Request(url)
        request.get_method = lambda: "HEAD"
        return urlopen(request).code == 200
    except (HTTPError, URLError):
        return False


def get_gravatar_profile_url(email, secure=GRAVATAR_DEFAULT_SECURE):
    """
    Builds a url to a gravatar profile from an email address.

    :param email: The email to fetch the gravatar for
    :param secure: If True use https, otherwise plain http
    """
    if secure:
        url_base = GRAVATAR_SECURE_URL
    else:
        url_base = GRAVATAR_URL

    # Calculate the email hash
    email_hash = calculate_gravatar_hash(email)

    # Build url
    url = f"{url_base}{email_hash}"

    return url
