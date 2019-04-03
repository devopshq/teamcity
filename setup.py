# coding: utf-8

from setuptools import setup  # noqa: H301

from dohq_teamcity.version import __version__ as VERSION

NAME = "dohq-teamcity"
REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Python JetBrains TeamCity REST API library",
    license='MIT',
    author='Alexey Burov',
    author_email='allburov@gmail.com',
    url="https://github.com/devopshq/teamcity",
    keywords=["JetBrains", "TeamCity REST API", "DevOpsHQ"],
    install_requires=REQUIRES,
    packages=[
        'dohq_teamcity',
        'dohq_teamcity.api',
        'dohq_teamcity.custom',
        'dohq_teamcity.models',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
    ],
    include_package_data=True,
    long_description="""
    dohq_teamcity is a Python package providing access to the JetBrains TeamCity server API.

    You can see detailed user manual here: https://devopshq.github.io/teamcity
    """
)
