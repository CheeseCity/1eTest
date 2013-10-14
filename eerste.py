# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\relax\python\eerste.ui'
#
# Created: Mon Jun 17 15:03:35 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_s1(object):
    def setupUi(self, s1):
        s1.setObjectName(_fromUtf8("s1"))
        s1.resize(629, 497)
        self.buttonBox = QtGui.QDialogButtonBox(s1)
        self.buttonBox.setGeometry(QtCore.QRect(40, 450, 561, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.groupBox = QtGui.QGroupBox(s1)
        self.groupBox.setGeometry(QtCore.QRect(40, 20, 561, 411))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.btnLicense = QtGui.QPushButton(self.groupBox)
        self.btnLicense.setGeometry(QtCore.QRect(30, 30, 81, 21))
        self.btnLicense.setObjectName(_fromUtf8("btnLicense"))
        self.lblLicense = QtGui.QLabel(self.groupBox)
        self.lblLicense.setGeometry(QtCore.QRect(150, 30, 331, 20))
        self.lblLicense.setText(_fromUtf8(""))
        self.lblLicense.setObjectName(_fromUtf8("lblLicense"))
        self.btnSession = QtGui.QPushButton(self.groupBox)
        self.btnSession.setGeometry(QtCore.QRect(30, 70, 81, 23))
        self.btnSession.setObjectName(_fromUtf8("btnSession"))
        self.lblSession = QtGui.QLabel(self.groupBox)
        self.lblSession.setGeometry(QtCore.QRect(150, 70, 331, 16))
        self.lblSession.setText(_fromUtf8(""))
        self.lblSession.setObjectName(_fromUtf8("lblSession"))

        self.retranslateUi(s1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), s1.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), s1.reject)
        QtCore.QObject.connect(self.btnLicense, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lblLicense.clear)
        QtCore.QMetaObject.connectSlotsByName(s1)

    def retranslateUi(self, s1):
        s1.setWindowTitle(_translate("s1", "Dialog", None))
        self.groupBox.setTitle(_translate("s1", "Kadertje", None))
        self.btnLicense.setText(_translate("s1", "Licentie", None))
        self.btnSession.setText(_translate("s1", "Sessie", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    s1 = QtGui.QDialog()
    ui = Ui_s1()
    ui.setupUi(s1)
    s1.show()
    sys.exit(app.exec_())

