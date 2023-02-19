# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_transfere.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(643, 480)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        Form.setStyleSheet("background-color: rgb(196, 215, 255);")
        self.ButtonSair = QtWidgets.QPushButton(Form)
        self.ButtonSair.setGeometry(QtCore.QRect(490, 380, 80, 23))
        self.ButtonSair.setStyleSheet("background-color: rgb(255, 0, 0, 0);")
        self.ButtonSair.setObjectName("ButtonSair")
        self.lineNumero = QtWidgets.QLineEdit(Form)
        self.lineNumero.setGeometry(QtCore.QRect(300, 180, 151, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineNumero.setFont(font)
        self.lineNumero.setStyleSheet("background-color: rgb(196, 215, 255, 0.5);")
        self.lineNumero.setObjectName("lineNumero")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 50, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 410, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.ButtonTransferir = QtWidgets.QPushButton(Form)
        self.ButtonTransferir.setGeometry(QtCore.QRect(340, 300, 80, 23))
        self.ButtonTransferir.setStyleSheet("background-color: rgb(171, 200, 206,0);")
        self.ButtonTransferir.setObjectName("ButtonTransferir")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 220, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(140, 180, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineSaldo = QtWidgets.QLineEdit(Form)
        self.lineSaldo.setGeometry(QtCore.QRect(300, 220, 151, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineSaldo.setFont(font)
        self.lineSaldo.setStyleSheet("background-color: rgb(196, 215, 255, 0.5);")
        self.lineSaldo.setObjectName("lineSaldo")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(450, 200, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.ButtonVoltar = QtWidgets.QPushButton(Form)
        self.ButtonVoltar.setGeometry(QtCore.QRect(380, 380, 80, 23))
        self.ButtonVoltar.setStyleSheet("background-color: rgb(171, 200, 206,0);")
        self.ButtonVoltar.setObjectName("ButtonVoltar")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(230, 260, 61, 20))
        self.label_6.setObjectName("label_6")
        self.lineSenha = QtWidgets.QLineEdit(Form)
        self.lineSenha.setGeometry(QtCore.QRect(300, 260, 151, 20))
        self.lineSenha.setObjectName("lineSenha")
        self.labelNotificacao = QtWidgets.QLabel(Form)
        self.labelNotificacao.setGeometry(QtCore.QRect(280, 350, 181, 20))
        self.labelNotificacao.setObjectName("labelNotificacao")
        self.lineNumero_2 = QtWidgets.QLineEdit(Form)
        self.lineNumero_2.setGeometry(QtCore.QRect(300, 140, 151, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineNumero_2.setFont(font)
        self.lineNumero_2.setStyleSheet("background-color: rgb(196, 215, 255, 0.5);")
        self.lineNumero_2.setObjectName("lineNumero_2")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(160, 140, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ButtonSair.setText(_translate("Form", "Sair"))
        self.label.setText(_translate("Form", "Transferência"))
        self.label_3.setText(_translate("Form", "NyBank"))
        self.ButtonTransferir.setText(_translate("Form", "Transferir"))
        self.label_2.setText(_translate("Form", "Valor da transferência : "))
        self.label_4.setText(_translate("Form", " Número destino : "))
        self.label_5.setText(_translate("Form", "(O número da conta de destino)"))
        self.ButtonVoltar.setText(_translate("Form", "Voltar"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Senha:</span></p></body></html>"))
        self.labelNotificacao.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_7.setText(_translate("Form", "Número conta : "))