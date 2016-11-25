# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import Handle
import requests


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(525, 450)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.user_name = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_name.sizePolicy().hasHeightForWidth())
        self.user_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.user_name.setFont(font)
        self.user_name.setText("")
        self.user_name.setAlignment(QtCore.Qt.AlignCenter)
        self.user_name.setObjectName("user_name")
        self.horizontalLayout.addWidget(self.user_name)
        self.number = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number.sizePolicy().hasHeightForWidth())
        self.number.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.number.setFont(font)
        self.number.setText("")
        self.number.setAlignment(QtCore.Qt.AlignCenter)
        self.number.setObjectName("number")
        self.horizontalLayout.addWidget(self.number)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.info = QtWidgets.QTextEdit(self.centralwidget)
        self.info.setObjectName("info")
        self.verticalLayout.addWidget(self.info)
        # 禁止编辑
        self.info.setFocusPolicy(QtCore.Qt.NoFocus)
        # 自动滚屏
        cursor = self.info.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        self.info.setTextCursor(cursor)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setGeometry(QtCore.QRect(782, 220, 171, 130))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu.sizePolicy().hasHeightForWidth())
        self.menu.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.menu.setFont(font)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.begin = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.begin.setFont(font)
        self.begin.setObjectName("begin")
        self.logout = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.logout.setFont(font)
        self.logout.setObjectName("logout")
        self.info_2 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.info_2.setFont(font)
        self.info_2.setObjectName("info_2")
        self.menu.addAction(self.begin)
        self.menu.addAction(self.logout)
        self.menu.addAction(self.info_2)
        self.menubar.addAction(self.menu.menuAction())

        self.begin.triggered.connect(self.start)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "一键评教"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.begin.setText(_translate("MainWindow", "开始"))
        self.logout.setText(_translate("MainWindow", "注销"))
        self.info_2.setText(_translate("MainWindow", "关于"))

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
            if num == 0:
                self.progressBar.setRange(0, 100)
                num = 100
            self.progressBar.setValue(num)
            self.info.append("评估完成!")
            self.info.append("请自行检查是否全部评估,如有未知结果或未评估的请重试")
