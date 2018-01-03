# -*- coding: utf-8 -*-

# calendar.py

import sys
from PyQt4 import QtGui, QtCore


class Calendar(QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)

		self.setGeometry(300, 300, 350, 300)
		self.setWindowTitle("Calendar")

		self.cal = QtGui.QCalendarWidget(self)
		self.cal.setGridVisible(True)
		self.cal.move(20, 20)
		self.connect(self.cal, QtCore.SIGNAL("selectionChanged()"), self.showDate)


		self.label = QtGui.QLabel(self)
		date = self.cal.selectedDate()
		self.label.setText(str(date.toPyDate()))
		self.label.move(130, 260)


	def showDate(self):
		date = self.cal.selectedDate()
		self.label.setText(str(date.toPyDate()))


app = QtGui.QApplication(sys.argv)
cl = Calendar()
cl.show()
app.exec_()
