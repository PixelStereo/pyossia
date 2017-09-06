#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is an example of a device
with I/O communication provided by libossia
"""


from pyossia import *

# create the OSSIA Device with the name provided
# here for test purpose
my_device = ossia.LocalDevice('PyOssia Device')
my_device.expose(protocol='oscquery', udp_port=3456, ws_port=5678)
my_int = my_device.add_param('test/value/int', value_type='int', default=66, domain=[-100, 100])
my_float = my_device.add_param('test/value/float', value_type='float', default=0.123456789, domain=[-2, 2])
my_bool = my_device.add_param('test/value/bool', value_type='bool', default=True)
my_string = my_device.add_param('test/value/string', value_type='string', default='Hello world !', domain=['once', 'loop', 'ping-pong'])
my_vec3f = my_device.add_param('test/value/vec3f', value_type='vec3f', default=(0, 0.57, 0.81))
my_list = my_device.add_param('test/value/list', value_type='list', default=[44100, "my_track.wav", 0.6])
my_char = my_device.add_param('test/value/char', value_type='char', default=chr(97))

print('---PARAMETERS---')
for param in my_device.get_parameters():
	print(param)
print('---NODES---')
for node in my_device.get_nodes():
	print(node)

from time import sleep
while True:
	pass
