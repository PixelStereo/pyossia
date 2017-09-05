#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
pyossia module will add usefull access for end users to C++ binded objects of libossia
"""

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
__release__ = __version__

# Import libossia python bindings
from pyossia import ossia_python as ossia

######################################################
# Module Constants
######################################################

# create a list of devices
# access to __devices__ must be done only by using
# add_device and pyossia.devices() (todo : add remove_device)

__devices__ = {'local':[], 'mirror':[]}

# create a list of value_types available in OSSIA
# maybe this is not necessary, just because 8'm a bit lazy
value_types = {	'float':ossia.ValueType.Float,
				'int':ossia.ValueType.Int,
				'bool':ossia.ValueType.Bool,
				'string':ossia.ValueType.String,
				'impulse':ossia.ValueType.Impulse,
				'list':ossia.ValueType.List,
				'vec3f':ossia.ValueType.Vec3f,
			}

######################################################
# Module functions / shortcuts to access libossia
######################################################

def add_device(name, **kwargs):
	"""
	create a node and make a create_parameter on the node
	"""
	# TODO :  raise an exception if mode is not provided as kwargs
	mode = kwargs['mode']
	if mode == 'local':
		device = ossia.LocalDevice(name)
	elif mode == 'mirror':
		target = kwargs['target']
		udp_port = kwargs['udp_port']
		device = ossia.OSCQueryDevice(name, target, udp_port)
	else:
		print(mode + ' is not implemented')
	__devices__[mode].append(device)
	return device

def devices(device_type='local'):
	# return a list of device
	return __devices__[device_type]

######################################################
# Following functions will be add to libossia bindings
######################################################

def add_param(self, name, **kwargs):
	"""
	create a node and make a create_parameter on the node
	"""
	node = self.add_node(name)
	value_type = kwargs['value_type']
	param = node.create_parameter(value_types[value_type])
	#print('todo : ' + str(kwargs))
	return param

def expose(self, protocol='oscquery', udp_port=3456, ws_port=5678):
	"""
	expose the device to the given <protocol>
	"""
	if protocol == 'oscquery':
		self.create_oscquery_server(udp_port, ws_port)
	else:
		print('ossia warning : ' + protocol + ' is not implemented')

def get_nodes(self, node=None, depth=0):
	"""
	return a list of all nodes attached to the given <node>
	<depth> argument allows a depth-specific list
	depth=0 means explore all the three
	depth=1 means explore only the first level
	(only the children of the given <node>)
	TODO : make depth levels in the code / it does not work for the moment
	"""
	if not node:
		node = self.root_node
	# create an empty list to return
	children = []
	# counter is used to follow depth-leveled exploration
	counter = 0
	# a function to iterate on node's tree recursively
	def iterate_on_children(node, counter):
		"""
		recursive exploration of the tree
		"""
		for child in node.children():
			# add the child to the children list to return
			children.append(child)
			# check the required depth
			if depth == counter:
				break
			# do the same for each child
			counter += 1
			iterate_on_children(child, counter)
	# do the research
	iterate_on_children(node, counter)
	# return the filled list
	return children

def get_params(self, node=None):
	"""
	return a list of all params for the device
	"""
	if not node:
		node = self.root_node
	children = []
	# a function to iterate on node's tree recursively
	def iterate_on_children(node):
		# check if there is children
		for child in node.children():
			# if the node is a param, it has an parameter
			if child.address.__class__.__name__ == 'Parameter':
				# add the child to the children list to return
				children.append(child)
			# do the same for each child
			iterate_on_children(child)
	# do the walk
	iterate_on_children(node)
	# return the filled list
	return children


def pull(self, callback):
	"""
	called when value changed
	"""
	self.add_callback(callback)

def push(self, value):
	"""
	called to ossia.parameter.push_value
	"""
	print(value)
	self.push_value(ossia.Value(value))

# customize a bit LocalDevice
# add a new_param /message / return method
# with kwargs as desired (optional)
ossia.LocalDevice.add_param = add_param
ossia.LocalDevice.expose = expose
ossia.LocalDevice.get_nodes = get_nodes
ossia.LocalDevice.get_params = get_params
ossia.Parameter.pull = pull
ossia.Parameter.push = push
