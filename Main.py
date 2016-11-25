from PyQt5 import QtWidgets
import Login
import Info
import Handle
import requests
import re
import Start
import sys
import webbrowser

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget1 = QtWidgets.QMainWindow()
widget2 = QtWidgets.QDialog()
version = '1.2'


def upgrade():
    try:
        control = requests.get("http://www.parallelc.cn/list.html")
    except Exception:
        return False
    else:
        new = re.findall('version:(.*)', control.text)
        if new:
            return new[0] != version
        else:
            return False


def try_go():
    try:
        html = Handle.login(ui.user_name.text(), ui.password.text(), ui.yzm.text())
        error = re.findall('<strong><font color="#990000">(.*?)</font></strong><br>', html.text)
        if error:
            ui.warn.setText(error[0])
            ui.img.show_img()
            return
        control = requests.get("http://www.parallelc.cn/list.html")
        go_list = re.findall("#(.*)", control.text)
        right = 0
        for i in go_list:
            if re.match(i, ui.user_name.text()):
                right = 1
                break
        if right == 0:
            raise Exception("你没有使用权限!")
    except requests.exceptions.ConnectionError:
        ui.warn.setText("连接失败!请检查网络")
    except Exception as e:
        ui.img.show_img()
        ui.warn.setText("发生错误!" + str(e))
    else:
        widget.close()
        ui1.clear()
        ui1.progressBar.setValue(0)
        info = Handle.get_info()
        ui1.number.setText(info[0])
        ui1.user_name.setText(info[1])
        widget1.show()


def logout():
    widget1.close()
    ui.clear()
    widget.show()

if __name__ == "__main__":
    ui = Login.Ui_Form()
    ui.setupUi(widget)
    ui1 = Start.Ui_MainWindow()
    ui1.setupUi(widget1)
    ui2 = Info.Ui_Dialog()
    ui2.setupUi(widget2)

    widget.show()
    if upgrade():
        reply = QtWidgets.QMessageBox.question(None, '更新', '\n有新版本,是否更新?',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.Yes)
        if reply == QtWidgets.QMessageBox.Yes:
            webbrowser.open("http://www.parallelc.cn/pj.zip")

    ui.login.clicked.connect(try_go)
    ui1.logout.triggered.connect(logout)
    ui1.info_2.triggered.connect(widget2.show)
    ui2.label_4.setText(ui2.label_4.text() + version)

    sys.exit(app.exec_())
