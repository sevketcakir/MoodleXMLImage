# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MoodleXMLImage.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.openFileButton = QPushButton(self.centralwidget)
        self.openFileButton.setObjectName(u"openFileButton")

        self.verticalLayout.addWidget(self.openFileButton)

        self.exportButton = QPushButton(self.centralwidget)
        self.exportButton.setObjectName(u"exportButton")

        self.verticalLayout.addWidget(self.exportButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.quizView = QTreeWidget(self.tab)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.quizView.setHeaderItem(__qtreewidgetitem)
        self.quizView.setObjectName(u"quizView")

        self.gridLayout_2.addWidget(self.quizView, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.settingsCodeStyle = QComboBox(self.groupBox_2)
        self.settingsCodeStyle.setObjectName(u"settingsCodeStyle")

        self.gridLayout_5.addWidget(self.settingsCodeStyle, 0, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)

        self.settingsLineNumbers = QCheckBox(self.groupBox_2)
        self.settingsLineNumbers.setObjectName(u"settingsLineNumbers")
        self.settingsLineNumbers.setChecked(True)

        self.gridLayout_5.addWidget(self.settingsLineNumbers, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox = QGroupBox(self.tab_2)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 5, 0, 1, 1)

        self.settingsFontSize = QSpinBox(self.groupBox)
        self.settingsFontSize.setObjectName(u"settingsFontSize")
        self.settingsFontSize.setMinimum(4)
        self.settingsFontSize.setValue(16)

        self.gridLayout_4.addWidget(self.settingsFontSize, 1, 1, 1, 1)

        self.settingsTextColor = QLineEdit(self.groupBox)
        self.settingsTextColor.setObjectName(u"settingsTextColor")

        self.gridLayout_4.addWidget(self.settingsTextColor, 5, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)

        self.settingsBackgroundColor = QLineEdit(self.groupBox)
        self.settingsBackgroundColor.setObjectName(u"settingsBackgroundColor")

        self.gridLayout_4.addWidget(self.settingsBackgroundColor, 4, 1, 1, 1)

        self.settingsTextWidth = QSpinBox(self.groupBox)
        self.settingsTextWidth.setObjectName(u"settingsTextWidth")
        self.settingsTextWidth.setMinimum(20)
        self.settingsTextWidth.setMaximum(200)
        self.settingsTextWidth.setValue(50)

        self.gridLayout_4.addWidget(self.settingsTextWidth, 3, 1, 1, 1)

        self.settingsImageWidth = QSpinBox(self.groupBox)
        self.settingsImageWidth.setObjectName(u"settingsImageWidth")
        self.settingsImageWidth.setMinimum(400)
        self.settingsImageWidth.setMaximum(2000)
        self.settingsImageWidth.setValue(600)

        self.gridLayout_4.addWidget(self.settingsImageWidth, 2, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)

        self.settingsFontName = QComboBox(self.groupBox)
        self.settingsFontName.setObjectName(u"settingsFontName")
        self.settingsFontName.setEditable(True)

        self.gridLayout_4.addWidget(self.settingsFontName, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)

        self.previewSettingsButton = QPushButton(self.tab_2)
        self.previewSettingsButton.setObjectName(u"previewSettingsButton")

        self.gridLayout_3.addWidget(self.previewSettingsButton, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MoodleXMLImage", None))
        self.openFileButton.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.exportButton.setText(QCoreApplication.translate("MainWindow", u"Export Moodle XML", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Quiz View", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Code Settings", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Pygments Code Style", None))
        self.settingsLineNumbers.setText(QCoreApplication.translate("MainWindow", u"Line Numbers", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Text Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Font Name", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Text Color", None))
        self.settingsTextColor.setText(QCoreApplication.translate("MainWindow", u"white", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Text Width", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Background Color", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Image Width", None))
        self.settingsBackgroundColor.setText(QCoreApplication.translate("MainWindow", u"midnightblue", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Font Size", None))
        self.previewSettingsButton.setText(QCoreApplication.translate("MainWindow", u"Preview Settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

