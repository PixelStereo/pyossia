#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
This will load the .so file compiled from ossia-python.cpp in libossia
"""

def __bootstrap__():
    global __bootstrap__, __loader__, __file__
    import sys, pkg_resources, imp
    if sys.version_info < (3, 0):
        __file__ = pkg_resources.resource_filename(__name__,'ossia_python.so')
    else:
        __file__ = pkg_resources.resource_filename(__name__,'ossia_python.cpython-36m-darwin.so')
        print(__file__)
    __loader__ = None; del __bootstrap__, __loader__
    imp.load_dynamic(__name__,__file__)
__bootstrap__()
