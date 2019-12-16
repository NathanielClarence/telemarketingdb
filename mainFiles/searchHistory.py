from PyQt5 import QtWidgets
#from telleUI import Ui as telle
#from followUp_CC import Ui as followup

class Ui(QtWidgets.QWidget):
    def __init__(self, priv, parentWin, mycursor, result, user, product):
        #super(Ui, self).__init__()
        #uic.loadUi('assets/ui/searchResult.ui', self)
        super(Ui, self).__init__()

        self.priv = priv
        self.parentWin = parentWin
        self.mycursor = mycursor
        self.user = user
        self.sResult = result
        self.product = product

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

        self.tb = QtWidgets.QLineEdit()
        self.tb.setText(str(self.sResult[num][10]))
        self.tb.setEnabled(False)
        self.fLayout.addRow(QtWidgets.QLabel("Terakhir dikontak:"), self.tb)
        self.layout_groupbox.addLayout(self.fLayout)

        self.tb = QtWidgets.QLineEdit()
        self.tb.setText(str(self.sResult[num][12]))
        self.tb.setEnabled(False)
        self.fLayout.addRow(QtWidgets.QLabel("Tertarik/Tidak:"), self.tb)
        self.layout_groupbox.addLayout(self.fLayout)

        if self.sResult[num][12]=="Tertarik":
            self.tb = QtWidgets.QLineEdit()
            self.tb.setText(str(self.sResult[num][11]))
            self.tb.setEnabled(False)
            self.fLayout.addRow(QtWidgets.QLabel("Follow-up terakhir:"), self.tb)
            self.layout_groupbox.addLayout(self.fLayout)

            self.tb = QtWidgets.QLineEdit()
            if self.sResult[num][13]:
                self.tb.setText("Ya")
            else:
                self.tb.setText("Tidak")
            self.tb.setEnabled(False)
            self.fLayout.addRow(QtWidgets.QLabel("Berkas:"), self.tb)
            self.layout_groupbox.addLayout(self.fLayout)

            self.tb = QtWidgets.QLineEdit()
            if self.sResult[num][14]:
                self.tb.setText("Ya")
            else:
                self.tb.setText("Tidak")
            self.tb.setEnabled(False)
            self.fLayout.addRow(QtWidgets.QLabel("Data Masuk:"), self.tb)
            self.layout_groupbox.addLayout(self.fLayout)

            self.tb = QtWidgets.QLineEdit()
            if self.sResult[num][15]==1:
                self.tb.setText("Ya")
            elif self.sResult[num][15]==0:
                self.tb.setText("Tidak")
            else:
                self.tb.setText("Belum")
            self.tb.setEnabled(False)
            self.fLayout.addRow(QtWidgets.QLabel("Approve:"), self.tb)
            self.layout_groupbox.addLayout(self.fLayout)
        elif self.sResult[num][12]=="Pikir-pikir":
            self.tb = QtWidgets.QLineEdit()
            self.tb.setText(str(self.sResult[num][16]))
            self.tb.setEnabled(False)
            self.fLayout.addRow(QtWidgets.QLabel("Hubungi kembali:"), self.tb)
            self.layout_groupbox.addLayout(self.fLayout)

        return self.sgroupbox

    def closeWin(self):
        self.parentWin.show()
        self.close()

'''if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    premain = QtWidgets.QMainWindow()
    premain.ui = Ui()
    sys.exit(app.exec_())'''