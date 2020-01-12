from PyQt5 import uic, QtWidgets
import sys

class Ui(QtWidgets.QWidget):
    def __init__(self, priv, parentWin, mycursor, user, product, target):
        super(Ui, self).__init__()
        uic.loadUi('assets/ui/followUp_CC.ui', self)
        self.setFixedSize(self.width(), self.height())
        self.show()

        self.priv = priv
        self.parentWin = parentWin
        self.mycursor = mycursor
        self.user = user
        self.prd = product
        self.table = "prod_"+product
        self.targetID = target

        self.initUI()

    def rtn(self):
        try:
            self.query = "UPDATE customers set fetched = false where id = %s;"
            self.mycursor.execute(self.query, (self.targetID,))
            self.mycursor.execute("commit;")
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)
        self.parentWin.show()
        self.close()

    def initUI(self):
        self.btn_return.clicked.connect(self.rtn)

        try:
            self.query = "SELECT "+self.table+".unique_code, nama, telp, bank, berkas, data_masuk, approval, data_id from " \
                        "customers left join "+self.table+" on id = " \
                        "cust_id where id = %s order by updated desc;"
            self.mycursor.execute(self.query,(self.targetID,))
            self.res = self.mycursor.fetchone()

            self.uniqueCode.setText(self.res[0])
            self.in_name.setText(self.res[1])
            self.in_phone.setText(self.res[2])
            self.in_bank.setText(self.res[3])
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

        if self.res[4]:
            self.chk_berkas.setChecked(True)
            self.chk_dataMasuk.setEnabled(True)
            self.berkas = self.res[4]
        if self.res[5]:
            self.chk_dataMasuk.setChecked(True)
            self.chk_Approve.setEnabled(True)
            self.chk_tidakApprove.setEnabled(True)
            self.dataMasuk = self.res[5]

        try:
            if self.res[6]==1:
                self.chk_Approve.setChecked(True)
                self.chk_tidakApprove.setChecked(False)
                self.approval = self.res[6]
            elif self.res[6]==0:
                self.chk_Approve.setChecked(False)
                self.chk_tidakApprove.setChecked(True)
                self.approval = self.res[6]
            else:
                self.chk_Approve.setChecked(False)
                self.chk_tidakApprove.setChecked(False)
                self.approval = self.res[6]
        except Exception as e:
            print(str(e))

        '''try:
            self.query = "UPDATE customers set fetched = True where id = %s;"
            self.mycursor.execute(self.query, (self.targetID,))
            self.mycursor.execute("commit;")
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)'''

        self.chk_berkas.toggled.connect(lambda: self.activateData(self.chk_dataMasuk, self.chk_berkas))
        self.chk_dataMasuk.toggled.connect(lambda: self.activateNext(self.chk_Approve, self.chk_dataMasuk, self.chk_tidakApprove))
        self.chk_Approve.toggled.connect(lambda: self.onlyOne(self.chk_tidakApprove, True))
        self.chk_tidakApprove.toggled.connect(lambda: self.onlyOne(self.chk_Approve, False))
        self.btn_save.clicked.connect(self.save)

    def save(self):
        try:
            self.query = "UPDATE customers set fetched = false where id = %s;"
            self.mycursor.execute(self.query, (self.targetID,))
            self.mycursor.execute("commit;")
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

        try:
            if self.approval != True:
                self.query = "update " + self.table + " set berkas = %s, data_masuk = %s, approval = %s, followup_date = curdate(), updater = %s where " \
                                                      "data_id = %s;"
            else:
                self.query = "update "+self.table+" set berkas = %s, data_masuk = %s, approval = %s, followup_date = curdate(), " \
                                                  "updater = %s, approval_date= curdate() where " \
                                                  "data_id = %s;"
            self.mycursor.execute(self.query, (self.berkas, self.dataMasuk, self.approval, self.user, self.res[7]))
            self.mycursor.execute("commit;")
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'Save Successful', "Data berhasil disimpan",
                                                     QtWidgets.QMessageBox.Ok)
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e), QtWidgets.QMessageBox.Ok)

        self.parentWin.show()
        self.close()

    def activateData(self, chk, selfchk):
        if selfchk.isChecked():
            self.berkas = True
            chk.setEnabled(True)
            #chk.setChecked(True)
        else:
            self.berkas = False
            chk.setEnabled(False)
            chk.setChecked(False)

    def activateNext(self, chk, selfchk, chk2):
        if selfchk.isChecked():
            self.dataMasuk = True
            chk.setEnabled(True)
            if chk2 != None:
                chk2.setEnabled(True)
        else:
            self.dataMasuk = False
            self.approval = False
            chk.setChecked(False)
            chk.setEnabled(False)
            if chk2 != None:
                chk2.setChecked(False)
                chk2.setEnabled(False)

    def onlyOne(self, aprv, aprval):
        aprv.setChecked(False)
        self.approval = aprval