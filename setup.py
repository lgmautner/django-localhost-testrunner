#!/usr/bin/env python

from setuptools import setup
from localhostrunner.version import __version__

setup(
    name = 'unittest-localhost',
    version = __version__,
    author = 'Max Mautner',
    author_email = 'max@leadgenius.com',
    description = 'unittest-based test runner that warns if a test makes network requests',
    license = 'MIT',
    platforms = ['Any'],
    keywords = [
        'unittest', 'localhost', 'network', 'testrunner'
    ],
    url = 'https://github.com/lgmautner/unittest-localhost/tree/master/',
    classifiers = [
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing'
    ],
    packages = ['localhostrunner', 'localhostrunner.djangotestrunner'],
    include_package_data = True,
    install_requires = [],
    test_suite = 'tests'
)
