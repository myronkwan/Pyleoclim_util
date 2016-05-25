from setuptools import setup, find_packages
import os
import sys
import io

setup(
    name = 'Pyleoclim',
    packages = find_packages(),
    version = 0.1,
    license = 'GNU Public',
    description = 'A Python package for paleoclimate data analysis',
    long_description = open('README.md').read() if exists("README.md") else "",
    author = 'Deborah Khider',
    author_email = 'dkhider@gmail.com',
    url = 'https://github.com/LinkedEarth/Pyleoclim_util/Pyleoclim',
    download_url = 'https://github.com/LinkedEarth/Pyleoclim_util/Pyleoclim/tarball/0.1',
    keywords = ['Paleoclimate, Data Analysis'],
    classifiers = [],
)