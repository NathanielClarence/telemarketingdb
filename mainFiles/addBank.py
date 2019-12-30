from PyQt5 import QtWidgets, uic, QtGui
import fetcher

class Ui(QtWidgets.QWidget):
    def __init__(self, mycursor):
        super(Ui, self).__init__()
        uic.loadUi('assets/ui/addBankUI.ui', self)
        self.setFixedSize(self.width(), self.height())
        self.show()

        self.mycursor = mycursor
        self.dropip = None
        self.dropdb = None
        self.usedb = None

        self.dropip, self.dropdb, self.usedb = fetcher.superData()

        self.initUI()

        self.btn_cancel.clicked.connect(self.closeWin)
        self.btn_add.clicked.connect(self.addBank)

    def closeWin(self):
        self.close()

    def initUI(self):
        try:
            self.query = "SELECT KODE_PRODUK FROM "+self.usedb+".PRODUCTS;"
            self.mycursor.execute(self.query)
            self.res = self.mycursor.fetchall()

            for x in self.res:
                self.cmb_prod.addItem(x[0])
                self.cmb_prdList.addItem(x[0])
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

        self.refreshBank()
        self.cmb_prdList.currentIndexChanged.connect(self.refreshBank)
        self.btn_remove.clicked.connect(self.removeBank)

    def refreshBank(self):
        try:
            self.query = "SELECT nama_bank from "+self.usedb+".bank_"+self.cmb_prdList.currentText().lower()+";"
            self.mycursor.execute(self.query)
            self.res = self.mycursor.fetchall()
            #print(self.res)

            self.cmb_removeBank.clear()

            for x in self.res:
                self.cmb_removeBank.addItem(x[0])
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

    def removeBank(self):
        self.removebnk = self.cmb_removeBank.currentText()
        self.qm = QtWidgets.QMessageBox
        self.confirm = self.qm.question(self, 'PERINGATAN',
                                        "Apakah anda yakin ingin menghapus " + self.removebnk + "?",
                                        self.qm.Yes | self.qm.No)

        if self.confirm == self.qm.Yes:
            try:
                self.query = "Delete from "+self.usedb+".bank_"+self.cmb_prdList.currentText()+" where nama_bank = %s;"
                self.bank = self.cmb_removeBank.currentText()
                self.mycursor.execute(self.query,(self.bank,))
                self.mycursor.execute("commit;")

                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'Hapus Bank', "Bank berhasil dihapus.",
                                                         QtWidgets.QMessageBox.Ok)

                self.closeWin()
            except Exception as e:
                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                         QtWidgets.QMessageBox.Ok)

    def addBank(self):
        self.namabank = self.in_bankName.text()
        self.produk = self.cmb_prod.currentText()
        try:
            if self.namabank == '':
                raise Exception("Nama bank harus diisi")

            self.query = "INSERT INTO "+self.usedb+".bank_"+self.produk+" (nama_bank) values (%s);"
            self.mycursor.execute(self.query, (self.namabank,))
            self.mycursor.execute("commit;")
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'NOTIFICATION', "Bank berhasil ditambahkan",
                                                     QtWidgets.QMessageBox.Ok)
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

        self.close()