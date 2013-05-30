from setuptools import setup, find_packages
import testtrackpro

setup(
    name="testtrackpro",
    version=testtrackpro.__version_string__,
    description="",
    long_description=open('README.rst').read(),
    url="https://github.com/dougn/python-testtrackpro/",
    author=testtrackpro.__author__,
    author_email=testtrackpro.__email__,
    license="BSD",
    py_modules=['testtrackpro'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=['suds>=0.4',],
    keywords=["testtrack", "testtrackpro", "soap", "suds"],
)
