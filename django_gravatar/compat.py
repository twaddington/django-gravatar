"""
This module provides compatibility with older versions of Django and Python
"""

try:
    from urllib.parse import urlparse, parse_qs, quote_plus, urlencode
except ImportError:     # Python 2
    from urlparse import urlparse, parse_qs
    from urllib import quote_plus, urlencode

try:
    from urllib.request import urlopen
except ImportError:     # Python 2
    from urllib import urlopen