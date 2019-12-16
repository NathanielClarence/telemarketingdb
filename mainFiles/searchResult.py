from PyQt5 import QtWidgets
from telleUI import Ui as telle
from followUp_CC import Ui as followup
from followUp_PL import Ui as followupPL

class Ui(QtWidgets.QWidget):
    def __init__(self, priv, parentWin, mycursor, result, user, product, recontact=None):
        #super(Ui, self).__init__()
        #uic.loadUi('assets/ui/searchResult.ui', self)
        super(Ui, self).__init__()

        self.priv = priv
        self.parentWin = parentWin
        self.mycursor = mycursor
        self.user = user
        self.sResult = result
        self.product = product
        self.recontact = recontact

        window_width = 800
        window_height = 600
        self.setFixedSize(window_width, window_height)
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
        self.show()

    def createLayout_Container(self):
        self.scrollarea = QtWidgets.QScrollArea(self)
        self.scrollarea.setFixedWidth(780)
        self.scrollarea.setWidgetResizable(True)

        self.widget = QtWidgets.QWidget()
        self.scrollarea.setWidget(self.widget)
        self.layout_SArea = QtWidgets.QVBoxLayout(self.widget)

        if len(self.sResult) == 0:
            self.zeroRes = QtWidgets.QLabel()
            self.zeroRes.setText("No result")
            self.layout_SArea.addWidget(self.zeroRes)

        '''self.sResult = [(1, None, '0888008080', None, 'koran', 0, None, None, '1911/000000001'),
                        (2, 'n1', '0808080', 'jalan-jalan', 'bank m', 0, None, None, '1911/000000002'),
                        (3, 'n2', '0888080080', 'jalan pagi', 'bank m', 0, None, None, '1911/000000003'),
                        (4, None, '088800808000088', None, 'koran', 0, None, None, '1911/000000004')]
                        id, nama, phone, alamat, asal_data, fetched, ??,??, unique_code'''

        for i in range(len(self.sResult)):
            self.layout_SArea.addWidget((self.createLayout_group(i)))
        self.layout_SArea.addStretch(1)

    def createLayout_group(self, num):  # question, num):
        self.sgroupbox = QtWidgets.QGroupBox("Unique Code: "+str(self.sResult[num][8]), self)

        #print(self.sResult[num])
        self.layout_groupbox = QtWidgets.QHBoxLayout(self.sgroupbox)

        self.fLayout = QtWidgets.QFormLayout()

        '''self.tb = QtWidgets.QLineEdit()
        self.tb.setText(self.sResult[num][8])
        self.tb.setEnabled(False)
        self.fLayout.addRow(QtWidgets.QLabel("Unique Code:"), self.tb)'''

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


        if self.recontact!= None:
            self.tb = QtWidgets.QLineEdit()
            self.tb.setText(str(self.sResult[num][11]))
            self.tb.setEnabled(False)
            self.fLayout.addRow(QtWidgets.QLabel("Kontak Ulang:"), self.tb)
            self.layout_groupbox.addLayout(self.fLayout)

            self.editButton = QtWidgets.QPushButton()
            self.editButton.setText("Kontak Ulang")
            self.editButton.clicked.connect(lambda: self.editCust(self.sResult[num][0], num))
            self.layout_groupbox.addWidget(self.editButton)

        else:
            self.editButton = QtWidgets.QPushButton()
            self.editButton.setText("Edit")
            if self.priv!= "adm":
                self.editButton.setEnabled(False)
            self.editButton.clicked.connect(lambda: self.editCust(self.sResult[num][0]))
            self.layout_groupbox.addWidget(self.editButton)

            try:
                #print(self.sResult[num][0])
                self.qCheckFollUp = "SELECT note from prod_"+self.product+" where cust_id = %s"
                self.mycursor.execute(self.qCheckFollUp, (self.sResult[num][0],))
                self.sFollUp = self.mycursor.fetchone()
            except Exception as e:
                print(e)
                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                         QtWidgets.QMessageBox.Ok)

            self.followUp = QtWidgets.QPushButton()
            self.followUp.setText("Follow Up")
            self.followUp.clicked.connect(lambda: self.follup(self.sResult[num][0]))
            self.layout_groupbox.addWidget(self.followUp)
            self.followUp.setEnabled(False)
            try:
                #print(str(self.sFollUp[0]))
                if self.sFollUp[0] == "Tertarik":
                    self.followUp.setEnabled(True)
            except Exception as e:
                print('')
                '''self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                         QtWidgets.QMessageBox.Ok)'''

        return self.sgroupbox

        '''self.show()

        self.priv = priv
        self.mycursor = mycursor
        self.parentWin = parentWin
        #self.sResult = result
        self.sResult = [(1, None, '0888008080', None, 'koran', 0, None, None, '1911/000000001'),
                        (2, 'n1', '0808080', 'jalan-jalan', 'bank m', 0, None, None, '1911/000000002'),
                        (3, 'n2', '0888080080', 'jalan pagi', 'bank m', 0, None, None, '1911/000000003'),
                        (4, None, '088800808000088', None, 'koran', 0, None, None, '1911/000000004')]

        self.btn_return.clicked.connect(self.closeWin)

        if len(self.sResult)!=0:
            self.noRes.setVisible(False)

            try:
                self.cnt = 0
                for res in range(len(self.sResult)):
                    print(self.sResult[res])
                    self.fLayout = QtWidgets.QFormLayout()

                    self.tb = QtWidgets.QLineEdit()
                    self.tb.setText(self.sResult[res][8])
                    self.tb.setEnabled(False)
                    self.fLayout.addRow(QtWidgets.QLabel("Unique Code:"), self.tb)

                    self.tb = QtWidgets.QLineEdit()
                    self.tb.setText(self.sResult[res][1])
                    self.tb.setEnabled(False)
                    self.fLayout.addRow(QtWidgets.QLabel("Nama:"), self.tb)

                    self.tb = QtWidgets.QLineEdit()
                    self.tb.setText(self.sResult[res][2])
                    self.tb.setEnabled(False)
                    self.fLayout.addRow(QtWidgets.QLabel("No HP:"),self.tb)

                    self.tb = QtWidgets.QLineEdit()
                    self.tb.setText(self.sResult[res][4])
                    self.tb.setEnabled(False)
                    self.fLayout.addRow(QtWidgets.QLabel("Asal Data:"), self.tb)
                    # print("pop")
                    self.gridLayout.addLayout(self.fLayout,self.cnt*2, 0, 2, 3)

                    self.editButton = QtWidgets.QPushButton()
                    self.editButton.setText("Edit")
                    self.editButton.clicked.connect(lambda: self.editCust(self.sResult[res][0]))
                    self.gridLayout.addWidget(self.editButton, self.cnt*2, 3)
                    #print("opo1")

                    self.followUp = QtWidgets.QPushButton()
                    self.followUp.setText("Follow Up")
                    self.followUp.clicked.connect(lambda: self.follup(self.sResult[res][0]))
                    self.gridLayout.addWidget(self.followUp, self.cnt*2+1, 3)

                    self.cnt+=1
            except Exception as e:
                print(str(e))'''

    def editCust(self, id, num = None):
        #print(id)
        try:
            if self.recontact!= None:
                self.query = "UPDATE prod_"+self.product+" set recontact_status = True where data_id = %s;"
                self.mycursor.execute(self.query, (self.sResult[num][10],))
                self.mycursor.execute("commit;")

                self.telle = QtWidgets.QWidget()
                self.telle.ui = telle(self.priv, self, self.mycursor, self.user,self.product, target = id, recontact= True)
            else:
                self.telle = QtWidgets.QWidget()
                self.telle.ui = telle(self.priv, self, self.mycursor, self.user, self.product, target=id)
            self.hide()
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

    def follup(self, id):
        #print("Follup "+str(id))
        self.folUp = QtWidgets.QWidget()
        if self.product.lower() == "pl":
            self.folUp.ui = followupPL(self.priv, self, self.mycursor, self.user, self.product, target=id)
        else:
            self.folUp.ui = followup(self.priv, self, self.mycursor, self.user, self.product, target=id)
        self.hide()

    def closeWin(self):
        self.parentWin.show()
        self.close()

'''if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    premain = QtWidgets.QMainWindow()
    premain.ui = Ui()
    sys.exit(app.exec_())'''