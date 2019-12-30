from PyQt5 import QtWidgets, uic
from addSuperAdmin import Ui as addSA
from addUsers import Ui as addAdmins
from addProduct import Ui as addPrdc
from addBank import Ui as addBnk
from addColumn import Ui as addCol

class Ui(QtWidgets.QWidget):
    def __init__(self, user, mycursor, parentWin):
        super(Ui, self).__init__()
        uic.loadUi('assets/ui/superadminUi.ui', self)
        self.setFixedSize(self.width(), self.height())
        self.show()

        self.user = user
        self.mycursor = mycursor
        self.parentWin = parentWin

        self.btn_addSuperadmin.clicked.connect(self.btnAddSA)
        self.btn_back.clicked.connect(self.logout)
        self.btn_add.clicked.connect(self.addUser)
        self.btn_addProduct.clicked.connect(self.addPrd)
        self.btn_addBank.clicked.connect(self.tambahBank)
        self.btn_addCol.clicked.connect(self.alterDB)

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