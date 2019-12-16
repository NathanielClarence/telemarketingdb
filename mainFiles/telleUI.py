from PyQt5 import uic, QtWidgets
from searchHistory import Ui as srcHistory
from datetime import datetime
import sys

class Ui(QtWidgets.QWidget):
    def __init__(self, priv, parentWin, mycursor, user, product, target=None, recontact = None):
        super(Ui, self).__init__()
        uic.loadUi('assets/ui/telleUI.ui', self)
        self.setFixedSize(self.width(), self.height())
        self.show()

        self.priv = priv
        self.parentWin = parentWin
        self.mycursor = mycursor
        self.user = user
        self.prd = product
        self.table = "prod_"+product
        self.targetID = target
        self.recontact = recontact

        self.initUi()
        self.initAddCol()

        if self.recontact:
            self.btn_save.setEnabled(True)
            self.btn_save.setVisible(True)

    def initAddCol(self):
        try:
            self.query = "SELECT col FROM add_data;"
            self.mycursor.execute(self.query)
            self.addtColumn = self.mycursor.fetchall()
            if len(self.addtColumn) > 0:
                self.colAdded = []
                for x in self.addtColumn:
                    #self.nLabel =
                    self.insertData = QtWidgets.QLineEdit()
                    if self.priv == "adm":
                        self.insertData.setEnabled(True)
                    else:
                        self.insertData.setEnabled(False)
                    #print("dobon")
                    self.formLayout.addRow(QtWidgets.QLabel(x[0]), self.insertData)
                    #print("db")
                    self.colAdded.append(self.insertData)

            self.query = "SELECT "
            for x in range(len(self.addtColumn)):
                if x+1==len(self.addtColumn):
                    self.query += self.addtColumn[x][0].lower()+" "
                else:
                    self.query += self.addtColumn[x][0].lower() + ", "
            self.query += "from customers WHERE id = "+str(self.targetID)+";"
            self.mycursor.execute(self.query)
            self.dd = self.mycursor.fetchone()
            for x in range(len(self.colAdded)):
                self.colAdded[x].setText(self.dd[x])
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e), QtWidgets.QMessageBox.Ok)

    def initUi(self):
        self.btn_pickup.setVisible(False)
        self.btn_fpickup.setVisible(False)
        self.btn_info.setVisible(False)
        self.btn_finfo.setVisible(False)
        self.btn_interest.setVisible(False)
        self.btn_finterest.setVisible(False)
        self.btn_abstain.setVisible(False)
        self.lbl_bank.setVisible(False)
        self.cmb_banks.setVisible(False)
        self.lbl_hub.setVisible(False)
        self.in_recontact.setVisible(False)
        self.btn_save.setVisible(False)
        self.btn_next.setEnabled(False)
        self.in_dob.setMaximumDateTime(datetime.now())

        if self.priv != "adm":
            self.in_name.setEnabled(False)
            self.in_phone.setEnabled(False)
            self.in_ktp.setEnabled(False)
            self.in_alamat.setEnabled(False)
            self.in_cc.setEnabled(False)
            self.in_income.setEnabled(False)
            self.in_source.setEnabled(False)
            self.in_dob.setEnabled(False)
            self.btn_save.setVisible(False)
        else:
            self.btn_save.setEnabled(True)
            self.btn_save.setVisible(True)

        self.btn_cls.clicked.connect(self.closeWin)
        self.btn_next.clicked.connect(self.next)

        self.btn_connect.clicked.connect(self.cnt)
        self.btn_fconnect.clicked.connect(self.fcnt)
        self.btn_pickup.clicked.connect(self.pick)
        self.btn_fpickup.clicked.connect(self.fpick)
        self.btn_info.clicked.connect(self.inf)
        self.btn_finfo.clicked.connect(self.finf)
        self.btn_interest.clicked.connect(self.inter)
        self.btn_finterest.clicked.connect(self.finter)
        self.btn_abstain.clicked.connect(self.abs)
        self.btn_save.clicked.connect(self.save)
        self.btn_history.clicked.connect(self.openHistory)

        self.lbl_product.setText(self.prd.upper())

        #get customer data
        if self.targetID!= None:
            self.query = "select nama, telp, alamat, asal_data, no_ktp, penghasilan, unique_code, id, cc from customers where id = "+str(self.targetID)+";"
            self.btn_next.setVisible(False)
            self.btn_next.setEnabled(False)
        else:
            self.btn_save.setEnabled(False)
            self.query = "select nama, telp, alamat, asal_data, no_ktp, penghasilan, cst.unique_code, id, cc, date_of_birth from " \
                         "(select * from customers where fetched = false" \
                         ") as cst left join "+self.table+ \
                         " on id = cust_id where connected = true and note not like 'Tertarik' and cust_id not in " \
                         "(select cust_id from "+self.table+" where updated between" \
                         " date_sub(now(), interval 30 day) and now()) or cust_id is null and fetched = false order by updated;"
            # print(self.query)
        self.mycursor.execute(self.query)
        self.cust_data = self.mycursor.fetchone()

        try:
            self.query = "select data_id, connected, received, explained, note, unique_code, updated from "+self.table+" where " \
                            "cust_id = "+str(self.cust_data[7])+" order by updated;"
        # print(self.cust_data)
            self.mycursor.execute(self.query)
            self.n_data = self.mycursor.fetchone()
            try:
                self.connected = self.n_data[1]
                self.received = self.n_data[2]
                self.explained = self.n_data[3]
                self.note = self.n_data[4]
                if self.n_data[5]!= None:
                    self.uniqueCode.setText(self.n_data[5])
                    self.btn_follup.setEnabled(True)
            except:
                self.connected = None
                self.received = None
                self.explained = None
                self.note = None
                self.recontact = None
        except Exception as e:
            print(e)
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', "Belum ada data",
                                                     QtWidgets.QMessageBox.Ok)

        try:
            self.query = "update customers set fetched = true where id = " + str(self.cust_data[7]) + ";"
            #print(self.query)
            self.mycursor.execute(self.query)
            self.mycursor.execute("commit;")
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

        self.in_name.setText(self.cust_data[0])
        self.in_phone.setText(self.cust_data[1])
        self.in_ktp.setText(self.cust_data[4])
        self.in_alamat.setText(self.cust_data[2])
        self.in_cc.setText(self.cust_data[8])
        self.in_income.setText(self.cust_data[5])
        self.in_source.setText(self.cust_data[3])
        self.in_dob.setDate(self.cust_data[9])

    def openHistory(self):
        try:
            self.query = "select id, nama, telp, alamat, asal_data, fetched, no_ktp, penghasilan, " + self.table + ".unique_code, cc" \
                            ", updated, followup_date, note, berkas, data_masuk, approval, recontact from customers as cst left " \
                            "join prod_cc on id = cust_id where cust_id = %s order by updated;"
            self.mycursor.execute(self.query,(self.cust_data[7],))
            self.result = self.mycursor.fetchall()
            self.follow = QtWidgets.QWidget()
            self.follow.ui = srcHistory(self.priv, self, self.mycursor, self.result, self.user,
                                    self.prd)
        except Exception as e:
            print(e)
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

    def save(self):
        if self.in_source.text() != '' and self.in_phone.text() != '':
            try:
                self.data = []
                self.data.append(str(self.in_name.text()))
                self.data.append(str(self.in_phone.text()))
                self.data.append(str(self.in_alamat.toPlainText()))
                self.data.append(str(self.in_ktp.text()))
                self.data.append(str(self.in_income.text()))
                self.data.append(str(self.in_source.text()))
                #self.data.append(self.uniqueCode.text())
                self.data.append(str(self.in_cc.text()))
                self.data.append(self.in_dob.dateTime().toString('yyyy-MM-dd'))
                self.uniqueCd = self.uniqueCode.text()
                if self.uniqueCd == "":
                    self.uniqueCd = None
                for x in range(len(self.data)):
                    if self.data[x] == '':
                        self.data[x]=None

                self.query = "UPDATE customers set nama = %s, telp = %s, alamat = %s, asal_data = %s, no_ktp = %s, " \
                             "penghasilan = %s, cc = %s, date_of_birth = %s where id = " + str(self.cust_data[7]) +";"
                self.inse = (self.data[0], self.data[1], self.data[2], self.data[5], self.data[3], self.data[4], self.data[6], self.data[7])
                self.mycursor.execute(self.query, self.inse)
                self.mycursor.execute("commit;")
            except Exception as e:
                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                         QtWidgets.QMessageBox.Ok)

            #if self.uniqueCd!=None:
            self.prodData()

            self.btn_save.setEnabled(False)
        else:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', 'Phone number and source cannot be empty',
                                                     QtWidgets.QMessageBox.Ok)

        self.saveAddt()

    def saveAddt(self):
        self.newDat = []

        for x in self.colAdded:
            if x.text() == '':
                self.newDat.append(None)
            else:
                self.newDat.append(x.text())
        self.newDat = tuple(self.newDat)

        try:
            self.query = "UPDATE customers SET "
            for x in range(len(self.addtColumn)):
                if x+1==len(self.addtColumn):
                    self.query += self.addtColumn[x][0]+"= %s "
                else:
                    self.query += self.addtColumn[x][0] + "= %s, "
            self.query += "WHERE id = "+str(self.cust_data[7])+";"
            self.mycursor.execute(self.query, self.newDat)
            self.mycursor.execute("commit;")
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e), QtWidgets.QMessageBox.Ok)

    def prodData(self):
        try:
            if self.note == "Pikir-pikir":
                self.recontact = self.in_recontact.dateTime().toString('yyyy-MM-dd hh:mm:ss')
            else:
                self.recontact = None
            self.bankChoice = str(self.cmb_banks.currentText())
            self.query = "insert into "+self.table+" (cust_id, connected, received, explained, note, unique_code, updated, updater, recontact, bank) values" \
                                                    "(%s,"+str(self.connected)+","+str(self.received)+","+str(self.explained)+"" \
                                                    ",%s,%s, curdate(), %s, %s, %s);"
            self.uniqueCd = self.uniqueCode.text()
            if self.uniqueCd == "":
                self.uniqueCd = None
            self.mycursor.execute(self.query, (str(self.cust_data[7]),self.note,self.uniqueCd, self.user, self.recontact, self.bankChoice))
            self.mycursor.execute("commit;")
        except Exception as e:
            print(str(e))
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

    def abs(self):
        self.note = "Pikir-pikir"
        self.lbl_hub.setVisible(True)
        self.in_recontact.setVisible(True)
        self.in_recontact.setEnabled(True)
        self.btn_next.setEnabled(True)
        self.in_recontact.setDateTime(datetime.now())

    def finter(self):
        self.note = "Tidak"
        self.btn_interest.setEnabled(False)
        self.btn_finterest.setEnabled(False)
        self.btn_abstain.setEnabled(False)
        self.btn_next.setEnabled(True)

    def inter(self):
        self.note = "Tertarik"
        print(self.note)
        self.prod = self.prd.upper()
        self.cd = self.cust_data[6][:4]+"/"+self.prod+self.cust_data[6][4:]
        try:
            self.uniqueCode.setText(self.cd)
        except Exception as e:
            print(e)
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)
        #print(self.uniqueCode.text())
        print(self.note)
        self.btn_interest.setEnabled(False)
        self.btn_finterest.setEnabled(False)
        self.btn_abstain.setEnabled(False)
        self.lbl_bank.setVisible(True)
        self.cmb_banks.setVisible(True)
        #self.btn_next.setEnabled(True)

        try:
            self.query = "SELECT nama_bank from bank_"+self.prd+";"
            self.mycursor.execute(self.query)
            self.banks = self.mycursor.fetchall()
            for x in self.banks:
                self.cmb_banks.addItem(x[0])
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

    def finf(self):
        self.explained = False
        self.btn_info.setEnabled(False)
        self.btn_finfo.setEnabled(False)
        self.btn_next.setEnabled(True)

    def inf(self):
        self.explained = True
        self.btn_info.setEnabled(False)
        self.btn_finfo.setEnabled(False)
        self.btn_interest.setVisible(True)
        self.btn_finterest.setVisible(True)
        self.btn_abstain.setVisible(True)
        self.btn_interest.setEnabled(True)
        self.btn_finterest.setEnabled(True)
        self.btn_abstain.setEnabled(True)

    def fpick(self):
        self.received = False
        self.btn_pickup.setEnabled(False)
        self.btn_fpickup.setEnabled(False)
        self.btn_next.setEnabled(True)

    def pick(self):
        self.received = True
        self.btn_pickup.setEnabled(False)
        self.btn_fpickup.setEnabled(False)
        self.btn_info.setVisible(True)
        self.btn_finfo.setVisible(True)
        self.btn_info.setEnabled(True)
        self.btn_finfo.setEnabled(True)

    def fcnt(self):
        self.connected=False
        self.btn_fconnect.setEnabled(False)
        self.btn_connect.setEnabled(False)
        self.btn_next.setEnabled(True)

    def cnt(self):
        self.connected = True
        self.btn_connect.setEnabled(False)
        self.btn_fconnect.setEnabled(False)
        self.btn_pickup.setVisible(True)
        self.btn_fpickup.setVisible(True)
        self.btn_pickup.setEnabled(True)
        self.btn_fpickup.setEnabled(True)

    def closeWin(self):
        self.query = "update customers set fetched = false where id = %s;"
        self.mycursor.execute(self.query,(str(self.cust_data[7]),))
        self.mycursor.execute("commit;")

        '''if self.uniqueCode.text() != '':
            self.prodData()
        else:
            try:
                self.query = "insert into "+self.table+" (cust_id, connected, received, explained, note, updated) values" \
                                                        "(%s,"+str(self.connected)+","+str(self.received)+","+str(self.explained)+"" \
                                                        ",%s, curdate());"
                self.mycursor.execute(self.query, (str(self.cust_data[7]),self.note))
                self.mycursor.execute("commit;")
            except Exception as e:
                print(str(e))'''

        self.parentWin.show()
        self.close()

    def next(self):
        self.query = "update customers set fetched = false where id = %s;"
        self.mycursor.execute(self.query, (str(self.cust_data[7]),))
        self.mycursor.execute("commit;")
        self.uniqueCd = self.uniqueCode.text()
        if self.uniqueCode.text() != '':
            self.prodData()
        else:
            try:
                self.query = "insert into "+self.table+" (cust_id, connected, received, explained, note, updated, updater) values" \
                                                        "(%s,"+str(self.connected)+","+str(self.received)+","+str(self.explained)+"" \
                                                        ",%s, curdate(), %s);"
                self.mycursor.execute(self.query, (str(self.cust_data[7]),self.note, self.user))
                self.mycursor.execute("commit;")
            except Exception as e:
                print(str(e))
                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                         QtWidgets.QMessageBox.Ok)
        self.nextCust = QtWidgets.QWidget()
        self.nextCust.ui = Ui(self.priv, self.parentWin, self.mycursor, self.user, self.prd)
        self.close()
        #ambil lagi dari result yang fetched = 0, set yang ini fetched = 1
        #waktu insert updated
        #self.parentWin

'''if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    premain = QtWidgets.QMainWindow()
    premain.ui = Ui()
    sys.exit(app.exec_())'''