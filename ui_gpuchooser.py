# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gpuchooser.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(651, 341)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mainvertlayout = QtWidgets.QVBoxLayout()
        self.mainvertlayout.setObjectName("mainvertlayout")
        self.verticalLayout_2.addLayout(self.mainvertlayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addentrybtn = QtWidgets.QPushButton(self.centralwidget)
        self.addentrybtn.setObjectName("addentrybtn")
        self.horizontalLayout.addWidget(self.addentrybtn)
        self.removebtn = QtWidgets.QPushButton(self.centralwidget)
        self.removebtn.setObjectName("removebtn")
        self.horizontalLayout.addWidget(self.removebtn)
        self.savebtn = QtWidgets.QPushButton(self.centralwidget)
        self.savebtn.setObjectName("savebtn")
        self.horizontalLayout.addWidget(self.savebtn)
        self.cancelbtn = QtWidgets.QPushButton(self.centralwidget)
        self.cancelbtn.setObjectName("cancelbtn")
        self.horizontalLayout.addWidget(self.cancelbtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 651, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PRIME GPU Chooser"))
        self.addentrybtn.setText(_translate("MainWindow", "Add New Entry"))
        self.removebtn.setText(_translate("MainWindow", "Remove Selected Entries"))
        self.savebtn.setText(_translate("MainWindow", "Save"))
        self.cancelbtn.setText(_translate("MainWindow", "Exit (don\'t forget to save)"))

