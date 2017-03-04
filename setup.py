#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup, Extension
import versioneer
import os, sys
sys.path.append(os.path.abspath('./pyossia'))
from _version import get_versions
__version__ = get_versions()['version']
del get_versions
__version__ = __version__.split('+')
__version__ = __version__[0]

setup(
  version=versioneer.get_version(),
  cmdclass=versioneer.get_cmdclass(),
  name = 'pyossia',
  packages = ['pyossia'],
  description = 'libossia usefull Classes',
  author = 'Pixel Stereo',
  url='https://github.com/PixelStereo/pyossia',
  download_url = 'https://github.com/PixelStereo/pyossia/tarball/' + __version__,
  ext_modules=[Extension("ossia-python", ["src/ossia-python.cpp"])],
  classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
