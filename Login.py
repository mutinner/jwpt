# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import Handle


class MyLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)

    def mouseReleaseEvent(self, QMouseEvent):
        self.show_img()

    def show_img(self):
        self.setText("加载中...")
        try:
            Handle.load_img()
        except Exception:
            self.setText("加载失败")
        else:
            self.setPixmap(QtGui.QPixmap("code.jpg"))
            self.show()


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 309)
        Form.setFixedSize(Form.width(), Form.height())
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(55, 95, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(55, 145, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(55, 195, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.reset = QtWidgets.QPushButton(Form)
        self.reset.setGeometry(QtCore.QRect(80, 250, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.reset.setFont(font)
        self.reset.setObjectName("reset")
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(120, 10, 180, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.login = QtWidgets.QPushButton(Form)
        self.login.setGeometry(QtCore.QRect(230, 250, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.login.setFont(font)
        self.login.setObjectName("login")
        self.warn = QtWidgets.QLabel(Form)
        self.warn.setGeometry(QtCore.QRect(55, 60, 311, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        pa = QtGui.QPalette()
        # 红色
        pa.setColor(QtGui.QPalette.WindowText, QtCore.Qt.red)
        self.warn.setFont(font)
        self.warn.setPalette(pa)
        self.warn.setText("")
        self.warn.setObjectName("warn")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(140, 140, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.password.setFont(font)
        # 密文
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.user_name = QtWidgets.QLineEdit(Form)
        self.user_name.setGeometry(QtCore.QRect(140, 91, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.user_name.setFont(font)
        self.user_name.setObjectName("user_name")
        self.yzm = QtWidgets.QLineEdit(Form)
        self.yzm.setGeometry(QtCore.QRect(140, 190, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.yzm.setFont(font)
        self.yzm.setObjectName("yzm")

        self.img = MyLabel(Form)
        self.img.setGeometry(QtCore.QRect(250, 190, 90, 30))
        self.img.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.img.setText("点击获取")
        self.img.setObjectName("img")

        self.reset.clicked.connect(self.clear)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.user_name, self.password)
        Form.setTabOrder(self.password, self.yzm)
        Form.setTabOrder(self.yzm, self.login)
        Form.setTabOrder(self.login, self.reset)

        self.login.setShortcut(QtCore.Qt.Key_Enter)
        self.login.setShortcut(QtCore.Qt.Key_Return)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录"))
        self.label.setText(_translate("Form", "学号"))
        self.label_2.setText(_translate("Form", "密码"))
        self.label_3.setText(_translate("Form", "验证码"))
        self.reset.setText(_translate("Form", "重置"))
        self.title.setText(_translate("Form", "一键评教"))
        self.login.setText(_translate("Form", "登录"))

    def clear(self):
        self.password.setText("")
        self.user_name.setText("")
        self.yzm.setText("")
        self.img.clear()
        self.img.setText("点击获取")
        self.warn.setText("")

