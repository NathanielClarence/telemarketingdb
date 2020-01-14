from PyQt5 import QtWidgets
from searchHistory import Ui as srcHistory

class Ui(QtWidgets.QWidget):
    def __init__(self, priv, parentWin, mycursor, result, user, product):
        super(Ui, self).__init__()

        self.priv = priv
        self.parentWin = parentWin
        self.mycursor = mycursor
        self.user = user
        self.sResult = result
        self.product = product
        self.table = "prod_"+product.lower()

        '''window_width = 800
        window_height = 600
        self.setFixedSize(window_width, window_height)'''
        #print("ee")
        #print(self.sResult)
        self.initUI()

    def initUI(self):
        self.createLayout_Container()
        self.layout_All = QtWidgets.QVBoxLayout(self)
        self.layout_All.addWidget(self.scrollarea)
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setObjectName("pushButton")
        self.layout_All.addWidget(self.pushButton)
        self.pushButton.setText("Return")
        self.pushButton.clicked.connect(self.closeWin)
        #self.show()
        self.showFullScreen()
        self.setFixedSize(self.width(), self.height())

    def createLayout_Container(self):
        self.scrollarea = QtWidgets.QScrollArea(self)
        #self.scrollarea.setFixedWidth(780)
        self.scrollarea.setWidgetResizable(True)

        self.widget = QtWidgets.QWidget()
        self.scrollarea.setWidget(self.widget)
        self.layout_SArea = QtWidgets.QVBoxLayout(self.widget)

        if len(self.sResult) == 0:
            self.zeroRes = QtWidgets.QLabel()
            self.zeroRes.setText("No result")
            self.layout_SArea.addWidget(self.zeroRes)
        try:
            for i in range(len(self.sResult)):
                self.layout_SArea.addWidget((self.createLayout_group(i)))
        except Exception as e:
            print(e)
        self.layout_SArea.addStretch(1)

    def createLayout_group(self, num):  # question, num):
        self.sgroupbox = QtWidgets.QGroupBox("Unique Code: "+str(self.sResult[num][8]), self)

        self.layout_groupbox = QtWidgets.QHBoxLayout(self.sgroupbox)

        self.fLayout = QtWidgets.QFormLayout()

        self.tb = QtWidgets.QLineEdit()
        self.tb.setText(self.sResult[num][1])
        self.tb.setEnabled(False)
        self.fLayout.addRow(QtWidgets.QLabel("Nama:"), self.tb)

        self.tb = QtWidgets.QLineEdit()
        self.tb.setText(self.sResult[num][2])
        self.tb.setEnabled(False)
        self.fLayout.addRow(QtWidgets.QLabel("No HP:"), self.tb)

        self.tb = QtWidgets.QLineEdit()
        self.tb.setText(self.sResult[num][4])
        self.tb.setEnabled(False)
        self.fLayout.addRow(QtWidgets.QLabel("Asal Data:"), self.tb)
        self.layout_groupbox.addLayout(self.fLayout)

        #else:
        self.historyButton = QtWidgets.QPushButton()
        self.historyButton.setText("Lihat Histori")
        if self.priv!= "adm":
            self.historyButton.setEnabled(False)
        self.historyButton.clicked.connect(lambda: self.editCust(self.sResult[num][0]))
        self.layout_groupbox.addWidget(self.historyButton)

        return self.sgroupbox

    def editCust(self, id):
        try:
            self.query = "select id, nama, telp, alamat, asal_data, fetched, no_ktp, penghasilan, " + self.table + ".unique_code, cc" \
                         ", updated, followup_date, note, berkas, data_masuk, approval, recontact from customers as cst left " \
                         "join prod_cc on id = cust_id where cust_id = %s order by updated;"
            self.mycursor.execute(self.query, (id,))
            self.result = self.mycursor.fetchall()
            self.follow = QtWidgets.QWidget()
            self.follow.ui = srcHistory(self.priv, self, self.mycursor, self.result, self.user,
                                        self.product)
            self.hide()
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

    def closeWin(self):
        self.parentWin.show()
        self.close()

'''if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    premain = QtWidgets.QMainWindow()
    premain.ui = Ui()
    sys.exit(app.exec_())'''