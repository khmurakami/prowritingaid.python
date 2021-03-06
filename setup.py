# coding: utf-8

"""
    ProWritingAid API V2

    Official ProWritingAid API Version 2

    OpenAPI spec version: v2
    Contact: hello@prowritingaid.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import sys
from setuptools import setup, find_packages

NAME = "ProWritingAidSDK"
VERSION = "2.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="ProWritingAid API V2",
    author_email="hello@prowritingaid.com",
    url="",
    keywords=["Swagger", "ProWritingAid API V2"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Official ProWritingAid API Version 2
    """
)
