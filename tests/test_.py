#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os, sys

sys.path.append(os.path.abspath(".."))
from pyossia import __version__


class TestAll(unittest.TestCase):

    def test_version(self):
        self.assertEqual(__version__, __version__)
        print(__version__)


if __name__ == "__main__":
    unittest.main()
