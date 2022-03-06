#!/usr/bin/env python

from setuptools import setup, Extension, find_packages
import os
import sys

setup(
    name='auturing',
    version='0.1.a',
    description="From an example of function definition, actually builds this function as a turing machine",
    long_description="Enter your project description here (long)",
    author='DELEVOYE Guillaume',
    author_email="delevoye.guillaume@gmail.com",
    packages=find_packages("."),
    url="https://github.com/GDelevoye/auturing",
    install_requires=[],
    package_data={'auturing': ['resources/*']},
    entry_points={'console_scripts': [
        "auturing = auturing.launchers.auturing_launcher:main",
    ]},
)
