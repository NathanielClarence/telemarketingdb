from PyQt5 import QtWidgets, uic
from reassignCustomer import Ui as reassign
'''import mysql.connector as conn
import sys'''

class Ui(QtWidgets.QWidget):
    def __init__(self, priv, parentWin, mycursor, user):
        super(Ui, self).__init__()
        uic.loadUi('assets/ui/assignCustomer.ui', self)
        self.showFullScreen()
        self.scrollArea_2.setGeometry(self.scrollArea_2.geometry().x(), self.scrollArea_2.geometry().x(), self.width() - 40,
                                    self.height() - 40)

        self.priv = priv
        #self.addData = []
        #self.addColumns = []
        self.parentWin = parentWin
        self.mycursor = mycursor
        self.user = user

        try:
            self.initUI()
        except Exception as e:
            print(str(e))
        self.setFixedSize(self.width(), self.height())

    def initUI(self):
        self.query = "select kode_produk from products;"
        self.mycursor.execute(self.query)
        self.result = self.mycursor.fetchall()

        for x in self.result:
            self.cmb_product.addItem(x[0])

        self.query = "select username, name from admins where privilege = 'telle' and active_status = 1 and product = %s;"
        self.mycursor.execute(self.query, (self.cmb_product.currentText(),))
        self.resultUser = self.mycursor.fetchall()
        for x in self.resultUser:
            self.cmb_telle.addItem(x[0])
        self.telle_name.setText(str(self.resultUser[self.cmb_telle.currentIndex()][1]))
        self.checkboxList = []
        self.vLayout = self.scrollAreaWidgetContents.layout()

        try:
            self.query = "select id, nama, telp, alamat, asal_data, assigned_telle from assign_"+self.cmb_product.currentText()+" left join (select id, nama" \
                         ", telp, alamat, asal_data from customers where id not in (select cust_id from prod_"+self.cmb_product.currentText()+" where updater" \
                         " = %s)) as cst on id = cust_id where id is not null and assign_date < date_sub(now(), interval 1 month) and times_assigned < 4 or " \
                         "assign_date is null;"
            self.mycursor.execute(self.query, (self.cmb_telle.currentText(),))
            self.result = self.mycursor.fetchall()

            if len(self.result) == 0:
                raise Exception("No data to show for this user.")
            #print("bocor")

            self.tableWidget.setRowCount(len(self.result))
            self.tableWidget.setColumnCount(len(self.result[0]))

            for x in range(len(self.result)):
                for y in range(len(self.result[x])):
                    self.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(self.result[x][y])))
                self.cb = QtWidgets.QCheckBox(str(self.result[x][0]))
                self.checkboxList.append(self.cb)
                self.vLayout.addWidget(self.cb)
        except Exception as e:
            print(e)
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

        self.cmb_product.currentTextChanged.connect(self.refreshUser)
        self.cmb_telle.currentTextChanged.connect(self.refreshDB)
        self.lbl_totalData.setText(str(len(self.result)))
        self.btn_partAssign.clicked.connect(self.partialAssign)
        self.btn_assign.clicked.connect(self.assignTo)
        self.btn_back.clicked.connect(self.closeWin)
        self.btn_reassign.clicked.connect(self.reassignCustomers)

    def reassignCustomers(self):
        self.assignUlang = QtWidgets.QWidget()
        self.assignUlang.ui = reassign(self.priv, self.mycursor, self.user, self.cmb_product.currentText(),
                                       self.telle_name.text(), self.cmb_telle.currentText())

    def closeWin(self):
        self.parentWin.show()
        self.close()

    def assignTo(self):
        self.selected = []
        for x in self.checkboxList:
            if x.isChecked():
                #self.selected.append(x.text())
                self.query = "UPDATE ASSIGN_"+self.cmb_product.currentText()+" set assigned_telle = %s, times_assigned = " \
                             "times_assigned +1, assign_date = current_timestamp where cust_id = %s;"
                self.mycursor.execute(self.query, (self.cmb_telle.currentText(),x.text()))
                self.mycursor.execute("commit;")

        self.refreshDB()

    def partialAssign(self):
        try:
            for x in self.checkboxList:
                x.setChecked(False)
            self.iteration = int(self.in_check.text())
            if self.iteration > int(self.lbl_totalData.text()):
                raise Exception("Input tidak boleh lebih besar dari "+str(self.lbl_totalData.text()))

            for x in range(self.iteration):
                self.checkboxList[x].setChecked(True)
        except Exception as e:
            print(e)
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

    def refreshUser(self):
        try:
            self.cmb_telle.clear()
            self.query = "select username, name from admins where privilege = 'telle' and active_status = 1 and product = %s;"
            self.mycursor.execute(self.query, (self.cmb_product.currentText(),))
            self.resultUser = self.mycursor.fetchall()
            #print(self.resultUser)
            for x in self.resultUser:
                self.cmb_telle.addItem(x[0])
            self.telle_name.setText(str(self.resultUser[self.cmb_telle.currentIndex()][1]))
        except Exception as e:
            print("user")
            print(str(e))
        #self.refreshDB()

    def refreshDB(self):
        try:
            self.tableWidget.setRowCount(0)
            for x in self.checkboxList:
                x.setParent(None)
                #self.vLayout.removeItem(x)
                self.vLayout.removeWidget(x)
            self.telle_name.setText(str(self.resultUser[self.cmb_telle.currentIndex()][1]))

            self.query = "select id, nama, telp, alamat, asal_data, assigned_telle from assign_"+self.cmb_product.currentText()+" left join (select id, nama" \
                         ", telp, alamat, asal_data from customers where id not in (select cust_id from prod_"+self.cmb_product.currentText()+" where updater" \
                         " = %s)) as cst on id = cust_id where id is not null and assign_date < date_sub(now(), interval 1 month) and times_assigned < 4 or " \
                         "assign_date is null;"
            self.mycursor.execute(self.query, (self.cmb_telle.currentText(),))
            self.result = self.mycursor.fetchall()

            if len(self.result) == 0:
                raise Exception("No data to show for this user.")
            #print("bocor")
            self.tableWidget.setRowCount(len(self.result))
            self.tableWidget.setColumnCount(len(self.result[0]))

            self.checkboxList = []

            #self.vLayout = QtWidgets.QVBoxLayout(self.scrollArea)
            if len(self.result)!=0:
                for x in range(len(self.result)):
                    for y in range(len(self.result[x])):
                        self.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(self.result[x][y])))
                    self.cb = QtWidgets.QCheckBox(str(self.result[x][0]))
                    #print(str(self.result[x][0]))
                    self.checkboxList.append(self.cb)
                    self.vLayout.addWidget(self.cb)

            self.lbl_totalData.setText(str(len(self.result)))
        except Exception as e:
            #print("db")
            #print(str(e))
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)
        #print(str(self.checkboxList))

'''if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    premain = QtWidgets.QWidget()
    premain.ui = Ui()
    sys.exit(app.exec_())'''