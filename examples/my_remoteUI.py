#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is an example of a device
with I/O communication provided by libossia
"""


from pyossia import ossia, add_param
from pyossia.pyqt.panel import Panel
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox



# create the OSSIA Device and some parameters
from my_device import my_device

# create the UI now
# this could be another app that control the Pyossia Test Device

class MainWindow(QMainWindow):
    """
    Main Window Doc String
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        # read a css for the whole MainWindow
        qss = open("style.qss", "r").read()
        self.setStyleSheet(qss)
        self.setAutoFillBackground(True)
        #self.setMinimumSize(self.panel.width() + 10, self.panel.height() + 10)
        self.move(0, 40)
        if self.centralWidget():
        	self.setFixedSize(self.centralWidget().width(), self.centralWidget().height())

        # Looking for oscquery devices on the network
        print('\nSCAN FOR OSC_QUERY DEVICES\n')
        devices = QComboBox()
        for data in ossia.list_oscquery_devices():
            devices.addItem(data.name)
            print(data.name + ": host = " + data.host + ", port = " + str(data.port))


class DeviceUI(object):
    """docstring for DeviceUI"""
    def __init__(self, arg):
        super(DeviceUI, self).__init__()
        self.arg = arg
        
        # Draw an UI for my_device
        self.panel = Panel(device=my_device, width='auto', height='auto')
        # assign this device to the mainwindow
        self.setCentralWidget(self.panel)





if __name__ == "__main__":
    # this is for python2 only
    try:
        reload(sys)
        sys.setdefaultencoding('utf8')
    except NameError:
        pass
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
