from PyQt5 import QtWidgets, uic
from dataInput import Ui as admPage
from exportData import Ui as exportDat
#import sys

class Ui(QtWidgets.QWidget):
    def __init__(self, priv, parentWin, mycursor, user):
        super(Ui, self).__init__()
        uic.loadUi('assets/ui/adminUi.ui', self)
        self.setFixedSize(self.width(), self.height())
        self.show()

        self.priv = priv
        self.parentWin = parentWin
        self.mycursor = mycursor
        self.user = user

        self.initUI()

    def initUI(self):
        self.btn_exit.clicked.connect(self.exit)
        self.btn_add.clicked.connect(self.addData)
        self.btn_exportDB.clicked.connect(self.exportDb)
        self.btn_exportUser.clicked.connect(self.exportTelle)

    def exportTelle(self):
        self.exportWin = QtWidgets.QWidget()
        self.exportWin.ui = exportDat(self.priv, self, self.mycursor, self.user, "telle")

    def exportDb(self):
        self.exportWin = QtWidgets.QWidget()
        self.exportWin.ui = exportDat(self.priv, self, self.mycursor, self.user, "db")

    def addData(self):
        self.addWindow = QtWidgets.QWidget()
        self.addWindow.ui = admPage(self.priv, self, self.mycursor, self.user)
        self.hide()

    def exit(self):
        self.parentWin.show()
        self.close()

'''if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    premain = QtWidgets.QWidget()
    premain.ui = Ui()
    sys.exit(app.exec_())'''