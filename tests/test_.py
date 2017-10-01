#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
This ia a test for pyossia module, based on libossia python bindings
"""

import unittest

# import pyossia module
from pyossia import ossia
import pyossia


def announcement(test):
    """
    Simple function to print usefull graphic separator for the log
    """
    print(' ')
    print('---TESTING ' + test + ' -----')
    print(' ')

class TestAll(unittest.TestCase):
    """
    Main test, it will trigger all the tests
    """

    """
    # create the OSSIA Device with the name provided
    # here for test purpose
    """
    my_device = ossia.LocalDevice('PyOssia Test Device')
    my_device.expose(protocol='oscquery', listening_port=3456, sending_port=5678, logger=False)
    my_device.expose(protocol='osc', listening_port=9996, sending_port=9997, logger=False)
    my_int = my_device.add_param('test/value/int', value_type='int', default=66, domain=[-100, 100])
    my_float = my_device.add_param('test/value/float', value_type='float', default=0.123456789, domain=[-2, 2])
    my_bool = my_device.add_param('test/value/bool', value_type='bool', default=True)
    my_string = my_device.add_param('test/value/string', value_type='string', default='Hello world !', domain=['once', 'loop'])
    my_vec3f = my_device.add_param('test/value/vec3f', value_type='vec3f', default=(0, 0.57, 0.81),  domain=[0, 1])
    my_list = my_device.add_param('test/value/list', value_type='list', default=[44100, "my_track.wav", 0.6])
    my_char = my_device.add_param('test/value/char', value_type='char', default=chr(97))

    def test_version(self):
        """
        print the actual version of pyossia
        """
        announcement(pyossia.__version__)
        self.assertEqual(isinstance(pyossia.__version__, str), True)

    def test_float(self):
        """
        test a parameter @value_type float
        """
        self.assertEqual(self.my_float.value, 0.0)
        self.my_float.push_value(0.123456)
        self.assertAlmostEqual(self.my_float.value, 0.123456)

    def test_device(self):
        """
        test a device
        """
        # Test the class of the device
        self.assertEqual(self.my_device.__class__.__name__, 'LocalDevice')
        # Test the string representation of the device's root node
        self.assertEqual(str(self.my_device.root_node), '/')
        # Grab the name of the device
        self.assertEqual(self.my_device.name, 'PyOssia Test Device')
        # How many children this device have?
        self.assertEqual(len(self.my_device.root_node.children()), 1)
        # How many nodes are under this device?
        self.assertEqual(len(self.my_device.root_node.get_nodes()), 2)
        # How many parameters under this device?
        self.assertEqual(len(self.my_device.root_node.get_parameters()), 7)


if __name__ == '__main__':
    unittest.main()
