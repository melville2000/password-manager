# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/design/signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pass_vault_ui.layouts import login_rc

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(587, 602)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/design/../logo/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.username_input = QtWidgets.QLineEdit(Form)
        self.username_input.setGeometry(QtCore.QRect(260, 270, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        self.username_input.setFont(font)
        self.username_input.setText("")
        self.username_input.setObjectName("username_input")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 270, 107, 30))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.password_input = QtWidgets.QLineEdit(Form)
        self.password_input.setEnabled(True)
        self.password_input.setGeometry(QtCore.QRect(260, 350, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        self.password_input.setFont(font)
        self.password_input.setAcceptDrops(False)
        self.password_input.setText("")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setClearButtonEnabled(False)
        self.password_input.setObjectName("password_input")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 390, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.confirm_password_input = QtWidgets.QLineEdit(Form)
        self.confirm_password_input.setEnabled(True)
        self.confirm_password_input.setGeometry(QtCore.QRect(260, 390, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        self.confirm_password_input.setFont(font)
        self.confirm_password_input.setAcceptDrops(False)
        self.confirm_password_input.setText("")
        self.confirm_password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password_input.setClearButtonEnabled(False)
        self.confirm_password_input.setObjectName("confirm_password_input")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 350, 107, 30))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(80, 310, 107, 30))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        font.setBold(False)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.otp_input = QtWidgets.QLineEdit(Form)
        self.otp_input.setEnabled(True)
        self.otp_input.setGeometry(QtCore.QRect(260, 430, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        self.otp_input.setFont(font)
        self.otp_input.setAcceptDrops(False)
        self.otp_input.setText("")
        self.otp_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.otp_input.setClearButtonEnabled(False)
        self.otp_input.setObjectName("otp_input")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(80, 430, 171, 30))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        font.setBold(False)
        self.label_6.setFont(font)
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.sign_up_btn = QtWidgets.QPushButton(Form)
        self.sign_up_btn.setGeometry(QtCore.QRect(230, 480, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        self.sign_up_btn.setFont(font)
        self.sign_up_btn.setObjectName("sign_up_btn")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(100, 540, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.email_input = QtWidgets.QLineEdit(Form)
        self.email_input.setGeometry(QtCore.QRect(260, 310, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        self.email_input.setFont(font)
        self.email_input.setText("")
        self.email_input.setObjectName("email_input")
        self.get_otp_btn = QtWidgets.QPushButton(Form)
        self.get_otp_btn.setGeometry(QtCore.QRect(450, 390, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        self.get_otp_btn.setFont(font)
        self.get_otp_btn.setObjectName("get_otp_btn")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(60, 50, 501, 201))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PassVault Register"))
        self.label.setText(_translate("Form", "Username"))
        self.label_2.setText(_translate("Form", "Confirm Password"))
        self.label_3.setText(_translate("Form", "Password"))
        self.label_5.setText(_translate("Form", "Email"))
        self.label_6.setText(_translate("Form", "OTP"))
        self.sign_up_btn.setText(_translate("Form", "Sign Up"))
        self.get_otp_btn.setText(_translate("Form", "Get OTP"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><img src=\":/newPrefix/logo/login_screen.png\"/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
