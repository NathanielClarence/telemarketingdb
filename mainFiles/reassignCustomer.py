from PyQt5 import QtWidgets, uic

class Ui(QtWidgets.QWidget):
    def __init__(self, priv, mycursor, user, product, telle, telleid):
        super(Ui, self).__init__()
        uic.loadUi('assets/ui/reassign.ui', self)
        self.show()

        self.priv = priv
        self.mycursor = mycursor
        self.user = user
        self.product = product
        self.telle = telle
        self.telleid = telleid

        try:
            self.initUI()
        except Exception as e:
            print(str(e))
        self.setFixedSize(self.width(), self.height())

    def initUI(self):
        self.lbl_product.setText(self.product)
        self.lbl_name.setText(self.telle)
        self.btn_close.clicked.connect(self.closeWin)
        self.btn_assign.clicked.connect(self.assignTo)

        self.query = "SELECT id, nama, telp, alamat, asal_data, assigned_telle from assign_"+self.product+" left join (select id, nama" \
                     ", telp, alamat, asal_data from customers where id in (select cust_id from prod_"+self.product+" where updater" \
                     " = %s)) as cst on id = cust_id where id is not null;"
        self.mycursor.execute(self.query, (self.telleid,))
        self.result = self.mycursor.fetchall()
        #print(self.result)

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

    def closeWin(self):
        self.close()