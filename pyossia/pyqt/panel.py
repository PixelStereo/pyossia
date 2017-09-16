#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
A Panel represents a bunch of parameters
It is designed to display instruments through remotes
"""

from PyQt5.QtWidgets import QGroupBox, QVBoxLayout


# Import libossia python bindings
from pyossia import ossia_python as ossia

from pyossia.pyqt.remote import FloatUI, BoolUI, IntUI, StringUI, Vec3fUI


######################################################
# Module functions / shortcuts to create pyossia GUI
######################################################


class Panel(QGroupBox):
    """
    PyQt Panel that display all params of a device
    float / int : QSlider + QSpiVBox
    string : QLineEdit
    bool : QCheckBox
    todo : tuples : depend of the unit (color, spatial, etc…)
    """
    def __init__(self, *args, **kwargs):
        super(Panel, self).__init__()
        # create a layout for this groupbox (to attach widgets on)
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.device = None
        self.setLayout(self.layout)
        self.setup(args, kwargs)
        self.resize(args, kwargs)

    def add_remote(self, parameter):
        """
        Add a QWidget for the current Value
        """
        if parameter.value_type == ossia.ValueType.Float:
            remote = FloatUI(parameter)
        elif parameter.value_type == ossia.ValueType.Bool:
            remote = BoolUI(parameter)
        elif parameter.value_type == ossia.ValueType.Int:
            remote = IntUI(parameter)
        elif parameter.value_type == ossia.ValueType.String:
            remote = StringUI(parameter)
        elif parameter.value_type == ossia.ValueType.Vec3f:
            remote = Vec3fUI(parameter)
        elif parameter.value_type == ossia.ValueType.List:
            remote = StringUI(parameter)
        elif parameter.value_type == ossia.ValueType.Char:
            remote = StringUI(parameter)
        return remote

    def setup(self, args, kwargs):
        """
        create a Remote for each parameter
        """
        if 'device' in kwargs.keys():
            self.device = kwargs['device']
            # set title for the panel
            self.setTitle(self.device.name)
            #self.setTitle(str(self.device.get_nodes()[0]))
            for child in self.device.get_parameters():
                remote = self.add_remote(child.parameter)
                self.layout.addWidget(remote)

    def resize(self, args, kwargs):
        """
        resize the Panel from its parameter size
        """
        # set width and height for this device/groupboxs
        if 'height' in kwargs.keys():
            if self.device:
                if kwargs['height'] == 'auto':
                    self.setFixedHeight(len(self.device.get_parameters()) * 49)
                else:
                    self.setFixedHeight(kwargs['height'])
        if 'height' in kwargs.keys():
            if self.device:
                if kwargs['width'] == 'auto':
                    self.setFixedWidth(305)
                else:
                    self.setFixedWidth(kwargs['width'])
