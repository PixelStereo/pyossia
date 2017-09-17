#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
All the Exceptions declared by the module are here
---
"""

class OssiaTypeError(Exception):
    """
    Waiting for an object of class 'expected', but received an object of class 'received'
    """
    def __init__(self, expected, received):
        super(OssiaTypeError, self).__init__()
        dbg = 'Wait for an {expected} instance object but receive a {received}'
        print(dbg.format(expected=expected, received=received.__class__))

class OssiaOutputError(Exception):
	"""
	There is no output in this project
	"""
	def __init__(self):
		super(OssiaOutputError, self).__init__()
