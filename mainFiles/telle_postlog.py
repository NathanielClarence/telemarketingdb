from PyQt5 import uic, QtWidgets
from telleUI import Ui as telle
from searchUser import Ui as search
from searchResult import Ui as srcRes

class Ui(QtWidgets.QWidget):
    def __init__(self, priv, parentWin, mycursor, user):
        super(Ui, self).__init__()
        uic.loadUi('assets/ui/telle_postlog.ui', self)
        self.showFullScreen()
        self.setFixedSize(self.width(), self.height())
        self.scrollArea.setGeometry(int(self.width() / 4), int(self.height() / 4), int(self.width() / 2),
                                    int(self.height() / 2))

        self.priv = priv
        self.parentWin = parentWin
        self.mycursor = mycursor
        self.user = user

        if self.priv == "adm":
            self.cmb_product.setEnabled(True)
            try:
                self.mycursor.execute("SELECT KODE_PRODUK FROM PRODUCTS;")
                self.res = self.mycursor.fetchall()
                for prd in self.res:
                    self.cmb_product.addItem(prd[0])
            except Exception as e:
                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'WARNING', str(e), QtWidgets.QMessageBox.Ok)
        else:
            self.mycursor.execute("SELECT product FROM admins where username like %s;",(self.user,))
            self.res = self.mycursor.fetchone()
            self.cmb_product.addItem(self.res[0])

        self.btn_all.clicked.connect(self.allcust)
        self.btn_close.clicked.connect(self.closeWin)
        self.btn_search.clicked.connect(self.srcCustomer)
        self.btn_follup.clicked.connect(self.followUp)
        self.btn_recontact.clicked.connect(self.kontakUlang)

        self.btn_recontact.setEnabled(False)
        self.btn_recontact.setVisible(False)

    def kontakUlang(self):
        try:
            self.table = "prod_" + str(self.cmb_product.currentText())
            self.query = "select id, nama, telp, alamat, asal_data, fetched, no_ktp, penghasilan, cst.unique_code, cc, data_id" \
                        ", recontact from (select * from customers where fetched = 0) as cst left join prod_cc on id = cust_id where " \
                         "note = 'Pikir-pikir' and recontact_status = 0;"
            self.mycursor.execute(self.query)
            self.result = self.mycursor.fetchall()
            self.follow = QtWidgets.QWidget()
            self.follow.ui = srcRes(self.priv, self, self.mycursor, self.result, self.user,
                                    str(self.cmb_product.currentText()), True)
            self.hide()
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

    def followUp(self):
        self.search = QtWidgets.QWidget()
        self.search.ui = search(self.priv, self, self.mycursor, self.user, True)
        self.hide()
        '''try:
            self.table = "prod_"+str(self.cmb_product.currentText())
            if str(self.cmb_product.currentText()).lower()=="pl":
                self.query = "select id, nama, telp, alamat, asal_data, fetched, no_ktp, penghasilan, " + self.table + ".unique_code, cc" \
                             " from (select * from customers where fetched = 0) as cst left join " + self.table + " on id = cust_id where note = 'Tertarik'" \
                             " and vis_approval like '2';"
            else:
                self.query = "select id, nama, telp, alamat, asal_data, fetched, no_ktp, penghasilan, "+self.table+".unique_code, cc" \
                         " from (select * from customers where fetched = 0) as cst left join "+self.table+" on id = cust_id where note = 'Tertarik'" \
                         " and approval like '2';"
            self.mycursor.execute(self.query)
            self.result = self.mycursor.fetchall()
            self.follow = QtWidgets.QWidget()
            self.follow.ui = srcRes(self.priv, self, self.mycursor, self.result, self.user, str(self.cmb_product.currentText()))
            self.hide()
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)'''

    def srcCustomer(self):
        self.search = QtWidgets.QWidget()
        self.search.ui = search(self.priv, self, self.mycursor, self.user)
        self.hide()

    def allcust(self):
        self.allcustomer = QtWidgets.QWidget()
        self.prod = str(self.cmb_product.currentText())
        print(self.prod)
        try:
            self.allcustomer.ui = telle(self.priv, self, self.mycursor, self.user, self.prod.lower())
        except Exception as e:
            print(str(e))
        self.hide()

    def closeWin(self):
        self.close()
        self.parentWin.show()