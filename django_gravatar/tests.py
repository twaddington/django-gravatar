import urlparse
import urllib

from django.test import TestCase
from django.template import Context, Template

from django_gravatar.helpers import *

class TestGravatarHelperMethods(TestCase):
    def test_gravatar_url(self):
        """
        Verify that the gravatar_url method returns the expected output.
        """
        email = "joe@example.com"
        email_upper = "JOE@example.com"
        email_strip = "   JOE@example.com "

        # Construct the url
        url = get_gravatar_url(email)

        # Verify email is properly sanitized
        self.assertEqual(url, get_gravatar_url(email_upper))
        self.assertEqual(url, get_gravatar_url(email_strip))

        # Parse query string from url
        urlp = urlparse.urlparse(url)
        qs = urlparse.parse_qs(urlp.query)

        # Verify the correct query arguments are included with the proper defaults
        self.assertTrue(qs.has_key('s'))
        self.assertTrue(qs.has_key('d'))
        self.assertTrue(qs.has_key('r'))

        self.assertEquals(qs.get('s').pop(), str(GRAVATAR_DEFAULT_SIZE))
        self.assertEquals(qs.get('d').pop(), GRAVATAR_DEFAULT_IMAGE)
        self.assertEquals(qs.get('r').pop(), GRAVATAR_DEFAULT_RATING)

        # Verify the correct protocol is used
        if GRAVATAR_DEFAULT_SECURE:
            self.assertTrue(GRAVATAR_SECURE_URL in url)
        else:
            self.assertTrue(GRAVATAR_URL in url)

        # Verify that a url value for default is urlencoded
        default_url = 'https://www.example.com/default.jpg'
        url = get_gravatar_url(email, default=default_url)

        # Verify urlencoding
        self.assertTrue(urllib.quote_plus(default_url) in url)

    def test_has_gravatar(self):
        """
        Verify that the has_gravatar helper method correctly
        determines if a user has a gravatar or not.
        """
        bad_email = 'eve@example.com'
        good_email = 'matt@automattic.com'

        self.assertFalse(has_gravatar(bad_email))
        self.assertTrue(has_gravatar(good_email))


class TestGravatarTemplateTags(TestCase):
    def test_gravatar_url(self):
        email = 'matt@automattic.com'
        context = Context({'email': email})

        t = Template("{% load gravatar %}{% gravatar_url email %}")
        rendered = t.render(context)

        self.assertEqual(rendered, get_gravatar_url(email))

    def test_gravatar_img(self):
        # Some defaults for testing
        email = 'matt@automattic.com'
        alt_text = 'some alt text'
        css_class = 'gravatar-thumb'
        size = 250

        # Build context
        context = Context({
            'email': email,
            'size': size,
            'alt_text': alt_text,
            'css_class': css_class,
        })

        # Default behavior
        t = Template("{% load gravatar %}{% gravatar email %}")
        rendered = t.render(context)

        self.assertTrue(get_gravatar_url(email) in rendered)
        self.assertTrue('class="gravatar"' in rendered)
        self.assertTrue('alt=""' in rendered)

        t = Template("{% load gravatar %}{% gravatar email size alt_text css_class %}")
        rendered = t.render(context)

        self.assertTrue('width="%s"' % (size,) in rendered)
        self.assertTrue('height="%s"' % (size,) in rendered)
        self.assertTrue('alt="%s"' % (alt_text,) in rendered)
        self.assertTrue('class="%s"' % (css_class,) in rendered)
