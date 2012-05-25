try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = open('README.rst')

setup(
    name='django-gravatar2',
    version='1.0.4',
    description='Essential Gravatar support for Django. Features helper methods, templatetags and a full test suite!',
    long_description=readme.read(),
    author='Tristan Waddington',
    author_email='tristan.waddington@gmail.com',
    url='https://github.com/twaddington/django-gravatar',
    packages=['django_gravatar', 'django_gravatar.templatetags'],
    classifiers=[
        'Development Status :: 5 - Production/Stable', # 4 Beta, 5 Production/Stable
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
