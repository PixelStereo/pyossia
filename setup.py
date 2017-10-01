#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
setup for the pyossia project
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
import subprocess
from distutils.command.build import build as _build
here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get current version
import versioneer
__version__ = versioneer.get_version()

import platform
if platform.system() == 'Linux':
    file = 'ossia-python-3.6-linux_x86_64.tar.gz'
    url = 'https://github.com/OSSIA/libossia/releases/download/deploy_test-06/' + file
elif platform.system() == 'Darwin':
    file = 'ossia-python-3.6-osx.tar.gz'
    url = 'https://github.com/OSSIA/libossia/releases/download/deploy_test-06/' + file

class build(_build):
    """
    A build command class that will be invoked during package install.
    """
    sub_commands = _build.sub_commands + [('CustomCommands', None)]

CUSTOM_COMMANDS = [
    ['wget', url],
    ['tar', 'xzf', file],
    ['ls'],
    ['cp', 'ossia_python.so', 'build/lib/pyossia/'],
    ['mv', 'ossia_python.so', 'pyossia/'],
    ['rm', 'ossia-python-3.6-osx.tar.gz']
    ]

class CustomCommands(setuptools.Command):
    """A setuptools Command class able to run arbitrary commands."""

    def initialize_options(self):
        print()
        print('INIT')
        print()

    def finalize_options(self):
        print()
        print('END')
        print()

    def RunCustomCommand(self, command_list):
        print('-------> Running command: %s' % command_list)
        p = subprocess.Popen(
            command_list,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # Can use communicate(input='y\n'.encode()) if the command run requires
        # some confirmation.
        stdout_data, _ = p.communicate()
        print('Command output: %s' % stdout_data)
        if p.returncode != 0:
            raise RuntimeError(
                'Command %s failed: exit code: %s' % (command_list, p.returncode))

    def run(self):
        for command in CUSTOM_COMMANDS:
            self.RunCustomCommand(command)


setup(
    name = 'pyossia',
    version =__version__,
    description = 'libossia usefull Classes',
    long_description = long_description,
    url = 'https://github.com/PixelStereo/pyossia',
    author = 'Pixel Stereo',
    author_email = 'contact@pixelstereo.org',
    license ='GPLv3+',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords=['creative', 'controls', 'osc', 'oscquery', 'websocket', 'libossia'],
    packages = find_packages(),
    zip_safe=False,
    cmdclass={
        # Command class instantiated and run during pip install scenarios.
        'build': build,
        'CustomCommands': CustomCommands,
    }
)