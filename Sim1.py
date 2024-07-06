from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sim1(object):
    def setupUi(self, Sim1):
        Sim1.setObjectName("Sim1")
        Sim1.resize(500, 300)
        self.pushButton_2 = QtWidgets.QPushButton(Sim1)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 0, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 0, 127);")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Sim1)
        self.label.setGeometry(QtCore.QRect(30, 20, 431, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Sim1)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Sim1)
        self.label_3.setGeometry(QtCore.QRect(230, 80, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Sim1)
        self.label_4.setGeometry(QtCore.QRect(390, 80, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Sim1)
        self.pushButton.setGeometry(QtCore.QRect(150, 150, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Sim1)
        self.label_5.setGeometry(QtCore.QRect(200, 200, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(Sim1)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 240, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border-radius: 10;\n"
"border: 2px solid #505050;")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.widget = QtWidgets.QWidget(Sim1)
        self.widget.setGeometry(QtCore.QRect(20, 110, 446, 24))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-radius: 10;\n"
"border: 2px solid #505050;")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border-radius: 10;\n"
"border: 2px solid #505050;")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("border-radius: 10;\n"
"border: 2px solid #505050;")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout.addWidget(self.lineEdit_5)

        self.retranslateUi(Sim1)
        QtCore.QMetaObject.connectSlotsByName(Sim1)

        self.pushButton.clicked.connect(lambda: self.add_functions())

    def retranslateUi(self, Sim1):
        _translate = QtCore.QCoreApplication.translate
        Sim1.setWindowTitle(_translate("Sim1", "Вычислить длину отрезка в треугольнике"))
        self.pushButton_2.setText(_translate("Sim1", "вернуться назад"))
        self.label.setText(_translate("Sim1", "Известно, что отрезки по парам - пропорциональны. Напишите 3 отрезка:"))
        self.label_2.setText(_translate("Sim1", "AB"))
        self.label_3.setText(_translate("Sim1", "AC"))
        self.label_4.setText(_translate("Sim1", "AK"))
        self.pushButton.setText(_translate("Sim1", "Дать ответ"))
        self.label_5.setText(_translate("Sim1", "Ответ:"))

    def add_functions(self):
        input_cut1 = float(self.lineEdit_2.text())
        input_cut2 = float(self.lineEdit_3.text())
        input_cut3 = float(self.lineEdit_5.text())

        otvet = (input_cut1 / input_cut2) * input_cut3

        self.lineEdit_4.setText(str(otvet))