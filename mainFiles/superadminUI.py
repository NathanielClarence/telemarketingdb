from PyQt5 import QtWidgets, uic
from addSuperAdmin import Ui as addSA
from addUsers import Ui as addAdmins
from addProduct import Ui as addPrdc
from addBank import Ui as addBnk
from addColumn import Ui as addCol
import fetcher

class Ui(QtWidgets.QWidget):
    def __init__(self, user, mycursor, parentWin):
        super(Ui, self).__init__()
        uic.loadUi('assets/ui/superadminUi.ui', self)
        self.setFixedSize(self.width(), self.height())
        self.show()

        self.user = user
        self.mycursor = mycursor
        self.parentWin = parentWin
        self.dropip, self.dbcore, self.targetDB = fetcher.superData()

        self.initUI()

    def initUI(self):
        self.totalData()
        self.thisMonth()
        self.contactedToday()

        self.btn_addSuperadmin.clicked.connect(self.btnAddSA)
        self.btn_back.clicked.connect(self.logout)
        self.btn_add.clicked.connect(self.addUser)
        self.btn_addProduct.clicked.connect(self.addPrd)
        self.btn_addBank.clicked.connect(self.tambahBank)
        self.btn_addCol.clicked.connect(self.alterDB)
        self.btn_refresh.clicked.connect(self.refreshData)

    def refreshData(self):
        self.totalData()
        self.thisMonth()
        self.contactedToday()

    def totalData(self):
        self.query = "SELECT count(id) from "+self.targetDB+".customers;"
        self.mycursor.execute(self.query)
        self.result = self.mycursor.fetchone()
        self.ttlData = str(self.result[0])
        #print(self.ttlData)
        self.lbl_data.setText(self.ttlData)

    def thisMonth(self):
        self.query = "SELECT count(id) from "+self.targetDB+".customers where date_added > date_sub(now(), interval 1 month);"
        self.mycursor.execute(self.query)
        self.result = self.mycursor.fetchone()
        self.thisMon = str(self.result[0])
        #print(self.thisMon)
        self.lbl_thisMonth.setText(self.thisMon)

    def contactedToday(self):
        self.today = 0
        self.query = "select kode_produk from "+self.targetDB+".products;"
        self.mycursor.execute(self.query)
        self.prodResult = self.mycursor.fetchall()
        for x in self.prodResult:
            self.query = "SELECT count(data_id) from "+self.targetDB+".prod_"+x[0]+" where updated = curdate();"
            self.mycursor.execute(self.query)
            self.result = self.mycursor.fetchone()
            self.today += self.result[0]
        self.lbl_contacted.setText(str(self.today))

    def alterDB(self):
        self.altDB = QtWidgets.QWidget
        self.altDB.ui = addCol(self.mycursor, self)

    def tambahBank(self):
        self.addBank = QtWidgets.QWidget()
        self.addBank.ui = addBnk(self.mycursor)

    def addPrd(self):
        self.addprod = QtWidgets.QWidget()
        self.addprod.ui = addPrdc(self.user, self.mycursor, self)
        self.hide()

    def addUser(self):
        self.addSA = QtWidgets.QWidget()
        self.addSA.ui = addAdmins(self.user, self.mycursor, self)
        self.hide()

    def btnAddSA(self):
        #print("tambah superadmin")
        self.addSA = QtWidgets.QWidget()
        self.addSA.ui = addSA(self.user, self.mycursor, self)
        self.hide()

    def logout(self):
        self.parentWin.show()
        self.close()