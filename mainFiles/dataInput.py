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
        self.show()

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
        self.in_source.setToolTip('<b>Asal data</b> harus diisi')
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

    '''def alterDB(self):
        self.altDB = QtWidgets.QWidget
        self.altDB.ui = addCol(self.mycursor, self)'''

    def rebindUniqueNum(self):
        try:
            self.mycursor.execute("SELECT max(id) FROM CUSTOMERS;")
            self.result = self.mycursor.fetchone()
            self.unicode = datetime.date.today().strftime("%y") + datetime.date.today().strftime("%m") + "/" + str(
                self.result[0] + 1).zfill(9)
            self.uniqueCode.setText(self.unicode)
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

    def addSingle(self):
        if self.in_phone.text() == '' or self.in_source == '':
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', 'Phone number and source cannot be empty', QtWidgets.QMessageBox.Ok)
        else:
            self.insData = []
            self.insData.append(str(self.unicode))
            self.insData.append(str(self.in_name.text()))
            self.insData.append(str(self.in_phone.text()))
            self.insData.append(str(self.in_id.text()))
            self.insData.append(self.in_dob.dateTime().toString('yyyy-MM-dd'))
            self.insData.append(str(self.in_address.toPlainText()))
            self.insData.append(str(self.in_cc.text()))
            self.insData.append(str(self.in_earning.text()))
            self.insData.append(str(self.in_source.text()))

            for x in range(len(self.insData)):
                if self.insData[x]=='':
                    self.insData[x]=None

            #print(self.insData)

            try:
                self.query = "INSERT INTO CUSTOMERS (unique_code, nama, telp, no_ktp, date_of_birth, alamat, cc, penghasilan, " \
                             "asal_data) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
                self.mycursor.execute(self.query, tuple(self.insData))
                self.mycursor.execute("commit;")

                if len(self.addColumns)!=0:
                    self.addtData()

                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'Tambah Data', "Data berhasil ditambahkan",
                                                         QtWidgets.QMessageBox.Ok)
            except Exception as e:
                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                         QtWidgets.QMessageBox.Ok)
            finally:
                self.in_name.setText("")
                self.in_phone.setText("")
                self.in_id.setText("")
                self.in_address.setText("")
                self.in_cc.setText("")
                self.in_earning.setText("")
                self.in_source.setText("")
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
        print(self.ans)
        print(self.query)
        try:
            self.mycursor.execute(self.query, tuple(self.ans))
            self.mycursor.execute("commit;")
        except Exception as e:
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
                self.inputList = [self.in_name, self.in_phone, self.in_id, self.in_dob, self.in_address, self.in_cc,
                                  self.in_earning, self.in_source]

                while self.cntrow < self.rows:
                    self.listData = []
                    self.inpt = 0
                    for x in self.dictData:
                        self.listData.append(self.dictData.get(x)[self.cntrow])
                        if self.inpt == 3:
                            self.inputList[self.inpt].setDate(datetime.datetime.strptime(self.dictData.get(x)[self.cntrow], '%d/%m/%Y'))
                        elif self.inpt ==1:
                            self.inputList[self.inpt].setText('0'+str(self.dictData.get(x)[self.cntrow]))
                        else:
                            self.inputList[self.inpt].setText(str(self.dictData.get(x)[self.cntrow]))
                        self.inpt+=1
                    #print(self.listData)
                    self.addSingle()
                    self.cntrow += 1

                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'Import Data', "Data berhasil diimport",
                                                         QtWidgets.QMessageBox.Ok)
            except Exception as e:
                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                         QtWidgets.QMessageBox.Ok)

    '''def importXLS(self):
        print("import xls, all rows (depends on how many cols customers table need)")
        print("query: insert into customers(..., add.data) values (...,...,...), change '' to None")
        print("update again this window's unique code")'''

'''if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    premain = QtWidgets.QWidget()
    premain.ui = Ui()
    sys.exit(app.exec_())'''