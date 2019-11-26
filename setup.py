from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.rst')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

version = {}
with open(os.path.join(_here, 'pysbdb', 'pysbdb.py')) as f:
    exec(f.read(), version)

setup(
    name='pysbdb',
    version=version['__0.1__'],
    description=('Quick query of NASA JPL Small Body Database.'),
    long_description=long_description,
    author='Siegfried Eggl',
    author_email='eggl@uw.edu',
    url='https://github.com/lsst-dm/pysbdb',
    license='GPL-3.0',
    packages=['pysbdb'],
#   dependencies
    install_requires=[
        'numpy',
        'requests'
    ],
#   no scripts e
#   scripts=['bin/a-script'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.6'],
    )
