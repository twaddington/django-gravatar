try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='django-gravatar2',
    version='1.4.0',
    description='Essential Gravatar support for Django. Features helper'
                ' methods, templatetags and a full test suite!',
    long_description=open('README.rst').read(),
    keywords='django gravatar avatar',
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
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
    ]
)
