#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='multy',
    version='1.0.1',
    description='Easily implement bulk insert and ON DUPLICATE KEY UPDATEstatements with MySQL and MariaDB',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hashimura-suguru/multy_py',
    author='hashimura suguru',
    author_email='sugurudesu515@gmail.com',
    license='MIT',
    keywords='MariaDB, MySQL, Bulk, Multiple, Query',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
)