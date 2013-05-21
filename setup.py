#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import rock

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

if sys.argv[-1] == 'test':
    os.system('python test/test_all.py')
    sys.exit()

required = ['PyPubSub>=3.1.2', 'fn>=0.2.12']
packages = ['rock']


setup(
    name='rock',
    version=rock.__version__,
    description='UI Automator for Android UIAutomator.',
    long_description=open('README.md').read() + '\n\n' +
                     open('HISTORY.md').read(),
    author='Xiaocong He',
    author_email='xiaocong@gmail.com',
    url='',
    packages=packages,
    package_data={'': ['LICENSE', 'NOTICE']},
    include_package_data=True,
    install_requires=required,
    license=open("LICENSE").read(),
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
    ),
)
