#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A setuptools based setup module.
See:
https://github.com/InversoGmbH/coding-dojo-py
"""

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='coding-dojo-py',
    version='2020.01',
    description='Repository der inverso GmbH für das monatliche Remote-CodingDojo in Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/InversoGmbH/coding-dojo-py',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
    ],
    keywords='coding-dojo kata python jython python3 python2',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3, <4',
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage', 'flake8'],
    }
)
