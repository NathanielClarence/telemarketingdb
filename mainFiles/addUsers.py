from PyQt5 import QtWidgets, uic
import fetcher
import sys

class Ui(QtWidgets.QWidget):
    def __init__(self, user, mycursor, parentWin):
        super(Ui, self).__init__()
        uic.loadUi('assets/ui/superadminAddUser.ui', self)
        self.showFullScreen()
        self.setFixedSize(self.width(), self.height())
        self.scrollArea.setGeometry(int(self.width() / 4), int(self.height() / 4), int(self.width() / 2),
                                    int(self.height() / 2))
        self.dropip = None
        self.dropdb = None
        self.usedb = None
        self.dropip, self.dropdb, self.usedb = fetcher.superData()

        self.user = user
        self.mycursor = mycursor
        self.parentWin = parentWin

        self.initUI()

    def closeWin(self):
        self.parentWin.show()
        self.close()

    def deactivateUser(self):
        self.removeadm = self.cmb_admName.currentText()
        self.qm = QtWidgets.QMessageBox
        self.confirm = self.qm.question(self, 'PERINGATAN',
                                        "Apakah anda yakin ingin menghapus pengguna " + self.removeadm + "?",
                                        self.qm.Yes | self.qm.No)
        if self.confirm == self.qm.Yes:
            try:
                self.query = "UPDATE "+self.usedb+".admins set active_status = False where username like %s;"
                self.mycursor.execute(self.query,(self.admins[self.cmb_admName.currentIndex()][0],))
                self.mycursor.execute("commit;")

                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'Hapus Admin', "Admin berhasil dinonaktifkan",
                                                         QtWidgets.QMessageBox.Ok)

                self.closeWin()
            except Exception as e:
                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                         QtWidgets.QMessageBox.Ok)

    def reactivateUser(self):
        self.removeadm = self.cmb_inactive.currentText()
        self.qm = QtWidgets.QMessageBox
        self.confirm = self.qm.question(self, 'PERINGATAN',
                                        "Apakah anda yakin ingin mengaktifkan pengguna " + self.removeadm + "?",
                                        self.qm.Yes | self.qm.No)
        if self.confirm == self.qm.Yes:
            try:
                self.query = "UPDATE dbtest.admins set active_status = True where username like %s;"
                self.mycursor.execute(self.query, (self.inactive_admins[self.cmb_inactive.currentIndex()][0],))
                self.mycursor.execute("commit;")

                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'Tambah Admin', "Admin berhasil diaktifkan kembali",
                                                         QtWidgets.QMessageBox.Ok)

                self.closeWin()
            except Exception as e:
                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                         QtWidgets.QMessageBox.Ok)

    def initUI(self):
        self.btn_back.clicked.connect(self.closeWin)
        self.cmb_privilege.currentIndexChanged.connect(self.activateNext)
        self.btn_add.clicked.connect(self.addUser)
        self.btn_deactivate.clicked.connect(self.deactivateUser)
        self.btn_reactivate.clicked.connect(self.reactivateUser)

        try:
            self.query = "SELECT nama_produk, kode_produk FROM "+self.usedb+".products;"
            self.mycursor.execute(self.query)
            self.products = self.mycursor.fetchall()
            for x in self.products:
                self.cmb_product.addItem(str(x[1])+" - "+str(x[0]))

        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

        try:
            self.query = "SELECT username, name from "+self.usedb+".admins where active_status = 1;"
            self.mycursor.execute(self.query)
            self.admins = self.mycursor.fetchall()
            for x in self.admins:
                self.cmb_admName.addItem(str(x[1]))
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

        try:
            self.query = "SELECT username, name from "+self.usedb+".admins where active_status = 0;"
            self.mycursor.execute(self.query)
            self.inactive_admins = self.mycursor.fetchall()
            for x in self.inactive_admins:
                self.cmb_inactive.addItem(str(x[1]))
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

    def addUser(self):
        self.name = self.in_name.text()
        self.passw = self.in_password.text()
        self.uname = self.in_username.text()

        try:
            if self.name == '' or self.passw == '' or self.uname == '':
                raise Exception("Name, username, and password must not be empty.")

            if self.cmb_privilege.currentText() == 'Admin':
                self.privilege = 'adm'
                self.prod = "all"
            else:
                self.privilege = 'telle'
                self.prod = self.products[self.cmb_product.currentIndex()][1]
                #print(self.prod)

            self.query = "INSERT INTO "+self.usedb+".admins(name, password, username, privilege, product) VALUES (%s, sha2(%s, 512), %s, %s, %s);"
            self.mycursor.execute(self.query, (self.name, self.passw, self.uname, self.privilege, self.prod))
            print(self.query)
            print(self.name)
            print(self.passw)
            self.mycursor.execute("commit;")
            self.mycursor.execute("use mysql;")

            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'Tambah pengguna', self.name+" berhasil ditambahkan.",
                                                     QtWidgets.QMessageBox.Ok)
            self.closeWin()
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

    def activateNext(self):
        if self.cmb_privilege.currentText() == "Telle":
            self.cmb_product.setEnabled(True)
        else:
            self.cmb_product.setEnabled(False)

'''if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    premain = QtWidgets.QWidget()
    premain.ui = Ui()
    sys.exit(app.exec_())'''