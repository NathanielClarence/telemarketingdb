import fetcher
from PyQt5 import QtWidgets, uic

class Ui(QtWidgets.QWidget):
    def __init__(self, parentWin):
        super(Ui, self).__init__()
        uic.loadUi('assets/ui/dbEdit.ui', self)
        self.setFixedSize(self.width(), self.height())
        self.show()

        self.parentWin = parentWin

        self.ipadd = None
        self.user = None
        self.passw = None
        self.dbcore = None

        self.initUI()

    def initUI(self):
        self.ipadd, self.user, self.passw, self.dbcore = fetcher.admData()
        if self.ipadd =='127.0.0.1':
            self.in_ipadd.setEnabled(False)
        else:
            self.in_ipadd.setEnabled(True)
            self.cmb_pc.setCurrentIndex(1)
        self.in_ipadd.setText(self.ipadd)
        self.in_uname.setText(self.user)
        self.in_pass.setText(self.passw)
        self.in_db.setText(self.dbcore)

        self.btn_back.clicked.connect(self.clsWin)
        self.btn_save.clicked.connect(self.saveConfig)
        self.cmb_pc.currentIndexChanged.connect(self.activateNext)

    def activateNext(self):
        if self.cmb_pc.currentText() == 'Server':
            self.in_ipadd.setEnabled(False)
            self.in_ipadd.setText('127.0.0.1')
        else:
            self.in_ipadd.setText('')
            self.in_ipadd.setEnabled(True)

    def saveConfig(self):
        #print("dd")
        try:
            self.user = self.in_uname.text()+"\n"
            self.passw = self.in_pass.text()+"\n"
            self.dbcore = self.in_db.text()+"\n"
            self.ipadd = self.in_ipadd.text()+"\n"

            if self.user == '\n' or self.passw=='\n' or self.dbcore =='\n' or self.ipadd =='\n':
                raise Exception("Data tidak boleh kosong.")
                #print("Data tidak boleh kosong")

            self.qm = QtWidgets.QMessageBox()
            self.confirm = self.qm.question(self, 'PERINGATAN', "Apakah anda yakin mengubah data berikut?",
                                            self.qm.Yes | self.qm.No)
            if self.confirm == self.qm.Yes:
                self.superadmin = [self.ipadd, "mysql\n", self.dbcore]
                self.othadmin = [self.ipadd, self.user, self.passw, self.dbcore]
                self.writeFile = open("assets/superadmin.dct", "w")
                self.writeFile.writelines(self.superadmin)
                self.writeFile.close()
                self.writeFile = open("assets/othadmin.dct", 'w')
                self.writeFile.writelines(self.othadmin)
                self.writeFile.close()

                self.buttonReply = QtWidgets.QMessageBox()
                self.warning = self.buttonReply.question(self, 'DB Config',
                                                         "Konfigurasi berhasil diubah",
                                                         QtWidgets.QMessageBox.Ok)
                self.clsWin()
        except Exception as e:
            #print(e)
            self.buttonReply = QtWidgets.QMessageBox()
            self.warning = self.buttonReply.question(self, 'PERINGATAN',
                                                     str(e),
                                                     QtWidgets.QMessageBox.Ok)

    def clsWin(self):
        self.parentWin.show()
        self.close()