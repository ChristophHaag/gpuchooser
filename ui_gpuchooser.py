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
        MainWindow.resize(882, 341)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollarea = QtWidgets.QWidget()
        self.scrollarea.setGeometry(QtCore.QRect(0, 0, 866, 239))
        self.scrollarea.setObjectName("scrollarea")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollarea)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainvertlayout = QtWidgets.QVBoxLayout()
        self.mainvertlayout.setObjectName("mainvertlayout")
        self.verticalLayout.addLayout(self.mainvertlayout)
        self.scrollArea.setWidget(self.scrollarea)
        self.verticalLayout_2.addWidget(self.scrollArea)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 882, 27))
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

