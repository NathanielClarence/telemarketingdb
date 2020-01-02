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
                     " = %s)) as cst on id = cust_id where id is not null;"
        self.mycursor.execute(self.query, (self.cmb_telle.currentText(),))
        self.result = self.mycursor.fetchall()

        self.tableWidget.setRowCount(len(self.result))
        self.tableWidget.setColumnCount(len(self.result[0]))

        self.checkboxList = []

        self.vLayout = QtWidgets.QVBoxLayout(self.scrollArea)

        for x in range(len(self.result)):
            for y in range(len(self.result[x])):
                self.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(self.result[x][y])))
            self.cb = QtWidgets.QCheckBox(str(self.result[x][0]))
            self.checkboxList.append(self.cb)
            self.vLayout.addWidget(self.cb)

        self.cmb_product.currentIndexChanged.connect(self.refreshUser)
        self.cmb_telle.currentIndexChanged.connect(self.refreshDB)
        self.lbl_totalData.setText(str(len(self.result)))

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

        self.query = "select id, nama, telp, alamat, asal_data, assigned_telle from assign_" + self.cmb_product.currentText() + " left join (select id, nama" \
                    ", telp, alamat, asal_data from customers where id not in (select cust_id from prod_" + self.cmb_product.currentText() + " where updater" \
                    " = %s)) as cst on id = cust_id where id is not null;"
        self.mycursor.execute(self.query, (self.cmb_telle.currentText(),))
        self.result = self.mycursor.fetchall()

        self.tableWidget.setRowCount(len(self.result))
        self.tableWidget.setColumnCount(len(self.result[0]))

        self.checkboxList = []

        #self.vLayout.setParent(None)
        self.vLayout = QtWidgets.QVBoxLayout(self.scrollArea)
        for x in range(len(self.result)):
            for y in range(len(self.result[x])):
                self.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(self.result[x][y])))
            self.cb = QtWidgets.QCheckBox(str(self.result[x][0]))
            self.checkboxList.append(self.cb)
            self.vLayout.addWidget(self.cb)

        self.lbl_totalData.setText(str(len(self.result)))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    premain = QtWidgets.QWidget()
    premain.ui = Ui()
    sys.exit(app.exec_())