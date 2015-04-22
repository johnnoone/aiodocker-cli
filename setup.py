#!/usr/bin/env python

from setuptools import setup

with open('README.rst') as file:
    content = file.read()

setup(
    name='aiodocker.cli',
    version='0.1',
    description='Expose aiodocker to cli',
    long_description=content,
    author='Xavier Barbosa',
    author_email='clint.northwood@gmail.com',
    url='https://github.com/johnnoone/aiodocker-cli',
    packages=[
        'aiodocker.cli'
    ],
    keywords=[
        'infrastructure',
        'asyncio',
        'container'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: System :: Clustering',
    ],
    install_requires=[
        'aiodocker>=0.1',
        'cliff>=1.12.0'
    ],
    entry_points={
        'console_scripts': [
            'aiodocker = aiodocker.cli:main'
        ],
    },
)
