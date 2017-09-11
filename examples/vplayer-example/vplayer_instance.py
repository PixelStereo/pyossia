#! /usr/bin/env python
# -*- coding: utf-8 -*-


# append pyossia path
import sys, os
sys.path.append(os.path.abspath("../.."))
from pyossia import *

from vplayer.player import VPlayer
from pyossia.functions import ossia_model

# create a device for this python program
ossia_device = ossia.LocalDevice("V Player")
# enable OSCQuery communication for our device
ossia_device.create_oscquery_server(3456, 5678)

# All the VPlayer instances will be created as a model of the ossia_device root
Vplayer = ossia_model(VPlayer, ossia_device)

# create an instance of a video player
vplayer = VPlayer()

# Just a test
from time import sleep
while True:
    pass
    vplayer.play_status = True
    print(vplayer.play_status)
    sleep(1)
    vplayer.play_status = False
    print(vplayer.play_status)
    sleep(1)
