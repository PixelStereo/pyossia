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
my_device.expose(listening_port=3456, sending_port=5678)
#my_device.expose(protocol='osc', listening_port=3456, sending_port=5678)
#my_device.expose(protocol='osc', listening_port=9997, sending_port=9997)
my_int = my_device.add_param('test/value/int', value_type='int', default_value=66, domain=[-100, 100])
my_float = my_device.add_param('test/value/float', value_type='float', default=0.123456789, domain=[-2, 2])
my_bool = my_device.add_param('test/value/bool', value_type='bool', default=True)
my_string = my_device.add_param('test/value/string', value_type='string', default='Hello world !', domain=['once', 'loop'])
my_vec3f = my_device.add_param('test/value/vec3f', value_type='vec3f', default=(0, 0.57, 0.81),  domain=[0, 1])
my_list = my_device.add_param('test/value/list', value_type='list', default=[44100, "my_track.wav", 0.6])
my_char = my_device.add_param('test/value/char', value_type='char', default=chr(97))

print('--- -LIST ALL NODES AND PARAMETERS- ---')
print()
for node in my_device.get_nodes():
    print('-- -NODE : ' + str(node))
    for child in node.children():
        if child.parameter:
            print('------ -parameter : ' + str(child) + ' : ' + str(child.parameter.clone_value().get()))
    print()
