#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
sys.path.append(os.path.abspath(".."))
from pyossia import __version__, new_device

print(__version__)

my_device = new_device('my test app')
print(my_device)