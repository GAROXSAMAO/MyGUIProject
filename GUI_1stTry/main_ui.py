# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        Form.resize(400, 466)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(400, 300))
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.gridFrame_2 = QtWidgets.QFrame(parent=Form)
        self.gridFrame_2.setObjectName("gridFrame_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridFrame_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.line_2 = QtWidgets.QFrame(parent=self.gridFrame_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_5.addWidget(self.line_2, 1, 0, 1, 1)
        self.horizontalFrame = QtWidgets.QFrame(parent=self.gridFrame_2)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.horizontalFrame)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(-1)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #2d7035;\n"
"}\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_4.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.horizontalFrame)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(-1)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"    background-color: #F44336;  /* Merah awal */\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #EF9A9A;  /* Merah lebih terang saat hover */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #B71C1C;  /* Merah lebih gelap saat klik */\n"
"}\n"
"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_4.addWidget(self.pushButton_8)
        self.gridLayout_5.addWidget(self.horizontalFrame, 5, 0, 1, 1)
        self.line = QtWidgets.QFrame(parent=self.gridFrame_2)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_5.addWidget(self.line, 4, 0, 1, 1)
        self.horizontalFrame_2 = QtWidgets.QFrame(parent=self.gridFrame_2)
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.horizontalFrame_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_6.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.horizontalFrame_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_6.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.horizontalFrame_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_6.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.horizontalFrame_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_6.addWidget(self.pushButton_6)
        self.gridLayout_5.addWidget(self.horizontalFrame_2, 6, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridFrame_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalFrame_3 = QtWidgets.QFrame(parent=self.gridFrame_2)
        self.horizontalFrame_3.setObjectName("horizontalFrame_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalFrame_3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lcdCLock = QtWidgets.QLCDNumber(parent=self.horizontalFrame_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.lcdCLock.setFont(font)
        self.lcdCLock.setObjectName("lcdCLock")
        self.horizontalLayout_7.addWidget(self.lcdCLock)
        self.label_3 = QtWidgets.QLabel(parent=self.horizontalFrame_3)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3, 0, QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignBottom)
        self.gridLayout_5.addWidget(self.horizontalFrame_3, 8, 0, 1, 1)
        self.gridFrame = QtWidgets.QFrame(parent=self.gridFrame_2)
        self.gridFrame.setObjectName("gridFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.gridFrame)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(parent=self.gridFrame)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.gridLayout_5.addWidget(self.gridFrame, 2, 0, 2, 1)
        self.horizontalLayout_8.addWidget(self.gridFrame_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_7.setText(_translate("Form", "Browse Files"))
        self.pushButton_8.setText(_translate("Form", "GPT "))
        self.pushButton_3.setText(_translate("Form", "YouTube"))
        self.pushButton_4.setText(_translate("Form", "GitHub"))
        self.pushButton_5.setText(_translate("Form", "VS Code"))
        self.pushButton_6.setText(_translate("Form", "Python"))
        self.label.setText(_translate("Form", "Welcome !"))
        self.label_3.setText(_translate("Form", "RRR."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
