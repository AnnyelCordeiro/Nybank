# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 527)
        Form.setStyleSheet("background-color: rgb(196, 215, 255);")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 410, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 40, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Uroob")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ButtonCadastrar = QtWidgets.QPushButton(Form)
        self.ButtonCadastrar.setGeometry(QtCore.QRect(240, 290, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.ButtonCadastrar.setFont(font)
        self.ButtonCadastrar.setStyleSheet("color: rgb(0, 122, 0);\n"
"background-color: rgb(171, 200, 206,0);")
        self.ButtonCadastrar.setObjectName("ButtonCadastrar")
        self.ButtonVoltar = QtWidgets.QPushButton(Form)
        self.ButtonVoltar.setGeometry(QtCore.QRect(240, 330, 101, 23))
        self.ButtonVoltar.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 0, 0,0);")
        self.ButtonVoltar.setObjectName("ButtonVoltar")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(180, 210, 57, 15))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(190, 240, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(190, 150, 57, 15))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(190, 180, 57, 15))
        self.label_9.setObjectName("label_9")
        self.lineUsuario = QtWidgets.QLineEdit(Form)
        self.lineUsuario.setGeometry(QtCore.QRect(240, 150, 113, 20))
        self.lineUsuario.setObjectName("lineUsuario")
        self.lineSenha = QtWidgets.QLineEdit(Form)
        self.lineSenha.setGeometry(QtCore.QRect(240, 180, 113, 20))
        self.lineSenha.setObjectName("lineSenha")
        self.lineNome = QtWidgets.QLineEdit(Form)
        self.lineNome.setGeometry(QtCore.QRect(240, 210, 113, 20))
        self.lineNome.setObjectName("lineNome")
        self.lineCpf = QtWidgets.QLineEdit(Form)
        self.lineCpf.setGeometry(QtCore.QRect(240, 240, 113, 20))
        self.lineCpf.setObjectName("lineCpf")
        self.labelNotificacao = QtWidgets.QLabel(Form)
        self.labelNotificacao.setGeometry(QtCore.QRect(180, 380, 221, 20))
        self.labelNotificacao.setObjectName("labelNotificacao")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "NyBank"))
        self.label.setText(_translate("Form", "Seja Bem-Vindo ao NyBank"))
        self.ButtonCadastrar.setText(_translate("Form", "Cadastrar"))
        self.ButtonVoltar.setText(_translate("Form", "Sair"))
        self.label_4.setText(_translate("Form", "  Nome :"))
        self.label_2.setText(_translate("Form", "Cadastro"))
        self.label_6.setText(_translate("Form", "CPF:"))
        self.label_8.setText(_translate("Form", "Usuário :"))
        self.label_9.setText(_translate("Form", "Senha :"))
        self.labelNotificacao.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
