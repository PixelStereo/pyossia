#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
from time import sleep
sys.path.append(os.path.abspath(".."))
from pyossia import __version__, new_device

print(__version__)

my_device = new_device('my test app')
my_device._localdevice.create_oscquery_server(3456, 5678)
test = my_device.new_parameter('test')
print(test)

while True:
	test = 1
	sleep(0.5)
	test = 0
	sleep(0.5)

quit()




props = [stuff for stuff in dir(my_device) if not stuff.startswith('__')]
print('-- methods')
for stuff in props:
	print('-- -- ' + stuff)

print('my_device', my_device)
print('add_node', my_device.add_node('lala'))
print('find_node', my_device.find_node('lala'))
print(my_device.find_node('lala'), type(my_device.find_node('lala')))
print('get_root_node', my_device.get_root_node())
print(my_device.get_root_node())

while True:
	pass
