#!/usr/bin/env python

from setuptools import setup

setup(
    name='quill-delta',
    version='1.0',
    description='Python port of the Quill-JS Delta library',
    author='Brantley Harris',
    author_email='deadwisdom@gmail.com',
    packages=['delta'],
    license="MIT License",
    install_requires=['diff-match-patch'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'mock'],   
)

