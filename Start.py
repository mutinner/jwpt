# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import Handle
import requests


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(398, 331)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.user_name = QtWidgets.QLabel(self.centralwidget)
        self.user_name.setGeometry(QtCore.QRect(90, 15, 110, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.user_name.setFont(font)
        self.user_name.setObjectName("user_name")
        self.number = QtWidgets.QLabel(self.centralwidget)
        self.number.setGeometry(QtCore.QRect(210, 15, 110, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.number.setFont(font)
        self.number.setObjectName("number")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 50, 351, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.info = QtWidgets.QTextEdit(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(20, 90, 351, 181))
        self.info.setObjectName("info")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.info.setFont(font)
        # 禁止编辑
        self.info.setFocusPolicy(QtCore.Qt.NoFocus)
        cursor = self.info.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        self.info.setTextCursor(cursor)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 398, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setGeometry(QtCore.QRect(273, 134, 148, 96))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.menuMenu.setFont(font)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.logout = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.logout.setFont(font)
        self.logout.setObjectName("logout")
        self.info_2 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.info_2.setFont(font)
        self.info_2.setObjectName("info_2")
        self.begin = QtWidgets.QAction(MainWindow)
        self.begin.setFont(font)
        self.begin.setObjectName("begin")
        self.menuMenu.addAction(self.begin)
        self.menuMenu.addAction(self.logout)
        self.menuMenu.addAction(self.info_2)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.begin.triggered.connect(self.start)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "一键评教"))
        self.user_name.setText(_translate("MainWindow", ""))
        self.number.setText(_translate("MainWindow", ""))
        self.menuMenu.setTitle(_translate("MainWindow", "菜单"))
        self.logout.setText(_translate("MainWindow", "注销"))
        self.info_2.setText(_translate("MainWindow", "关于"))
        self.begin.setText(_translate("MainWindow", "开始"))

    def clear(self):
        self.info.setText("")
        self.user_name.setText("")
        self.number.setText("")
        self.progressBar.setRange(0, 100)
        self.progressBar.setValue(0)

    def start(self):
        try:
            num = Handle.list_num()
            self.progressBar.setRange(0, num)
            k = 0
            for i in Handle.start():
                for j in i:
                    self.info.insertPlainText(j)
                k += 1
                self.progressBar.setValue(k)
                t = QtCore.QTime()
                t.start()
                while t.elapsed() < 1000:
                    QtCore.QCoreApplication.processEvents()
        except requests.exceptions.ConnectionError:
            self.progressBar.setValue(0)
            self.info.append("连接失败!请检查网络")
        except Exception as e:
            self.progressBar.setValue(0)
            self.info.append("发生错误!请重试")
            self.info.append(str(e))
        else:
            self.progressBar.setValue(num)
            self.info.append("评估完成!")
            self.info.append("请自行检查是否全部评估,如有未知结果请重试")
