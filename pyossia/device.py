#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
A Device is the root of the hieracrchical tree.
A device might have Parameters attached to.
"""

import ossia_python as ossia


class Device(object):
	"""
	This
	"""
	def __init__(self, name):
		super(Device, self).__init__()
		# create the OSSIA Device with the name provided

	def __new__(self, name):
		my_device = ossia.LocalDevice(name)
		return my_device