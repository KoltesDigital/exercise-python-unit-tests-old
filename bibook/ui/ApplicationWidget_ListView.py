# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bibook\ui\ApplicationWidget-ListView.ui',
# licensing of 'bibook\ui\ApplicationWidget-ListView.ui' applies.
#
# Created: Fri Jun 14 19:37:28 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ApplicationWidget(object):
    def setupUi(self, ApplicationWidget):
        ApplicationWidget.setObjectName("ApplicationWidget")
        ApplicationWidget.resize(419, 258)
        self.verticalLayout = QtWidgets.QVBoxLayout(ApplicationWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bookListView = QtWidgets.QListView(ApplicationWidget)
        self.bookListView.setObjectName("bookListView")
        self.verticalLayout.addWidget(self.bookListView)
        self.borrowBookButton = QtWidgets.QPushButton(ApplicationWidget)
        self.borrowBookButton.setObjectName("borrowBookButton")
        self.verticalLayout.addWidget(self.borrowBookButton)
        self.statusLabel = QtWidgets.QLabel(ApplicationWidget)
        self.statusLabel.setText("")
        self.statusLabel.setObjectName("statusLabel")
        self.verticalLayout.addWidget(self.statusLabel)

        self.retranslateUi(ApplicationWidget)
        QtCore.QMetaObject.connectSlotsByName(ApplicationWidget)

    def retranslateUi(self, ApplicationWidget):
        ApplicationWidget.setWindowTitle(QtWidgets.QApplication.translate("ApplicationWidget", "BiBook", None, -1))
        self.borrowBookButton.setText(QtWidgets.QApplication.translate("ApplicationWidget", "Borrow the book", None, -1))

