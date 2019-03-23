from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

with open('README.MD') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

version = {}
with open(os.path.join(_here, 'colorfulScraper', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name='colorful_scraper',
    version=version['__version__'],
    description=('Encycolorpedia to json color scraper.'),
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Dusan Radisavljevic',
    author_email='ducaradisavljevic@gmail.com',
    url='https://github.com/dradisavljevic/ColorfulScraper',
    license=license,
    packages=['colorfulScraper'],
    python_requires='>=3.6.0',
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.7.2'],
    )
