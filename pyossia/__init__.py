#! /usr/bin/env python
# -*- coding: utf-8 -*-

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
__release__ = __version__

from pyossia.constants import __devices__

# this is here fow now, to simplify development
# it creates a LocalDevice at pyossia import
import ossia_python as ossia

def add_param(self, name, datatype=ossia.ValueType.Float):
	"""
	create a node and make a create_address on the node
	"""
	node = self.add_node(name)
	param = node.create_address(datatype)
	return param

def expose(self, protocol='oscquery', udp_port=3456, ws_port=5678):
	if protocol == 'oscquery':
		self.create_oscquery_server(udp_port, ws_port)
	else:
		print('ossia warning : ' + protocol + ' is not implemented')

def get_nodes(self, node):
	children = []
	# a function to iterate on node's tree recursively
	def iterate_on_children(node):
		for child in node.children():
			children.append(child)
			iterate_on_children(child)
	iterate_on_children(node)
	return children

def get_params(self, node):
	children = []
	# a function to iterate on node's tree recursively
	def iterate_on_children(node):
		for child in node.children():
			if child.get_address():
				children.append(child)
			iterate_on_children(child)
	iterate_on_children(node)
	return children

# customize a bit LocalDevice
# add a new_param /message / return method
# with kwargs as desired (optional)
ossia.LocalDevice.add_param = add_param
ossia.LocalDevice.expose = expose
ossia.LocalDevice.get_nodes = get_nodes
ossia.LocalDevice.get_params = get_params
