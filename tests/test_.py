#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os, sys

# import pyossia module
import pyossia

# load my_device example, which contains one instance of each type of parameter
from examples.my_device import *


def announcement(test):
    print(' ')
    print('---TESTING ' + test + ' -----')
    print(' ')

class TestAll(unittest.TestCase):

    def test_version(self):
        announcement(pyossia.__version__)

    def test_float(self):
        self.assertEqual(my_float.value.get(), 0.0)
        my_float.push(0.123456)
        self.assertAlmostEqual(my_float.value.get_float(), 0.123456)

    def test_device(self):
        self.assertEqual(my_device.__class__.__name__, 'LocalDevice')
        # TODO : How to test the name of the device? Next one is node, but it might be Ossia Test Device
        # self.assertEqual(str(my_device.root_node), 'Python Test Device')
        self.assertEqual(len(my_device.root_node.children()), 1)
        self.assertEqual(len(my_device.get_nodes()), 2)
        self.assertEqual(len(my_device.get_parameters()), 7)



if __name__ == '__main__':
    unittest.main()
