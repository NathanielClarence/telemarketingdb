from PyQt5 import QtWidgets, uic
import fetcher

class Ui(QtWidgets.QWidget):
    def __init__(self, user, mycursor, parentWin):
        super(Ui, self).__init__()
        uic.loadUi('assets/ui/addRemoveSuperadmin.ui', self)
        self.setFixedSize(self.width(), self.height())
        self.show()

        self.user = user
        self.mycursor = mycursor
        self.parentWin = parentWin
        #print(self.dbuser)

        self.dmp1, self.dbuser, self.dmp2, self.dmp3 = fetcher.admData()

        self.initUI()

    def closeWin(self):
        self.parentWin.show()
        self.close()

    def addSA(self):
        self.newuser = self.in_username.text()
        self.newpass = self.in_password.text()

        try:
            if self.newuser == '' or self.newpass == '':
                raise Exception("Username and Password cannot be empty.")

            self.query = "CREATE USER %s@'%' IDENTIFIED BY %s;"
            self.mycursor.execute(self.query,(self.newuser, self.newpass))
            self.mycursor.execute("""GRANT ALL PRIVILEGES ON *. * TO %s@'%' with grant option;""", (self.newuser,))

            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'Tambah Superadmin', "Superadmin berhasil ditambahkan",
                                                     QtWidgets.QMessageBox.Ok)
            self.closeWin()
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

    def initUI(self):
        self.btn_back.clicked.connect(self.closeWin)
        self.btn_add.clicked.connect(self.addSA)
        self.btn_delete.clicked.connect(self.removeSA)

        try:
            self.query =  "SELECT user from user where user not like '%mysql%' and user not like 'root' and user not like" \
                          " %s and host like '\%' and user not like %s;"
            self.mycursor.execute(self.query, (self.user,self.dbuser))
            self.superadmins = self.mycursor.fetchall()
            for x in self.superadmins:
                self.cmb_superadmin.addItem(x[0])
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

    def removeSA(self):
        #print(self.cmb_superadmin.currentText())
        self.removeadm = self.cmb_superadmin.currentText()
        self.qm = QtWidgets.QMessageBox
        self.confirm = self.qm.question(self, 'PERINGATAN', "Apakah anda yakin ingin menghapus superadmin "+self.removeadm+"?",
                                        self.qm.Yes | self.qm.No)
        if self.confirm == self.qm.Yes:
            try:

                self.query = "REVOKE ALL PRIVILEGES, GRANT OPTION FROM %s@'%';"
                self.mycursor.execute(self.query,(self.removeadm, ))
                self.mycursor.execute("drop user %s@'%';", (self.removeadm, ))

                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'Hapus Superadmin', "Superadmin berhasil dihapus.",
                                                         QtWidgets.QMessageBox.Ok)

                self.closeWin()
            except Exception as e:
                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                         QtWidgets.QMessageBox.Ok)