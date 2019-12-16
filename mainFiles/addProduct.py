from PyQt5 import QtWidgets, uic
import fetcher

class Ui(QtWidgets.QWidget):
    def __init__(self, user, mycursor, parentWin):
        super(Ui, self).__init__()
        uic.loadUi('assets/ui/addRemoveProduct.ui', self)
        self.setFixedSize(self.width(), self.height())
        self.show()
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
        self.hide()

    def removePrd(self):
        self.removeprod = self.cmb_prd.currentText()
        self.qm = QtWidgets.QMessageBox
        self.confirm = self.qm.question(self, 'PERINGATAN',
                                        "Apakah anda yakin ingin menghapus produk " + self.removeprod + "?",
                                        self.qm.Yes | self.qm.No)

        if self.confirm == self.qm.Yes:
            try:
                self.query = "DELETE FROM "+self.usedb+".products WHERE kode_produk like %s;"
                self.mycursor.execute(self.query, (self.products[self.cmb_prd.currentIndex()][1],))
                self.mycursor.execute("Drop table "+self.usedb+".prod_"+self.products[self.cmb_prd.currentIndex()][1]+";")
                self.mycursor.execute("Drop table "+self.usedb+".bank_" + self.products[self.cmb_prd.currentIndex()][1] + ";")
                self.mycursor.execute("commit;")

                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'Hapus Produk', "Produk berhasil dihapus.",
                                                         QtWidgets.QMessageBox.Ok)

                self.closeWin()
            except Exception as e:
                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                         QtWidgets.QMessageBox.Ok)

    def addPrd(self):
        self.name = self.in_name.text()
        self.code = self.in_code.text()

        try:
            if self.name == '' or self.code == '':
                raise Exception("Product name and product code must not be empty.")

            self.query = "INSERT INTO "+self.usedb+".products(nama_produk, kode_produk) VALUES (%s, %s);"
            self.mycursor.execute(self.query, (self.name, self.code))
            self.mycursor.execute("use "+self.usedb+";")
            self.mycursor.execute("CREATE TABLE prod_"+self.code+" like prod_cc;")
            self.mycursor.execute("CREATE TABLE bank_"+self.code+" like bank_cc;")
            self.mycursor.execute("commit;")
            self.mycursor.execute("use mysql;")

            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'Tambah produk', self.name+" berhasil ditambahkan.",
                                                     QtWidgets.QMessageBox.Ok)
            self.closeWin()
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

    def initUI(self):
        self.btn_delete.clicked.connect(self.removePrd)
        self.btn_add.clicked.connect(self.addPrd)
        self.btn_back.clicked.connect(self.closeWin)

        try:
            self.query = "SELECT nama_produk, kode_produk FROM "+self.usedb+".products;"
            self.mycursor.execute(self.query)
            self.products = self.mycursor.fetchall()
            for x in self.products:
                self.cmb_prd.addItem(str(x[1]) + " - " + str(x[0]))

        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)