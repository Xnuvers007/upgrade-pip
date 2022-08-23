from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.3'
DESCRIPTION = 'upgrade packages pip outdated'
LONG_DESCRIPTION = 'A package that allows to upgrade all pip python outdated.'

# Setting up
setup(
    name="upgrade-pip",
    version=VERSION,
    author="Xnuvers007 (Indra Dwi A)",
    author_email="indra111.ida@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'pip', 'packages', 'update', 'outdated', 'internet','programmer','developer','upgrade','upgradepip','programming'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Natural Language :: English",
        "Natural Language :: Indonesian"
    ]
)

