# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_oceandata.ui'
#
# Created: Wed Feb  4 17:45:52 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_OceanData(object):
    def setupUi(self, OceanData):
        OceanData.setObjectName(_fromUtf8("OceanData"))
        OceanData.resize(406, 516)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(OceanData.sizePolicy().hasHeightForWidth())
        OceanData.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(OceanData)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.plainTextEdit = QtGui.QPlainTextEdit(OceanData)
        self.plainTextEdit.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setMinimumSize(QtCore.QSize(0, 180))
        self.plainTextEdit.setBaseSize(QtCore.QSize(0, 0))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.gridLayout.addWidget(self.plainTextEdit, 7, 0, 1, 1)
        self.btnDownload = QtGui.QPushButton(OceanData)
        self.btnDownload.setEnabled(False)
        self.btnDownload.setObjectName(_fromUtf8("btnDownload"))
        self.gridLayout.addWidget(self.btnDownload, 8, 0, 1, 1)
        self.checkBoxCanvas = QtGui.QCheckBox(OceanData)
        self.checkBoxCanvas.setObjectName(_fromUtf8("checkBoxCanvas"))
        self.gridLayout.addWidget(self.checkBoxCanvas, 6, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtGui.QLabel(OceanData)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.txtPath = QtGui.QLineEdit(OceanData)
        self.txtPath.setEnabled(True)
        self.txtPath.setText(_fromUtf8(""))
        self.txtPath.setReadOnly(True)
        self.txtPath.setObjectName(_fromUtf8("txtPath"))
        self.horizontalLayout_4.addWidget(self.txtPath)
        self.toolButton = QtGui.QToolButton(OceanData)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout_4.addWidget(self.toolButton)
        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(OceanData)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBoxRes = QtGui.QComboBox(OceanData)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxRes.sizePolicy().hasHeightForWidth())
        self.comboBoxRes.setSizePolicy(sizePolicy)
        self.comboBoxRes.setObjectName(_fromUtf8("comboBoxRes"))
        self.horizontalLayout_3.addWidget(self.comboBoxRes)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(OceanData)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.startDate = QtGui.QDateEdit(OceanData)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startDate.sizePolicy().hasHeightForWidth())
        self.startDate.setSizePolicy(sizePolicy)
        self.startDate.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1752, 9, 14), QtCore.QTime(0, 0, 0)))
        self.startDate.setCalendarPopup(True)
        self.startDate.setDate(QtCore.QDate(1995, 1, 1))
        self.startDate.setObjectName(_fromUtf8("startDate"))
        self.horizontalLayout_2.addWidget(self.startDate)
        self.endDate = QtGui.QDateEdit(OceanData)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.endDate.sizePolicy().hasHeightForWidth())
        self.endDate.setSizePolicy(sizePolicy)
        self.endDate.setCalendarPopup(True)
        self.endDate.setDate(QtCore.QDate(2013, 12, 31))
        self.endDate.setObjectName(_fromUtf8("endDate"))
        self.horizontalLayout_2.addWidget(self.endDate)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_6 = QtGui.QLabel(OceanData)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.comboBoxTime = QtGui.QComboBox(OceanData)
        self.comboBoxTime.setObjectName(_fromUtf8("comboBoxTime"))
        self.comboBoxTime.addItem(_fromUtf8(""))
        self.comboBoxTime.addItem(_fromUtf8(""))
        self.comboBoxTime.addItem(_fromUtf8(""))
        self.comboBoxTime.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.comboBoxTime)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_4 = QtGui.QLabel(OceanData)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_5.addWidget(self.label_4)
        self.comboBoxDatasets = QtGui.QComboBox(OceanData)
        self.comboBoxDatasets.setEnabled(True)
        self.comboBoxDatasets.setObjectName(_fromUtf8("comboBoxDatasets"))
        self.comboBoxDatasets.addItem(_fromUtf8(""))
        self.comboBoxDatasets.setItemText(0, _fromUtf8(""))
        self.comboBoxDatasets.addItem(_fromUtf8(""))
        self.comboBoxDatasets.addItem(_fromUtf8(""))
        self.comboBoxDatasets.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.comboBoxDatasets)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(OceanData)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.retranslateUi(OceanData)
        QtCore.QObject.connect(self.btnDownload, QtCore.SIGNAL(_fromUtf8("clicked()")), OceanData.accept)
        QtCore.QObject.connect(self.toolButton, QtCore.SIGNAL(_fromUtf8("clicked()")), OceanData.open)
        QtCore.QObject.connect(self.comboBoxDatasets, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), OceanData.update)
        QtCore.QMetaObject.connectSlotsByName(OceanData)

    def retranslateUi(self, OceanData):
        OceanData.setWindowTitle(_translate("OceanData", "OceanData", None))
        self.plainTextEdit.setPlainText(_translate("OceanData", "For full details on datasets, please refer to http://oceancolor.gsfc.nasa.gov/\n"
"\n"
"", None))
        self.btnDownload.setText(_translate("OceanData", "Download", None))
        self.checkBoxCanvas.setText(_translate("OceanData", "Add to canvas", None))
        self.label.setText(_translate("OceanData", "Download to:", None))
        self.toolButton.setText(_translate("OceanData", "...", None))
        self.label_3.setText(_translate("OceanData", "Resolution:", None))
        self.label_2.setText(_translate("OceanData", "Date range:  ", None))
        self.startDate.setDisplayFormat(_translate("OceanData", "yyyy/MM/dd", None))
        self.endDate.setDisplayFormat(_translate("OceanData", "yyyy/MM/dd", None))
        self.label_6.setText(_translate("OceanData", "Time period:", None))
        self.comboBoxTime.setItemText(0, _translate("OceanData", "Annual", None))
        self.comboBoxTime.setItemText(1, _translate("OceanData", "Monthly", None))
        self.comboBoxTime.setItemText(2, _translate("OceanData", "8 day", None))
        self.comboBoxTime.setItemText(3, _translate("OceanData", "Daily", None))
        self.label_4.setText(_translate("OceanData", "Dataset:", None))
        self.comboBoxDatasets.setItemText(1, _translate("OceanData", "AQUA MODIS Chlorophyll Concentration", None))
        self.comboBoxDatasets.setItemText(2, _translate("OceanData", "SeaWiFS Chlorophyll Concentration", None))
        self.comboBoxDatasets.setItemText(3, _translate("OceanData", "AQUA MODIS Sea Surface Temperature", None))
        self.label_5.setText(_translate("OceanData", "NASA Oceancolor Downloader", None))

