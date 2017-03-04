#! /usr/bin/env python
# -*- coding: utf-8 -*-




from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from pyossia.constants import __devices__
from pyossia.device import Device

def new_device(name=None, tags=None, version=None, author=None):
    """
    Create a new device
        :return node object if successful
        :return False if name is not valid (already exists or is not provided)
    """
    device = Device(name=name, tags=tags, version=version, author=author)
    if device:
        __devices__.append(device)
        return __devices__[-1]
    else:
        return False
