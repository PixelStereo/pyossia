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
my_device.expose(protocol='oscquery', listening_port=3456, sending_port=5678, logger=False)
my_device.expose(protocol='osc', listening_port=3456, sending_port=5678, logger=False)
my_int = my_device.add_param('test/numeric/int', value_type='int', default=66, domain=[-100, 100])
my_float = my_device.add_param('test/numeric/float', value_type='float', default=0.123456789, domain=[-2, 2])
my_vec2f = my_device.add_param('test/numeric/vec2f', value_type='vec2f', default=(-0.5, 0.5),  domain=[-0, 1])
my_vec3f = my_device.add_param('test/numeric/vec3f', value_type='vec3f', default=(0, 0, 0),  domain=[0, 360])
my_vec4f = my_device.add_param('test/numeric/vec4f', value_type='vec4f', default=(0, 0.57, 0.81, 0.7),  domain=[0, 1])
my_bool = my_device.add_param('test/value/bool', value_type='bool', default=True, repetitions_filter=True)
my_string = my_device.add_param('test/misc/string', value_type='string', default='Hello world !', domain=['once', 'loop'])
my_list = my_device.add_param('test/value/list', value_type='list', default=[44100, "my_track.wav", 0.6])
my_char = my_device.add_param('test/value/char', value_type='char', default=chr(97))


print('--- -LIST ALL NODES AND PARAMETERS- ---')
print(my_device.get_nodes())
for node in my_device.get_nodes():
    print('-- -NODE : ' + str(node))
    for child in node.children():
        if child.parameter:
            print('----', child.parameter)
            if child.parameter.value_type == ossia.ValueType.Vec3f:
                print(child.parameter.clone_value())
            else:
                pass
                print(child.parameter.clone_value())
            print('------ -parameter : ' + str(child) + ' : ' + str(child.parameter.clone_value()))
    print()
