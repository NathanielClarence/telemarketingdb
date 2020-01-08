from PyQt5 import QtWidgets, uic
import mysql.connector as conn
import sys

class Ui(QtWidgets.QWidget):
    def __init__(self):#, priv, parentWin, mycursor, user):
        super(Ui, self).__init__()
        uic.loadUi('assets/ui/assignCustomer.ui', self)
        self.show()

        '''self.priv = priv
        self.addData = []
        self.addColumns = []
        self.parentWin = parentWin
        self.mycursor = mycursor
        self.user = user'''

        try:
            self.initUI()
        except Exception as e:
            print(str(e))
        self.setFixedSize(self.width(), self.height())

    def initUI(self):
        self.mydb = conn.connect(
            host="localhost",
            user='root',
            passwd='root',
            database="dbtest",
            auth_plugin='mysql_native_password',
            buffered=True
        )
        self.mycursor = self.mydb.cursor()

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

        self.query = "select id, nama, telp, alamat, asal_data, assigned_telle from assign_"+self.cmb_product.currentText()+" left join (select id, nama" \
                     ", telp, alamat, asal_data from customers where id not in (select cust_id from prod_"+self.cmb_product.currentText()+" where updater" \
                     " = %s)) as cst on id = cust_id where id is not null and assign_date < date_sub(now(), interval 1 month) and times_assigned < 4;"
        self.mycursor.execute(self.query, (self.cmb_telle.currentText(),))
        self.result = self.mycursor.fetchall()

        self.tableWidget.setRowCount(len(self.result))
        self.tableWidget.setColumnCount(len(self.result[0]))

        self.checkboxList = []

        self.vLayout = self.scrollAreaWidgetContents.layout()

        for x in range(len(self.result)):
            for y in range(len(self.result[x])):
                self.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(self.result[x][y])))
            self.cb = QtWidgets.QCheckBox(str(self.result[x][0]))
            self.checkboxList.append(self.cb)
            self.vLayout.addWidget(self.cb)

        self.cmb_product.currentIndexChanged.connect(self.refreshUser)
        self.cmb_telle.currentIndexChanged.connect(self.refreshDB)
        self.lbl_totalData.setText(str(len(self.result)))
        self.btn_partAssign.clicked.connect(self.partialAssign)
        self.btn_assign.clicked.connect(self.assignTo)

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
        for x in self.checkboxList:
            x.setChecked(False)
        self.iteration = int(self.in_check.text())
        for x in range(self.iteration):
            self.checkboxList[x].setChecked(True)

    def refreshUser(self):
        self.cmb_telle.clear()
        self.query = "select username, name from admins where privilege = 'telle' and active_status = 1 and product = %s;"
        self.mycursor.execute(self.query, (self.cmb_product.currentText(),))
        self.resultUser = self.mycursor.fetchall()
        #print(self.resultUser)
        for x in self.resultUser:
            self.cmb_telle.addItem(x[0])
        self.telle_name.setText(str(self.resultUser[self.cmb_telle.currentIndex()][1]))

        self.refreshDB()

    def refreshDB(self):
        '''self.query = "select username, name from admins where privilege = 'telle' and active_status = 1 and product = %s;"
        self.mycursor.execute(self.query, (self.cmb_product.currentText(),))
        self.resultUser = self.mycursor.fetchall()
        for x in self.resultUser:
            self.cmb_telle.addItem(x[0])'''
        self.telle_name.setText(str(self.resultUser[self.cmb_telle.currentIndex()][1]))

        self.query = "select id, nama, telp, alamat, asal_data, assigned_telle from assign_"+self.cmb_product.currentText()+" left join (select id, nama" \
                     ", telp, alamat, asal_data from customers where id not in (select cust_id from prod_"+self.cmb_product.currentText()+" where updater" \
                     " = %s)) as cst on id = cust_id where id is not null and assign_date < date_sub(now(), interval 1 month) and times_assigned < 4;"
        self.mycursor.execute(self.query, (self.cmb_telle.currentText(),))
        self.result = self.mycursor.fetchall()

        self.tableWidget.setRowCount(len(self.result))
        self.tableWidget.setColumnCount(len(self.result[0]))

        for x in self.checkboxList:
            x.setParent(None)
            #self.vLayout.removeItem(x)
            self.vLayout.removeWidget(x)

        self.checkboxList = []

        #self.vLayout = QtWidgets.QVBoxLayout(self.scrollArea)
        for x in range(len(self.result)):
            for y in range(len(self.result[x])):
                self.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(self.result[x][y])))
            self.cb = QtWidgets.QCheckBox(str(self.result[x][0]))
            #print(str(self.result[x][0]))
            self.checkboxList.append(self.cb)
            self.vLayout.addWidget(self.cb)

        self.lbl_totalData.setText(str(len(self.result)))
        #print(str(self.checkboxList))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    premain = QtWidgets.QWidget()
    premain.ui = Ui()
    sys.exit(app.exec_())