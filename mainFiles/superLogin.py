from PyQt5 import QtWidgets, uic
import mysql.connector as conn
from superadminUI import Ui as superadmin
import fetcher

class Ui(QtWidgets.QDialog):
    def __init__(self, parentWin):
        super(Ui, self).__init__()
        uic.loadUi('assets/ui/login.ui', self)
        self.setFixedSize(self.width(), self.height())
        self.show()

        self.parentWin = parentWin
        self.btn_close.clicked.connect(self.closeWin)
        self.btn_login.clicked.connect(self.login)
        self.ipadd = None
        self.dbcore = None
        self.dropdb = None

    def closeWin(self):
        self.close()

    def login(self):
        try:
            self.uname = self.in_uname.text()
            self.paswd = self.in_pass.text()
            self.ipadd, self.dbcore, self.dropdb = fetcher.superData()
        except Exception as e:
            print(e)
        try:
            self.mydb = conn.connect(
                host=self.ipadd,
                user=self.uname,
                passwd=self.paswd,
                database=self.dbcore,
                auth_plugin='mysql_native_password',
                buffered = True
            )
            #print("logged in")
            #send mydb to next window
            self.superadminWin = QtWidgets.QWidget()
            self.superadminWin.ui = superadmin(self.uname, self.mydb.cursor(), self.parentWin)
            self.parentWin.hide()
            self.close()

        except Exception as e:
            print(e)
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)