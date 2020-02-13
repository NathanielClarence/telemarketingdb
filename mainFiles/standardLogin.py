from PyQt5 import QtWidgets, uic
import mysql.connector as conn
import mysql.connector.locales.eng.client_error as locale
import fetcher
from adminUI import Ui as admPage
from telle_postlog import Ui as telle

class Ui(QtWidgets.QDialog):
    def __init__(self, priv, wdw):
        super(Ui, self).__init__()
        uic.loadUi('assets/ui/login.ui', self)
        self.setFixedSize(self.width(), self.height())

        self.mainWin = wdw
        self.show()
        self.btn_close.clicked.connect(self.closeWin)
        self.btn_login.clicked.connect(self.login)
        self.priv = priv
        self.hst = None
        self.user = None
        self.passw = None
        self.dbcore = None

        self.loca = locale

    def closeWin(self):
        self.close()

    def login(self):
        self.hst, self.user, self.passw, self.dbcore = fetcher.admData()

        try:
            self.mydb = conn.connect(
                host=self.hst,
                user=self.user,#sesuaikan user khusus
                passwd=self.passw,#sesuaikan user khusus
                database=self.dbcore,
                auth_plugin='mysql_native_password',
                buffered = True
            )

            try:
                self.uname = self.in_uname.text()
                self.paswd = self.in_pass.text()

                if self.priv == 'adm':
                    self.query = "SELECT username FROM ADMINS WHERE USERNAME = %s and password = sha2(%s, 512) and " \
                                 "privilege = %s and active_status = true;"
                    self.inst = (self.uname, self.paswd, self.priv)
                elif self.priv == 'tele':
                    self.query = "SELECT username, privilege FROM ADMINS WHERE USERNAME = %s and password = sha2(%s, 512)" \
                                 " and active_status = true;"
                    self.inst = (self.uname, self.paswd)

                # print(inst)
                self.mycursor = self.mydb.cursor()
                self.mycursor.execute(self.query, self.inst)
                self.result = self.mycursor.fetchone()
                #print(self.result)
                # print(self.result[0])
                if self.result!=None:
                    if self.priv == 'adm' and self.result!=None:
                        self.adminPage()
                    elif self.priv == 'tele' and self.result!=None:
                        self.telePage(self.result[1])
                else:
                    self.buttonReply = QtWidgets.QMessageBox
                    self.warning = self.buttonReply.question(self, 'WARNING', "Pengguna tidak ditemukan",
                                                             QtWidgets.QMessageBox.Ok)
            except Exception as e:
                print(str(e))
                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'WARNING', str(e),# "User not found or wrong password",
                                                         QtWidgets.QMessageBox.Ok)

        except Exception as e:
            print(str(e))
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

    def adminPage(self):
        self.adminPg = QtWidgets.QWidget()
        self.adminPg.ui = admPage(self.priv, self.mainWin, self.mycursor, self.uname)#should be changed to preadmin
        self.mainWin.hide()
        self.close()

    def telePage(self, priv):
        #print("Not yet there")
        self.telle = QtWidgets.QWidget()
        #print(priv)
        self.telle.ui = telle(priv, self.mainWin, self.mycursor, self.uname)
        self.mainWin.hide()
        self.close()
        #pre-telepage
        # opts: search (followup-by phone/uniquecd/name), hubungi kembali, new data(from db)