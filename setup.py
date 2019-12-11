from setuptools import setup

setup(
    name='pysbdb',
    version='1.0',
    description='Direct query of NASA JPL Small Body Database API.',
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
