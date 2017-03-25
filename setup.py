# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

setup(
    name="vania",
    version="0.1.0",
    description="A module to fairly distribute objects among targets considering weights.",
    license="MIT",
    author="Hackathonners",
    packages=find_packages(),
    install_requires=[
        'pulp',
    ],
    package_dir={'': '.'},
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
