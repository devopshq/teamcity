# coding: utf-8

from setuptools import setup  # noqa: H301

NAME = "dohq-teamcity"
VERSION = "1.0.0"
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
    description="Python JetBrains TeamCity REST API library",
    author_email="",
    url="https://github.com/devopshq/teamcity",
    keywords=["JetBrains", "TeamCity REST API", "DevOpsHQ"],
    install_requires=REQUIRES,
    packages=[
        'dohq_teamcity',
        'dohq_teamcity.api',
        'dohq_teamcity.custom',
        'dohq_teamcity.models',
    ],
    include_package_data=True,
    package_data={
        '': [
            'dohq_teamcity/models/test.py',
        ]
    },
    long_description="""dohq_teamcity is a Python package providing access to the JetBrains TeamCity server API."""
)
