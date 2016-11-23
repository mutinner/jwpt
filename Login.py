# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import Main
import Start
import requests
import re
import sys
import info

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget1 = QtWidgets.QMainWindow()
widget2 = QtWidgets.QDialog()


class MyLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(MyLabel, self).__init__(parent)

    def mouseReleaseEvent(self, QMouseEvent):
        self.show_img()

    def show_img(self):
        self.setText("加载中...")
        try:
            Main.load_img()
        except Exception:
            self.setText("加载失败")
        else:
            self.setPixmap(QtGui.QPixmap("code.jpg"))
            self.show()


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 309)
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

        self.login.clicked.connect(self.try_go)
        self.reset.clicked.connect(self.clear)
        self.img.setObjectName("img")

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

    def try_go(self):
        try:
            html = Main.login(self.user_name.text(), self.password.text(), self.yzm.text())
        except requests.exceptions.ConnectionError:
            self.warn.setText("连接失败!请检查网络")
        except Exception as e:
            self.warn.setText("发生错误!" + e)
        else:
            error = re.findall('<strong><font color="#990000">(.*?)</font></strong><br>', html.text)
            if error:
                self.warn.setText(error[0])
                self.img.show_img()
            else:
                widget.close()
                ui1.clear()
                ui1.progressBar.setValue(0)
                info = Main.get_info()
                ui1.number.setText(info[0])
                ui1.user_name.setText(info[1])
                widget1.show()


def change():
    widget1.close()
    ui.clear()
    widget.show()

if __name__ == "__main__":
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    ui1 = Start.Ui_MainWindow()
    ui1.setupUi(widget1)
    ui1.logout.triggered.connect(change)
    ui2 = info.Ui_Dialog()
    ui2.setupUi(widget2)
    ui1.info_2.triggered.connect(widget2.show)
    sys.exit(app.exec_())
