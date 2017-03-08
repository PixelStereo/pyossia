#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
from time import sleep
sys.path.append(os.path.abspath(".."))
print(sys.version)
from pyossia import my_device

from PyQt5.QtCore import QAbstractItemModel, QFile, QIODevice, QModelIndex, Qt
from PyQt5.QtWidgets import QApplication, QTreeView
from PyQt5.QtGui import QStandardItemModel, QStandardItem 

"""view = QTreeView()
view.setSelectionBehavior(QAbstractItemView.SelectRows)
model = QStandardItemModel()
model.setHorizontalHeaderLabels(['col1', 'col2', 'col3'])
view.setModel(model)
view.setUniformRowHeights(True)
"""
class TreeModel(QStandardItemModel):
	"""
	docstring for TreeModel
	"""
	def __init__(self, root):
		super(TreeModel, self).__init__()
		self.root = root
		root_item = QStandardItem(str(root))
		nodes = root.children()
		for node in nodes:
			child = QStandardItem(str(node))
			if node.get_address():
				print('param : ' + str(node))
			else:
				print('node : ' + str(node))
			root_item.appendRow(child)
			children = node.children()
			for ch in children:
				chi = QStandardItem(str(ch))
				child.appendRow(chi)
			self.appendRow(root_item)

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    import json
    from pprint import pprint
    with open('device.device') as data_file:    
    	data = json.load(data_file)
    	data = data['Children']
    	pprint(data)
    root = my_device.get_root_node()
    model = TreeModel(root)
    view = QTreeView()
    view.setModel(model)
    view.setWindowTitle("OSCQuery Explorer")
    view.show()
    sys.exit(app.exec_())
