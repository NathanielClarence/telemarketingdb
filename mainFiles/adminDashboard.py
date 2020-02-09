from PyQt5 import QtWidgets, uic, QtGui
import fetcher
#import sys
#import mysql.connector as conn

class Ui(QtWidgets.QMainWindow):
    def __init__(self, user, mycursor, parentWin):
        super(Ui, self).__init__()
        uic.loadUi('assets/ui/dashboard.ui', self)
        self.user= user
        self.mycursor = mycursor
        self.parentWin = parentWin

        self.ip, self.core, self.target = fetcher.superData()

        self.showFullScreen()
        self.setFixedSize(self.width(), self.height())
        self.scrollArea.setGeometry(self.scrollArea.geometry().x(),self.scrollArea.geometry().x(), self.width()-20, self.height()-20)
        self.initUI()

    def initUI(self):
        try:
            self.btn_back.clicked.connect(self.closeWin)
            self.mycursor.execute("use "+str(self.target))

            '''self.mydb = conn.connect(
                host="127.0.0.1",
                user="ruchid",
                passwd="admin",
                database="dbtest",
                auth_plugin='mysql_native_password',
                buffered = True
            )

            self.mycursor = self.mydb.cursor()'''

            self.query = "SELECT kode_produk, nama_produk from products;"
            self.mycursor.execute(self.query)
            self.products = self.mycursor.fetchall()

            self.summaryRow = 0

            #self.myfont = QtGui.QFont("Segoe UI", 10).setBold(True)

            for x in range(len(self.products)):
                self.query = "select count(note) from prod_"+self.products[x][0]+" where note ='Tertarik' and updated = curdate();"
                self.mycursor.execute(self.query)
                self.tertarik = self.mycursor.fetchone()[0]

                self.query = "select count(note) from prod_" + self.products[x][
                    0] + " where note ='Tidak' and updated = curdate();"
                self.mycursor.execute(self.query)
                self.tidakTertarik = self.mycursor.fetchone()[0]

                self.query = "select count(note) from prod_" + self.products[x][
                    0] + " where note ='Pikir-pikir' and updated = curdate();"
                self.mycursor.execute(self.query)
                self.pikirpikir = self.mycursor.fetchone()[0]

                self.query = "select count(prospect) from prod_" + self.products[x][
                    0] + " where prospect ='1' and updated = curdate();"
                self.mycursor.execute(self.query)
                self.hp = self.mycursor.fetchone()[0]

                self.query = "select count(prospect) from prod_" + self.products[x][
                    0] + " where prospect ='2' and updated = curdate();"
                self.mycursor.execute(self.query)
                self.wp = self.mycursor.fetchone()[0]

                self.query = "select count(prospect) from prod_" + self.products[x][
                    0] + " where prospect ='3' and updated = curdate();"
                self.mycursor.execute(self.query)
                self.cp = self.mycursor.fetchone()[0]

                self.query = "select count(connected), sum(connected), sum(received), sum(explained)" \
                                          " from prod_" + self.products[x][0] + " where updated = curdate();"
                self.mycursor.execute(self.query)
                self.alldata = self.mycursor.fetchone()

                self.productLabel = QtWidgets.QLabel(self.products[x][1])
                self.productLabel.setFont(QtGui.QFont("Segoe UI", 12, weight = QtGui.QFont.Bold))
                self.innerGrid.addWidget(self.productLabel, self.summaryRow, 0)
                self.labels = ['Ditelepon','Tersambung', 'Diterima', 'Dijelaskan']
                for x in range(len(self.alldata)):
                    self.innerGrid.addWidget(QtWidgets.QLabel(self.labels[x]), self.summaryRow+x+1, 0)
                    self.innerGrid.addWidget(QtWidgets.QLabel(str(self.alldata[x])),self.summaryRow+x+1, 1)
                self.summaryRow+=5

                self.innerGrid.addWidget(QtWidgets.QLabel("Tertarik"), self.summaryRow, 0)
                self.innerGrid.addWidget(QtWidgets.QLabel(str(self.tertarik)), self.summaryRow, 1)
                self.summaryRow+=1

                self.innerGrid.addWidget(QtWidgets.QLabel("Tidak Tertarik"), self.summaryRow, 0)
                self.innerGrid.addWidget(QtWidgets.QLabel(str(self.tidakTertarik)), self.summaryRow, 1)
                self.summaryRow += 1

                self.innerGrid.addWidget(QtWidgets.QLabel("Pikir-pikir"), self.summaryRow, 0)
                self.innerGrid.addWidget(QtWidgets.QLabel(str(self.pikirpikir)), self.summaryRow, 1)
                self.summaryRow += 1

                self.innerGrid.addWidget(QtWidgets.QLabel("Hot Prospect"), self.summaryRow, 0)
                self.innerGrid.addWidget(QtWidgets.QLabel(str(self.hp)), self.summaryRow, 1)
                self.summaryRow += 1

                self.innerGrid.addWidget(QtWidgets.QLabel("Warm Prospect"), self.summaryRow, 0)
                self.innerGrid.addWidget(QtWidgets.QLabel(str(self.wp)), self.summaryRow, 1)
                self.summaryRow += 1

                self.innerGrid.addWidget(QtWidgets.QLabel("Cold Prospect"), self.summaryRow, 0)
                self.innerGrid.addWidget(QtWidgets.QLabel(str(self.cp)), self.summaryRow, 1)
                self.summaryRow += 1

                self.innerGrid.addWidget(QtWidgets.QLabel(" "), self.summaryRow, 0)
                self.summaryRow +=1

            self.eachrows = []

            for x in self.products:  # jangan lupa diganti curdate()
                self.query = "select name as Nama, called as Ditelepon, cnn as Tersambung, rec as Diangkat, " \
                             "exp as Diinfokan, cnt as Tertarik,appointment as Appointment, username, product from (select count" \
                             "(connected) as called, sum(connected) as cnn, sum(received) as rec, sum(explained) as exp," \
                             " pra.updater, pra.updated, cnt, appointment from prod_" + x[
                                 0] + " as pra left join (select pdd.updater" \
                                      ", pdd.updated, count(note) as appointment, cnt from prod_" + x[
                                 0] + " as pdd left join (select updater, " \
                                      "updated, count(note) as cnt from prod_" + x[
                                 0] + " where note = 'Tertarik' group by updated, updater) as" \
                                      " tt on tt.updater = pdd.updater and pdd.updated= tt.updated where note = 'Pikir-pikir' group" \
                                      " by pdd.updater, pdd.updated) as prd on pra.updater = prd.updater and pra.updated = prd.updat" \
                                      "ed where pra.updated = curdate() group by updater, updated) as pcd left join admins on pcd.upd" \
                                      "ater = admins.username order by updated;"
                self.mycursor.execute(self.query)
                self.result = self.mycursor.fetchall()

                self.eachrows += self.result

            self.tableWidget.setRowCount(len(self.eachrows))
            self.tableWidget.setColumnCount(len(self.eachrows[0]))

            self.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Nama"))
            self.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Ditelepon"))
            self.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Tersambung"))
            self.tableWidget.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("Diangkat"))
            self.tableWidget.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem("Diinfokan"))
            self.tableWidget.setHorizontalHeaderItem(5, QtWidgets.QTableWidgetItem("Tertarik"))
            self.tableWidget.setHorizontalHeaderItem(6, QtWidgets.QTableWidgetItem("Appointment"))
            self.tableWidget.setHorizontalHeaderItem(7, QtWidgets.QTableWidgetItem("Username"))
            self.tableWidget.setHorizontalHeaderItem(8, QtWidgets.QTableWidgetItem("Kode Produk"))

            for x in range(len(self.eachrows)):
                for y in range(len(self.eachrows[x])):
                    self.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(self.eachrows[x][y])))
        except Exception as e:
            print(e)

    def closeWin(self):
        self.mycursor.execute("use "+self.core)
        self.parentWin.show()
        self.close()

'''if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    premain = QtWidgets.QMainWindow()
    premain.ui = Ui()
    sys.exit(app.exec_())'''