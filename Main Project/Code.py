print "Only basic code"
print "Code for further test..."

import sys
import os
from PyQt4 import QtCore, QtGui, uic

thisFolder = os.path.dirname(os.path.realpath(__file__))
uiName = "Ok_Test.ui"
uiPath = "%s\%s" %(thisFolder,uiName)

class Tester(QtGui.QWidget):
	
	def __init__(self,parent=None):
		QtGui.QMainWindow.__init__(self, parent=parent)
		uic.loadUi(uiPath, self)
		
		
def main():		
	app = QtGui.QApplication(sys.argv)
	widget = Tester()
	widget.show()

	sys.exit(app.exec_())

	
if __name__ == '__main__':
	main()