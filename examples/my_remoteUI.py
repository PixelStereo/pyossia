#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is an example of a device
with I/O communication provided by libossia
"""


from pyossia import ossia, add_param
from pyossia.pyqt.panel import Panel
import sys
from PyQt5.Qt import QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QGridLayout, QGroupBox, QLabel, QListWidgetItem


# create the UI now
# this could be another app that control the Pyossia Test Device

class MainWindow(QMainWindow, QThread):
    """
    Main Window Doc String
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        # read a css for the whole MainWindow
        qss = open("style.qss", "r").read()
        self.setStyleSheet(qss)
        self.setAutoFillBackground(True)
        # create a layout for widgets
        self.gui = QGroupBox('osc query explorer')
        self.layout().addWidget(self.gui)
        self.gui_layout = QGridLayout()
        self.gui.setLayout(self.gui_layout)
        devices = QListWidget()
        try:
            device = ossia.OSCQueryDevice('my_device', 'ws://localhost:3456', 5678)
            devices.addItem('test device')
            device.update()
        except RuntimeError:
            print('no devices found on the network')
        panel = Panel('test device remote')
        if len(devices) > 0:
            devices.setCurrentRow(0)
            for node in device.get_parameters():
                panel.add_remote(node.parameter)
        self.gui_layout.addWidget(QLabel('devices found on the network'), 0, 0)
        self.gui_layout.addWidget(devices, 1, 0)
        self.gui_layout.addWidget(QLabel('device remote'), 0, 1)
        self.gui_layout.addWidget(panel, 1, 1)
        devices.currentItemChanged.connect(self.selection_changed)
        self.move(0, 40)
        self.setMinimumSize(self.gui.size())

    def selection_changed(self, truc):
        print('GO ---', truc.text(), type(truc))


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
