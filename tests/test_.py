#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os, sys

from pyossia import __version__, add_device

test_device = add_device('Ossia Test Device', mode='local', )
test_device.expose(protocol='oscquery', ws_port=56789, udp_port=3456)
test_remote_device = add_device('Ossia Test Remote', mode='mirror', target='http://127.0.0.1:5678', udp_port=3456)
my_int = test_device.add_param('/test/int', datatype='int', domain=[0, 100], clipmode='both', unique=True)
my_float = test_device.add_param('/test/float', datatype='float', domain=[0, 1], clipmode='low', unique=True)
my_string = test_device.add_param('/test/string', datatype='string', domain=['uno', 'dos', 'tres'], clipmode=None)
my_bool = test_device.add_param('/test/bool', datatype='bool')


def announcement(test):
    print(' ')
    print('---TESTING ' + test + ' -----')
    print(' ')

class TestAll(unittest.TestCase):

    def test_version(self):
        announcement(__version__)

    def test_device(self):
        self.assertEqual(test_device.__class__.__name__, 'LocalDevice')
        # QUESTION : How to test the name of the device? Next one is node, but it might be Ossia Test Device
        # self.assertEqual(test_device.get_root_node().get_address(), 'Ossia Test Device')
        self.assertEqual(len(test_device.get_root_node().children()), 1)
        self.assertEqual(len(test_device.get_nodes()), 1)
        self.assertEqual(len(test_device.get_params()), 4)



if __name__ == '__main__':
    unittest.main()
