# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup
from restfmclient.version import __version__


long_description = (
    open('README.rst').read() +
    '\n' +
    open('CHANGES.rst').read() +
    '\n'
)

setup(
    name='restfmclient',
    version=__version__,
    description="Python client library for RESTfm",
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
    ],
    keywords='Python Filemaker RestFM',
    author='René Jochum',
    author_email='rene.jochum@mariaebene.at',
    url='http://pypi.python.org/pypi/restfm',
    license='MIT',
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]
    ),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'setuptools',
        'aiohttp',
        'simplejson',
        'pytz',
    ]
)
