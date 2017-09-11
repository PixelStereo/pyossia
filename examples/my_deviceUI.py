#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is an example of a device
with I/O communication provided by libossia with pyqt5 GUI
"""

from pyossia.pyqt.panel import Panel

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow


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
        # Draw an UI for my_device
        self.panel = Panel(device=my_device, width='auto', height='auto')
        # assign this device to the mainwindow
        self.setCentralWidget(self.panel)
        #self.setMinimumSize(self.panel.width() + 10, self.panel.height() + 10)
        self.move(0, 40)
        self.setFixedSize(self.centralWidget().width(), self.centralWidget().height())


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
