# -*- coding: utf-8 -*-

# dragdrop.py

import sys
from PyQt4 import QtGui, QtCore

class Button(QtGui.QPushButton):
	def __init__(self, title, parent):
		QtGui.QPushButton.__init__(self, title, parent)
		self.setAcceptDrops(True)

	def dragEnterEvent(self, event):
		if event.mimeData().hasFormat("text/plain"):
			event.accept()
		else:
			event.ignore()

	def dropEvent(self, event):
		self.setText(event.mimeData().text())


class DragDrop(QtGui.QDialog):
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self, parent)

		self.resize(280, 150)
		self.setWindowTitle("Simple Drag & Drop")

		edit = QtGui.QLineEdit("", self)
		edit.setDragEnabled(True)
		edit.move(30, 65)

		button = Button("button", self)
		button.move(170, 65)


		screen = QtGui.QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width()-size.width())/2,
			(screen.height()-size.height())/2)


app = QtGui.QApplication(sys.argv)
dd = DragDrop()
dd.show()
app.exec_()

