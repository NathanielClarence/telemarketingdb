from PyQt5 import QtWidgets, uic
import fetcher

class Ui(QtWidgets.QDialog):
    def __init__(self, user, mycursor, parentWin):
        super(Ui, self).__init__()
        try:
            uic.loadUi('assets/ui/paramTelleAddData.ui', self)
            self.showFullScreen()
            self.setFixedSize(self.width(), self.height())
            self.scrollArea.setGeometry(int(self.width() / 4), int(self.height() / 4), int(self.width() / 2),
                                        int(self.height() / 2))

            self.dropip = None
            self.dropdb = None
            self.usedb = None

            self.dropip, self.dropdb, self.usedb = fetcher.superData()

            self.user = user
            self.mycursor = mycursor
            self.parentWin = parentWin

            self.dataTelleParams = "DataPerTelle"
            self.dataCircleParams = "DataCircle"
            self.dataResetParams = "DataReset"

            self.initUI()
        except Exception as e:
            print(e)

    def closeWin(self):
        self.parentWin.show()
        self.close()

    def addTelleParam(self):
        self.dataPerTelle = self.in_DataPerTelle.text()
        self.dataCircle = self.in_DataCircle.text()
        self.dataReset = self.in_DataReset.text()

        try:
            if self.dataPerTelle == '' or self.dataCircle == '':
                raise Exception("Jumlah Data per Telle and Perputaran Data cannot be empty.")

            self.query = "UPDATE "+self.usedb+".params SET value = %s WHERE name = %s;"
            self.mycursor.execute(self.query, (self.dataPerTelle, self.dataTelleParams))
            self.mycursor.execute(self.query, (self.dataCircle, self.dataCircleParams))
            self.mycursor.execute(self.query, (self.dataReset, self.dataResetParams))
            self.mycursor.execute("commit;")

            self.buttonReply = QtWidgets.QMessageBox
            # self, title, message, button
            self.warning = self.buttonReply.question(self,"Penambahan Parameter", "Parameter berhasil ditambahkan.",
                                                     QtWidgets.QMessageBox.Ok)
            self.closeWin()
        except Exception as e:
            print("KKKKKKKKKKKKKKKKKKKKKKKKKKKK")
            print(e)
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

    def initUI(self):
        self.btn_Submit.clicked.connect(self.addTelleParam)
        self.btn_Cancel.clicked.connect(self.closeWin)

        try:
            self.query = "SELECT value FROM "+self.usedb+".params WHERE name = %s;"
            self.mycursor.execute(self.query, (self.dataTelleParams,))
            self.TelleParams = self.mycursor.fetchone()
            self.in_DataPerTelle.setText(self.TelleParams[0])

            self.mycursor.execute(self.query, (self.dataCircleParams,))
            self.TelleCircleParams = self.mycursor.fetchone()
            self.in_DataCircle.setText(self.TelleCircleParams[0])

            self.mycursor.execute(self.query, (self.dataResetParams,))
            self.TelleResetParams = self.mycursor.fetchone()
            self.in_DataReset.setText(self.TelleResetParams[0])

        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)
