from PyQt5 import uic, QtWidgets
from historyResult import Ui as srcRes

class Ui(QtWidgets.QWidget):
    def __init__(self, priv, parentWin, mycursor, user):
        super(Ui, self).__init__()
        uic.loadUi('assets/ui/searchUser.ui', self)
        self.setFixedSize(self.width(), self.height())
        self.show()

        self.priv = priv
        self.mycursor = mycursor
        self.parentWin = parentWin
        self.user = user

        self.btn_cancel.clicked.connect(self.cancelSearch)
        self.btn_search.clicked.connect(self.searchUser)

        if self.priv == "adm":
            self.cmb_prod.setEnabled(True)
            try:
                self.mycursor.execute("SELECT KODE_PRODUK FROM PRODUCTS;")
                self.res = self.mycursor.fetchall()
                for prd in self.res:
                    self.cmb_prod.addItem(prd[0])
            except Exception as e:
                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'WARNING', str(e), QtWidgets.QMessageBox.Ok)
        else:
            self.mycursor.execute("SELECT product FROM admins where username like %s;",(self.user,))
            self.res = self.mycursor.fetchone()
            self.cmb_prod.addItem(self.res[0].upper())

    def cancelSearch(self):
        self.parentWin.show()
        self.close()

    def searchUser(self):
        self.uniqueCode = self.in_uniCode.text()
        self.name = self.in_name.text()
        self.phone = self.in_phone.text()
        self.product = self.cmb_prod.currentText()
        if self.name =='':
            self.name = None
        else:
            self.name = "%"+self.name+"%"
        if self.phone == '':
            self.phone = None
        else:
            self.phone = "%" + self.phone + "%"
        if self.uniqueCode == '':
            self.uniqueCode = None
        else:
            self.uniqueCode = "%"+self.uniqueCode+"%"

        try:
            if self.uniqueCode == None and self.phone== None and self.name == None:
                #print("dope")
                self.query = "SELECT * FROM customers where fetched = 0 limit 50;"
                self.mycursor.execute(self.query)
            else:
                self.query = "SELECT * FROM (select * from customers where fetched = 0) as cst WHERE nama LIKE %s or " \
                             "telp like %s or unique_code like %s;"
                self.mycursor.execute(self.query, (self.name, self.phone, self.uniqueCode))
            self.result = self.mycursor.fetchall()
        except Exception as e:
            #print(e)
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

        #print(self.result)
        self.srcResult = QtWidgets.QWidget()
        self.srcResult.ui = srcRes(self.priv, self.parentWin, self.mycursor, self.result, self.user, self.product)
        self.close()