#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
pyossia-pyqt module add Graphical User Interface for libossia devices
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont


class AbstractValue(QGroupBox):
    """
    PyQt Widget that display label with parameter of the parameter
    float / int : QSlider + QSpinbox
    string : QLineEdit
    bool : QCheckBox
    todo : tuples : depend of the unit (color, spatial, etc…)
    """
    def __init__(self,  *args, **kwargs):
        super(AbstractValue, self).__init__()
        self.parameter = args[0]
        # Create label with parameter
        self.label = QLabel(str(self.parameter.node))
        self.label.setFixedSize(100, 20)
        self.label.setFont(QFont('Helvetica', 12, QFont.Light))
        # Create parameter layout
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.setFixedSize(300, 45)


class BoolUI(AbstractValue):
	"""
	docstring for BoolUI
	"""
	def __init__(self, *args, **kwargs):
		super(BoolUI, self).__init__(*args, **kwargs)
		self.value = QPushButton(str(self.parameter))
		self.value.setCheckable(True)
		self.layout.addWidget(self.value)
		self.value.toggled.connect(self.parameter.push)
		def parameter_pull(value):
			self.value.setChecked(value.get())
			self.value.setText(str(self.parameter))
		self.parameter.add_callback(parameter_pull)
		parameter_pull(self.parameter.clone_value())


class FloatUI(AbstractValue):
    """
    docstring for FloatUI
    """
    def __init__(self, *args, **kwargs):
        super(FloatUI, self).__init__(*args, **kwargs)
        self.value = QSlider(Qt.Horizontal, None)
        self.layout.addWidget(self.value)
        if self.parameter.have_domain():
            self.value.setRange(self.parameter.domain.min.get()*32768, self.parameter.domain.max.get()*32768)
        else:
            self.value.setRange(0, 32768)
        def parameter_push(value):
            value = float(value/32768)
            self.parameter.push(value)
        self.value.valueChanged.connect(parameter_push)
        def parameter_pull(value):
            value = value.get()*32768
            self.value.setValue(value)
        self.parameter.add_callback(parameter_pull)
        parameter_pull(self.parameter.clone_value())

class Vec3fUI(AbstractValue):
    """
    docstring for Vec3f
    """
    def __init__(self, *args, **kwargs):
        super(Vec3fUI, self).__init__(*args, **kwargs)
        self.value1 = QDial()
        self.value2 = QDial()
        self.value3 = QDial()
        self.value1.setValue(1)
        self.value2.setValue(1)
        self.value3.setValue(1)
        self.value1.setFixedSize(35, 35)
        self.value2.setFixedSize(35, 35)
        self.value3.setFixedSize(35, 35)
        self.value1.setRange(0, 32768)
        self.value2.setRange(0, 32768)
        self.value3.setRange(0, 32768)
        def parameter_push():
            self.parameter.push([self.value1.value()/32768, self.value2.value()/32768, self.value3.value()/32768])
        self.value1.valueChanged.connect(parameter_push)
        self.value2.valueChanged.connect(parameter_push)
        self.value3.valueChanged.connect(parameter_push)
        self.layout.addWidget(self.value1)
        self.layout.addWidget(self.value2)
        self.layout.addWidget(self.value3)
        def parameter_pull(value):
            value1 = value.get()[0]*32768
            value2 = value.get()[1]*32768
            value3 = value.get()[2]*32768
            self.value1.setValue(value1)
            self.value2.setValue(value2)
            self.value3.setValue(value3)
        self.parameter.add_callback(parameter_pull)
        parameter_pull(self.parameter.clone_value())


class IntUI(AbstractValue):
    """
    docstring for FloatUI
    """
    def __init__(self, *args, **kwargs):
        super(IntUI, self).__init__(*args, **kwargs)
        self.value = QSlider(Qt.Horizontal, None)
        self.layout.addWidget(self.value)
        if self.parameter.have_domain():
            self.value.setRange(self.parameter.domain.min.get(), self.parameter.domain.max.get())
        else:
            self.value.setRange(0, 100)
        self.value.valueChanged.connect(self.parameter.push)
        def parameter_pull(value):
            self.value.setValue(value.get())
        self.parameter.add_callback(parameter_pull)
        parameter_pull(self.parameter.clone_value())

class StringUI(AbstractValue):
    """
    docstring for StringUI
    """
    def __init__(self, *args, **kwargs):
        super(StringUI, self).__init__(*args, **kwargs)
        self.value = QLineEdit()
        self.value.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.layout.addWidget(self.value)
        if self.parameter.have_domain():
            print(self.parameter.domain.min)
        self.value.textEdited.connect(self.parameter.push)
        def parameter_pull(value):
            self.value.setText(str(value.get()))
        self.parameter.add_callback(parameter_pull)
        parameter_pull(self.parameter.clone_value())
