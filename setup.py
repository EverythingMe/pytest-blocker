#!/usr/bin/env python

from setuptools import setup, find_packages
import os

__here__ = os.path.abspath(os.path.dirname(__file__))

# define __version__
# execfile doesn't exist in python 3
# see: http://stackoverflow.com/questions/6357361/alternative-to-execfile-in-python-3-2
exec(open(os.path.join(__here__, 'pytest_blocker', '__version__.py')).read())


setup(
    name='pytest-blocker',
    description='pytest plugin to mark a test as blocker and skip all other tests',
    version=__version__,
    author='EverythingMe',
    author_email='automation@everything.me',
    url='http://github.com/EverythingMe/pytest-blocker',
    packages=find_packages(),
    entry_points = {
        'pytest11': [
            'pytest_blocker = pytest_blocker',
        ]
    },
    install_requires=['pytest'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Quality Assurance',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
