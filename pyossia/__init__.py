#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Introduction
============
pyossia module will add usefull access for end users to C++ binded objects of libossia

It is currently broken, due to last changes in ossia_python.cpp binding file
that introduce some bugs related to get and set parameter values

Change log
==========
0.0.* aka the first
*******************
First version of pyossia, still in alpha develeopment.
Not available for now


pyossia usefull functions
=========================
"""


# Import libossia python bindings
# the ossia_python.so file must be in the pyossia module
from pyossia import ossia_python as ossia

# these few lines are used to get versionning from git
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
__release__ = __version__


######################################################
# Module Constants
######################################################

# create a list of devices
# access to __devices__ must be done only by using
# add_device and pyossia.devices() (todo : add remove_device)
__devices__ = {'local':[], 'mirror':[]}

# create a list of value_types available in OSSIA
# maybe this is not necessary, just because 8'm a bit lazy
__value_types__ = {'float':ossia.ValueType.Float,
                   'int':ossia.ValueType.Int,
                   'bool':ossia.ValueType.Bool,
                   'string':ossia.ValueType.String,
                   'impulse':ossia.ValueType.Impulse,
                   'list':ossia.ValueType.List,
                   'vec2f':ossia.ValueType.Vec2f,
                   'vec3f':ossia.ValueType.Vec3f,
                   'vec4f':ossia.ValueType.Vec4f,
                   'char':ossia.ValueType.Char,
                  }

######################################################
# Module functions / shortcuts to access libossia
######################################################

def add_device(name, **kwargs):
    """
    create a local device a node and make a create_parameter on the node
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
    """
    return a list of device
    """
    return __devices__[device_type]


def expose(self, protocol='oscquery', host='localhost', listening_port=3456, sending_port=5678, logger=False):
    """
    expose the device to the given <protocol>
    
    # TODO : Implement other protocol (serial, midi, osc, etc…)
    """
    if protocol == 'oscquery':
        self.create_oscquery_server(listening_port, sending_port, logger)
    elif protocol == 'osc':
        self.create_osc_server(host, listening_port, sending_port, logger)
    else:
        print('ossia warning : ' + protocol + ' is not implemented')

######################################################
# Following functions are here for conveniance over ossia_python bindings
# and might be add to libossia bindings later.
######################################################

def add_param(self, name, **kwargs):
    """
    create a node and make a create_parameter on the node
    """
    node = self.add_node(name)
    value_type = kwargs['value_type']
    param = node.create_parameter(__value_types__[value_type])
    if 'domain' in kwargs.keys():
        param.make_domain(kwargs['domain'][0], kwargs['domain'][1])
    # TODO : Checks kwargs and please set value as required
    # such as domain, clipmode, accessmode, default value etc…
    return param

def get_nodes(self, node=None, depth=0):
    """
    return a list of all nodes attached to the given <node>
    <depth> argument allows a depth-specific list
    depth=0 means explore all the three
    depth=1 means explore only the first level
    (only the children of the given <node>)
    TODO : make depth levels in the code / it does not work for the moment
    # check the required depth
    #counter += 1
    #if depth == counter and depth != 0:
    #    break
    """
    node = self.root_node
    if not node:
        node = self.root_node
    # create an empty list to return
    children = []
    # counter is used to follow depth-leveled exploration
    counter = 0
    # a function to iterate on node's tree recursively
    def iterate_nodes(node, counter):
        """
        recursive exploration of the tree
        """
        for child in node.children():
            # if the node is a param, it has an parameter
            if not child.parameter.__class__.__name__ == 'Parameter':
                # add the child to the children list to return
                children.append(child)
            # do the same for each child
            iterate_nodes(child, counter)
    # do the research
    iterate_nodes(node, counter)
    # return the filled list
    return children

def get_parameters(self, node=None):
    """
    return a list of all params for the device
    """
    if not node:
        node = self.root_node
    children = []
    # a function to iterate on node's tree recursively
    def iterate_parameters(node):
        """
    	recursive function to explore the whole three
    	"""
        # check if there is children
        for child in node.children():
            # if the node is a param, it has an parameter
            if child.parameter.__class__.__name__ == 'Parameter':
                # add the child to the children list to return
                children.append(child)
            # do the same for each child
            iterate_parameters(child)
    # do the walk
    iterate_parameters(node)
    # return the filled list
    return children


# customize a bit LocalDevice
# add a new_param /message / return method
# with kwargs as desired (optional)
ossia.LocalDevice.add_param = add_param
ossia.LocalDevice.expose = expose
ossia.LocalDevice.get_nodes = get_nodes
ossia.LocalDevice.get_parameters = get_parameters

ossia.OSCQueryDevice.expose = expose
ossia.OSCQueryDevice.get_nodes = get_nodes
ossia.OSCQueryDevice.get_parameters = get_parameters
