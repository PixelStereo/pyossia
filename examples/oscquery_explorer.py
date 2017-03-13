#! /usr/bin/env python
import sys, os
sys.path.append(os.path.abspath(".."))
import pyossia
import time

### REMOTE DEVICE SETUP
# a function to iterate on node's tree recursively
def iterate_on_children(node):

	for child in node.children():
		if child.get_address():
			print(str(child) + " " + str(child.get_address()))
		else:
			print(child)
		iterate_on_children(child)

def update():
	while not oscquery_device.update():
		pass
	iterate_on_children(oscquery_device.get_root_node())
try:
	oscquery_device = ossia.OSCQueryDevice("I'm a remote device", "ws://127.0.0.1:5678", 9998)

	print('here')
	# explore the remote device
	oscquery_device.update()
	print('---- UPDATE --- ', dir(oscquery_device))
	while True:
		time.sleep(0.2)
		update()
		

except:
	print("\nfail to connect to ws://10.0.1.83:5678\n")




	