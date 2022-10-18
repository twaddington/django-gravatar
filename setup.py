try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def description(file: str):
    with open(file) as f:
        rvalue = f.read()

    return rvalue


setup(
    name="django-gravatar2",
    version="2.0.0b",
    description="Essential Gravatar support for Django. Features helper"
    " methods, templatetags and a full test suite!",
    long_description=description("README.rst"),
    keywords="django gravatar avatar",
    license="MIT",
    author="Tristan Waddington",
    author_email="tristan.waddington@gmail.com",
    url="https://github.com/twaddington/django-gravatar",
    packages=["django_gravatar", "django_gravatar.templatetags"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",  # 4 Beta, 5 Production/Stable
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Framework :: Django",
    ],
)
