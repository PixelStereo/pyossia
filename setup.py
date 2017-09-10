#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
setup for the pyossia project
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages, Extension
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get current version
import versioneer
__version__ = versioneer.get_version()


import os
import re
import sys
import platform
import subprocess

from setuptools.command.build_ext import build_ext


class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=''):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)

class CMakeBuild(build_ext):
    def run(self):
        try:
            out = subprocess.check_output(['cmake', '--version'])
        except OSError:
            raise RuntimeError("CMake must be installed to build the following extensions: " +
                               ", ".join(e.name for e in self.extensions))

        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        cmake_args = ['-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + extdir,
                      '-DPYTHON_EXECUTABLE=' + sys.executable, 
                      '-DOSSIA_PD=0',
                      '-DOSSIA_Qt=0',
                      '-DOSSIA_C=0',]

        cfg = 'Debug' if self.debug else 'Release'
        build_args = ['--config', cfg]

        if platform.system() == "Windows":
            cmake_args += ['-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{}={}'.format(cfg.upper(), extdir)]
            if sys.maxsize > 2**32:
                cmake_args += ['-A', 'x64']
            build_args += ['--', '/m']
        else:
            cmake_args += ['-DCMAKE_BUILD_TYPE=' + cfg]
            build_args += ['--', '-j16', ]

        env = os.environ.copy()
        env['CXXFLAGS'] = '{} -DVERSION_INFO=\\"{}\\"'.format(env.get('CXXFLAGS', ''),
                                                              self.distribution.get_version())
        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)
        print(['cmake', ext.sourcedir] + cmake_args)
        subprocess.check_call(['cmake', ext.sourcedir] + cmake_args, cwd=self.build_temp)
        subprocess.check_call(['cmake', '--build', '.'] + build_args, cwd=self.build_temp)

from setuptools.command.install import install as _install
from setuptools.command.develop import develop as _develop


def _post_install(dir):
    from shutil import move as movefile
    if sys.version_info < (3, 0):
    	movefile('/usr/local/lib/ossia_python.so', here+'/pyossia/ossia_python.so' )
    else:
    	movefile('/usr/local/lib/ossia_python.cpython-36m-darwin.so', here+'/pyossia/ossia_python.cpython-36m-darwin.so' )

class install(_install):
    def run(self):
        _install.run(self)
        self.execute(_post_install, (self.install_lib,),
                          msg="Running post install task")

class develop(_develop):
    def run(self):
        _develop.run(self)
        self.execute(_post_install, (self.install_lib,),
                          msg="Running post install task")
setup(
  name = 'pyossia',
  version=__version__,
  description = 'libossia usefull Classes',
  long_description=long_description,
  url='https://github.com/PixelStereo/pyossia',
  author = 'Pixel Stereo',
  license='GPLv3+',
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
    ],
  keywords='sample setuptools development',
  # You can just specify the packages manually here if your project is
  # simple. Or you can use find_packages().
  packages=find_packages(exclude=['3rdParty', 'examples', 'docs', 'tests']),
  # useless ?? package_data={'ossia_python': ['ossia_python/*']},
  install_requires=['zeroconf', 'pybind11>=1.7'],
  extras_require={
    'test': ['coverage']
    },
  download_url = 'https://github.com/PixelStereo/pyossia/tarball/' + __version__,
  ext_package='/usr/local/lib',
  ext_modules=[CMakeExtension('ossia_python', sourcedir='./3rdParty/libossia')],
  cmdclass={
    'build_ext': CMakeBuild,
    'install': install,
    'develop': develop,
  	},
  zip_safe=False,
)
