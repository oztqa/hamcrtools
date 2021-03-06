# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages


setup(
    name='hamcrtools',
    version_format='{tag}',
    setup_requires=['setuptools-git-version'],
    url='https://github.com/oztqa/hamcrtools',
    packages=find_packages(include=('hamcrtools',)),
    description='Extension for hamcrest library',
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'pyhamcrest',
        'jsonschema',
        'requests',
    ],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Natural Language :: Russian',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
    ),
)
