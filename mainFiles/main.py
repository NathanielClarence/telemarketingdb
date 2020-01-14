'''import mysql.connector as conn'''
from PyQt5 import QtWidgets, uic, QtCore
import sys
from superLogin import Ui as spLogin
from standardLogin import Ui as stdLogin
from dbEdit import Ui as editDB

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('assets/ui/chooseLogin.ui', self)
        #self.wdw = self
        self.showFullScreen()
        self.setFixedSize(self.width(), self.height())
        self.scrollArea.setGeometry(int(self.width()/4),int(self.height()/4), int(self.width()/2), int(self.height()/2))
        self.initUI()

    def initUI(self):
        self.sa_Login.clicked.connect(self.superLogin)
        self.adm_Login.clicked.connect(lambda: self.standard("adm"))
        self.tel_Login.clicked.connect(lambda: self.standard("tele"))
        self.exit.clicked.connect(self.clsWindow)
        self.btn_dbEdit.clicked.connect(self.dbEdit)

    def dbEdit(self):
        self.dbEditWin = QtWidgets.QWidget()
        self.dbEditWin.ui = editDB(self)
        self.hide()

    def superLogin(self):
        self.openWindow = QtWidgets.QDialog()
        self.openWindow.ui = spLogin(self)

    def standard(self, priv):
        self.openWindow = QtWidgets.QDialog()
        self.openWindow.ui = stdLogin(priv, self)

    def clsWindow(self):
        QtWidgets.qApp.quit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    premain = QtWidgets.QMainWindow()
    premain.ui = Ui()
    sys.exit(app.exec_())