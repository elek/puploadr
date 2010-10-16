#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name = "puploadr",
    version = "0.2",
    packages = find_packages(),
    author = 'Elek, Marton',
    description = "Yet another flickr uploader script with resume capabilities",
    license = "GPL",
    install_requires = ['argparse','flickrapi','configobj','progressbar'],
    entry_points = {    
	'console_scripts': [
    	    'puploadr = puploadr.puploadr:main'
        ]
    }
)
