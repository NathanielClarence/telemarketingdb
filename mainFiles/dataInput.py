from PyQt5 import QtWidgets, uic, QtGui, QtCore
from searchUser import Ui as searchCust
#from addBank import Ui as addBnk
#from addColumn import Ui as addCol
import datetime
import pandas as pd
import re
import sys

class Ui(QtWidgets.QWidget):
    def __init__(self, priv, parentWin, mycursor, user):
        super(Ui, self).__init__()
        uic.loadUi('assets/ui/adminData.ui', self)
        self.showFullScreen()
        self.scrollArea.setGeometry(self.scrollArea.geometry().x(), self.scrollArea.geometry().x(), self.width() - 20,
                                    self.height() - 20)

        self.priv = priv
        self.addData = []
        self.addColumns = []
        self.parentWin = parentWin
        self.mycursor = mycursor
        self.user = user

        self.rebindUniqueNum()
        self.initUI()
        self.setFixedSize(self.width(), self.height())

    def initUI(self):
        self.mycursor.execute("SELECT * FROM add_data;")
        self.result = self.mycursor.fetchall()
        for x in self.result:
            self.addRow(x[0])
            self.addColumns.append(x[0])

        self.lbl_gap.setVisible(False)
        QtWidgets.QToolTip.setFont(QtGui.QFont('Serif', 9))
        self.in_phone.setToolTip('<b>No HP</b> harus diisi')
        self.cmb_source.setToolTip('<b>Asal data</b> harus diisi')
        self.btn_addData.clicked.connect(self.addSingle)
        '''if self.priv == 'adm':
            self.btn_addCol.setVisible(True)
            self.btn_addCol.setEnabled(True)
            self.btn_addCol.clicked.connect(self.alterDB)
        else:
            self.btn_addCol.setVisible(False)
            self.btn_addCol.setEnabled(False)'''
        # self.btn_import.clicked.connect(self.importXLS)
        #self.btn_addBank.clicked.connect(self.tambahBank)
        self.btn_update.clicked.connect(self.updateCustomer)
        self.btn_clsWin.clicked.connect(self.clsWin)
        self.in_dob.setMaximumDateTime(datetime.datetime.now())
        self.btn_import.clicked.connect(self.importDB)

        self.query = "select kode_produk from products;"
        self.mycursor.execute(self.query)
        self.products = self.mycursor.fetchall()
        self.products = tuple(self.products)
        self.GetBankDatas()

    '''def alterDB(self):
        self.altDB = QtWidgets.QWidget
        self.altDB.ui = addCol(self.mycursor, self)'''

    def rebindUniqueNum(self):
        try:
            self.mycursor.execute("SELECT max(id) FROM CUSTOMERS;")
            self.result = self.mycursor.fetchone()
            if self.result[0] != None:
                self.unicode = datetime.date.today().strftime("%y") + datetime.date.today().strftime("%m") + "/" + str(
                    self.result[0] + 1).zfill(9)
            else:
                self.unicode = datetime.date.today().strftime("%y") + datetime.date.today().strftime("%m") + "/" + str(1).zfill(9)
            self.uniqueCode.setText(self.unicode)
        except Exception as e:
            print("rebind")
            print(len(self.result))
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

    '''def addSingle(self):
        self.phone = str(self.in_phone.text())
        self.phone = re.sub('[^0-9]+', '',re.sub("\+62", '0', self.phone))
        print(self.phone)
        if self.phone.isnumeric():
            print("True")
        else:
            print("Try Again")'''
        #print(self.phone)

    def addSingle(self, s=0):
        self.phone = str(self.in_phone.text())
        self.phone = re.sub('[^0-9]+', '', re.sub("\+62", '0', self.phone))
        if self.phone == '':
            #print("Masuk add single self.phone if")
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', 'Phone number cannot be empty', QtWidgets.QMessageBox.Ok)
        else:
            try:
                if not self.phone.isnumeric():
                    raise Exception("Invalid phone number "+self.in_phone.text())

                self.insData = []
                self.insData.append(str(self.unicode))
                self.insData.append(str(self.in_name.text()))
                self.insData.append(self.phone)
                #self.insData.append(str(self.in_id.text()))
                self.insData.append(self.in_dob.dateTime().toString('yyyy-MM-dd'))
                self.insData.append(str(self.in_address.toPlainText()))
                self.insData.append(str(self.in_merek.text()))
                self.insData.append(str(self.in_tipe.text()))
                self.insData.append(str(self.in_tahun.text()))
                self.insData.append(str(self.in_nopol.text()))
                self.insData.append(str(self.cmb_source.currentText()))

                for x in range(len(self.insData)):
                    if self.insData[x]=='':
                        self.insData[x]=None

                #self.query = "INSERT INTO CUSTOMERS (unique_code, nama, telp, no_ktp, date_of_birth, alamat, cc, penghasilan, " \
                #             "asal_data) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"

                self.query = "INSERT INTO CUSTOMERS (unique_code, nama, telp, date_of_birth, alamat, merek_mobil, tipe_mobil, " \
                             "tahun_mobil, nopol, asal_data) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                self.mycursor.execute(self.query, tuple(self.insData))

                self.query = "select max(id) from customers;"
                self.mycursor.execute(self.query)
                self.result = self.mycursor.fetchone()

                self.query = "select kode_produk from products;"
                self.mycursor.execute(self.query)
                self.productRes = self.mycursor.fetchall()

                for x in self.productRes:
                    self.query = "insert into assign_"+str(x[0])+" (cust_id, assigned_telle, times_assigned) values ('"+str(self.result[0])+"'" \
                                 ", 'None', '0');"
                    self.mycursor.execute(self.query)
                self.mycursor.execute("commit;")

                if len(self.addColumns)!=0:
                    self.addtData()

                if s == 0:
                    self.buttonReply = QtWidgets.QMessageBox
                    self.warning = self.buttonReply.question(self, 'Tambah Data', "Data berhasil ditambahkan",
                                                             QtWidgets.QMessageBox.Ok)
            except Exception as e:
                print(e)
                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                         QtWidgets.QMessageBox.Ok)
            finally:
                self.in_name.setText("")
                self.in_phone.setText("")
                #self.in_id.setText("")
                self.in_dob.setDate(QtCore.QDate(2000, 1, 1))
                self.in_address.setText("")
                #self.in_cc.setText("")
               # self.in_earning.setText("")
                self.cmb_source.setCurrentIndex(0)
                self.in_merek.setText("")
                self.in_tipe.setText("")
                self.in_tahun.setText("")
                self.in_nopol.setText("")
                self.rebindUniqueNum()

    def addtData(self):
        self.query = "UPDATE customers SET "
        for x in range(len(self.addColumns)):
            if x+1 == len(self.addColumns):
                self.query += self.addColumns[x]+"= %s"
            else:
                self.query += self.addColumns[x]+"= %s, "
        self.query += " WHERE unique_code = %s;"
        self.ans = []
        for x in self.addData:
            if x.text()=="":
                self.ans.append(None)
            else:
                self.ans.append(str(x.text()))
            x.setText("")
        self.ans.append(self.insData[0])
        '''print(self.ans)
        print(self.query)
        print(str(tuple(self.ans)))'''
        try:
            self.mycursor.execute(self.query, tuple(self.ans))
            self.mycursor.execute("commit;")
        except Exception as e:
            print(e)
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

    def clsWin(self):
        self.parentWin.show()
        self.close()

    def addRow(self, rowname):
        self.newData = QtWidgets.QLineEdit()
        self.addData.append(self.newData)
        self.formLayout.addRow(QtWidgets.QLabel(rowname), self.newData)

    def updateCustomer(self):
        self.searchWin = QtWidgets.QWidget()
        self.searchWin.ui = searchCust(self.priv, self, self.mycursor, self.user)
        self.hide()

    '''def tambahBank(self):
        self.addBank = QtWidgets.QWidget()
        self.addBank.ui = addBnk(self.mycursor)'''

    def importDB(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Import From Excel", "",
                                                            "Excel Files (*.xlsx);;Excel 97-2003 (*.xls)", options=options)
        if fileName:
            #print(fileName)
            try:
                self.df = pd.read_excel(fileName, sheet_name="Sheet1")
                self.dictData = {}
                for x in self.df:
                    self.listData = []
                    if x.lower() != 'no':
                        for y in self.df[x]:
                            self.listData.append(y)
                        self.dictData[x] = self.listData
                    if x.lower() == 'no hp':
                        self.rows = self.df.count()[x]

                self.cntrow = 0
                self.inputList = [self.in_name, self.in_phone, self.in_dob, self.in_address, self.in_merek, self.in_tipe,
                                  self.in_tahun, self.in_nopol, self.cmb_source]

                self.isBankExist = False
                #print(self.cntrow)
                #print(self.rows)
                while self.cntrow < self.rows:
                    self.listData = []
                    self.inpt = 0
                    for x in self.dictData:
                        print(self.inpt)
                        self.listData.append(self.dictData.get(x)[self.cntrow])
                        if self.inpt == 2:
                            #try:
                            self.inputList[self.inpt].setDate(datetime.datetime.strptime(self.dictData.get(x)[self.cntrow], '%d/%m/%Y'))
                            #except:
                            #self.inputList[self.inpt].setDate(datetime.datetime.strptime('01/01/2000', '%d/%m/%Y'))
                        elif self.inpt == 1:
                            #if self.dictData.get(x)[self.cntrow] ==
                            self.inputList[self.inpt].setText('0'+str(self.dictData.get(x)[self.cntrow]))
                        elif self.inpt == 8:
                            for y in self.banks:
                                if y == str(self.dictData.get(x)[self.cntrow]):
                                    self.isBankExist = True
                                    self.inputList[self.inpt].setCurrentText(str(self.dictData.get(x)[self.cntrow]))
                                    break
                        else:
                            self.inputList[self.inpt].setText(str(self.dictData.get(x)[self.cntrow]))
                        self.inpt+=1
                    #print(self.listData)

                    if self.isBankExist:
                        self.addSingle(s=1)
                    else:
                        self.buttonReply = QtWidgets.QMessageBox
                        self.warning = self.buttonReply.question(self, 'WARNING',
                                                                 'Asal data untuk nomor HP: '+str(self.inputList[1].text())+' tidak sesuai.',
                                                                 QtWidgets.QMessageBox.Ok)

                    self.cntrow += 1

                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'Import Data', "Data berhasil diimport",
                                                         QtWidgets.QMessageBox.Ok)
            except Exception as e:
                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                         QtWidgets.QMessageBox.Ok)
                print("ss")

    def GetBankDatas(self):
        self.banks=[]
        for x in self.products:
            self.query = "select nama_bank from bank_" +  x[0]
            self.mycursor.execute(self.query)
            self.bank_prod = self.mycursor.fetchall()

            for y in self.bank_prod:
                self.banks.append(y[0])
        self.banks = ("Koran",) +tuple(self.banks)

        for z in self.banks:
            self.cmb_source.addItem(z)
    '''def importXLS(self):
        print("import xls, all rows (depends on how many cols customers table need)")
        print("query: insert into customers(..., add.data) values (...,...,...), change '' to None")
        print("update again this window's unique code")'''

'''if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    premain = QtWidgets.QWidget()
    premain.ui = Ui()
    sys.exit(app.exec_())'''