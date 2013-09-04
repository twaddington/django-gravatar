try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='django-gravatar2',
    version='1.1.3',
    description='Essential Gravatar support for Django. Features helper'
                ' methods, templatetags and a full test suite!',
    long_description=open('README.rst').read(),
    license=open('LICENSE').read(),
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
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Framework :: Django',
    ]
)
