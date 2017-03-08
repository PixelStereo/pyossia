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
		self.root_item = QStandardItem(str(root))

		self.iterate_children(root, self.root_item)

	def iterate_children(self, node, parent):
		"""
		recursive method to explore children until the end
		"""
		for nod in node.children():
			child = QStandardItem(str(nod).split('/')[-1])
			parent.appendRow(child)
			self.iterate_children(nod, child)
		self.appendRow(self.root_item)

	


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    import json
    from pprint import pprint
    root = my_device.get_root_node()
    model = TreeModel(root)
    view = QTreeView()
    view.setModel(model)
    view.expandAll()
    view.setWindowTitle("OSCQuery Explorer")
    view.show()
    sys.exit(app.exec_())
