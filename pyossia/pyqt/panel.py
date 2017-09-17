#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
A Panel is a Group of widget designed to add Parameter remotes
"""

from PyQt5.QtWidgets import QGroupBox, QVBoxLayout

# Import libossia python bindings
from pyossia import ossia_python as ossia
from pyossia.pyqt.remote import FloatUI, BoolUI, IntUI, StringUI, Vec2fUI, Vec3fUI, Vec4fUI


class Panel(QGroupBox):
    """
    A QGroupBox to put one or several remote inside
    """
    def __init__(self, *args, **kwargs):
        super(Panel, self).__init__()
        # create a layout for this groupbox (to attach widgets on)
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.device = None
        self.setLayout(self.layout)

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
        elif parameter.value_type == ossia.ValueType.Vec2f:
            remote = Vec2fUI(parameter)
        elif parameter.value_type == ossia.ValueType.Vec3f:
            remote = Vec3fUI(parameter)
        elif parameter.value_type == ossia.ValueType.Vec4f:
            remote = Vec4fUI(parameter)
        elif parameter.value_type == ossia.ValueType.List:
            remote = ListUI(parameter)
        elif parameter.value_type == ossia.ValueType.Char:
            remote = CharUI(parameter)
        else:
            print('ERROR 999', parameter.value_type)
            remote = StringUI(parameter)
        self.layout.addWidget(remote)
        return remote
