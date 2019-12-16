from PyQt5 import QtWidgets, uic
import os
import xlsxwriter
from datetime import datetime

class Ui(QtWidgets.QWidget):
    def __init__(self, priv, parentWin, mycursor, user, exportType):
        super(Ui, self).__init__()
        uic.loadUi('assets/ui/export.ui', self)
        self.setFixedSize(self.width(), self.height())
        self.show()

        self.priv = priv
        self.parentWin = parentWin
        self.mycursor = mycursor
        self.user = user
        self.exportType = exportType

        self.initUI()

    def initUI(self):
        self.in_to.setMaximumDateTime(datetime.now())
        self.in_from.setMaximumDateTime(datetime.now())
        self.in_to.setDate(datetime.now())
        self.in_from.setDate(datetime.now())

        try:
            self.query = "select kode_produk from products;"
            self.mycursor.execute(self.query)
            self.res = self.mycursor.fetchall()
            for x in self.res:
                self.cmb_prod.addItem(x[0])
        except Exception as e:
            print(e)

        self.btn_export.clicked.connect(self.exportToXlsx)
        self.btn_back.clicked.connect(self.back)

    def exportToXlsx(self):
        if not os.path.exists(os.getcwd() + "\\File Export"):
            os.makedirs(os.getcwd() + "\\File Export")

        self.exportFile = self.cmb_prod.currentText()
        if self.exportType == 'telle':
            if self.exportFile.lower() != 'pl':
                try:
                    self.dateRange = (self.in_from.dateTime().toString('yyyy-MM-dd'),self.in_to.dateTime().toString('yyyy-MM-dd'))
                    self.query = "select updated, name, called, cnn, rec, exp,cnt, privilege from (select count(connected) as " \
                                 "called, sum(connected) as cnn, sum(received)" \
                                 " as rec, sum(explained) as exp, pra.updater, pra.updated, cnt from prod_"+str(self.exportFile)+" as pra left join " \
                                 "(select updater, updated, count(note) as cnt from prod_"+str(self.exportFile)+" where note = 'Tertarik' group by updated, " \
                                 "updater) as prd on pra.updater = prd.updater and pra.updated = prd.updated where pra.updated between %s" \
                                 " and %s group by updater, updated) as pcd left join admins on pcd.updater = admins.username order by updated;"
                    self.mycursor.execute(self.query, self.dateRange)
                    self.result = self.mycursor.fetchall()
                    #print(self.result)
                    self.filename = "Export Files/Tele_"+self.exportFile+"_"+self.in_from.dateTime().toString('yyyyMMdd')\
                                    +"-"+self.in_to.dateTime().toString('yyyyMMdd')+".xlsx"
                    self.workbook = xlsxwriter.Workbook(self.filename)
                    self.worksheet = self.workbook.add_worksheet()

                    self.columns = ['No', 'Tanggal', 'Nama Tele', 'Jumlah yang ditelepon/hari', 'Jumlah tersambung', 'Jumlah diangkat', 'Jumlah '
                                    'info tersampaikan', 'Minat']
                    for x in range(len(self.columns)):
                        self.worksheet.write(0, x, self.columns[x])

                    for x in range(len(self.result)):
                        self.worksheet.write(x+1, 0, str(x+1))
                        for y in range(len(self.result[x])):
                            self.worksheet.write(x+1, y+1, str(self.result[x][y]))
                            if self.result[x][7] == "adm":
                                self.worksheet.write(x + 1, 8, "Admin")
                            elif self.result[x][7] == "telle":
                                self.worksheet.write(x + 1, 8, "Tele")
                            if self.result[x][y] == None:
                                self.worksheet.write(x+1, y+1, '')

                    self.workbook.close()
                    self.buttonReply = QtWidgets.QMessageBox
                    self.warning = self.buttonReply.question(self, 'File Export', "File berhasil diexport ke "+os.getcwd()+"\\"+self.filename,
                                                             QtWidgets.QMessageBox.Ok)

                    self.back()
                except Exception as e:
                    self.buttonReply = QtWidgets.QMessageBox
                    self.warning = self.buttonReply.question(self, 'WARNING',
                                                             str(e),
                                                             QtWidgets.QMessageBox.Ok)
            elif self.exportFile.lower() == "pl":
                try:
                    self.dateRange = (self.in_from.dateTime().toString('yyyy-MM-dd'),self.in_to.dateTime().toString('yyyy-MM-dd'))
                    self.query = "select updated, name, called, cnn, rec, exp,cnt, privilege from (select count(connected) as " \
                                 "called, sum(connected) as cnn, sum(received)" \
                                 " as rec, sum(explained) as exp, pra.updater, pra.updated, cnt from prod_pl as pra left join " \
                                 "(select updater, updated, count(note) as cnt from prod_pl where note = 'Tertarik' group by updated, " \
                                 "updater) as prd on pra.updater = prd.updater and pra.updated = prd.updated where pra.updated between %s" \
                                 " and %s group by updater, updated) as pcd left join admins on pcd.updater = admins.username order by updated;"
                    self.mycursor.execute(self.query, self.dateRange)
                    self.result = self.mycursor.fetchall()
                    #print(self.result)
                    self.filename = "Export Files/Tele_"+self.exportFile+"_"+self.in_from.dateTime().toString('yyyyMMdd')\
                                    +"-"+self.in_to.dateTime().toString('yyyyMMdd')+".xlsx"
                    self.workbook = xlsxwriter.Workbook(self.filename)
                    self.worksheet = self.workbook.add_worksheet()

                    self.columns = ['No', 'Tanggal', 'Nama Tele', 'Jumlah yang ditelepon/hari', 'Jumlah tersambung', 'Jumlah diangkat', 'Jumlah '
                                    'info tersampaikan', 'Minat']
                    for x in range(len(self.columns)):
                        self.worksheet.write(0, x, self.columns[x])

                    for x in range(len(self.result)):
                        self.worksheet.write(x+1, 0, str(x+1))
                        for y in range(len(self.result[x])):
                            self.worksheet.write(x+1, y+1, str(self.result[x][y]))
                            if self.result[x][7] == "adm":
                                self.worksheet.write(x + 1, 8, "Admin")
                            elif self.result[x][7] == "telle":
                                self.worksheet.write(x + 1, 8, "Tele")
                            if self.result[x][y] == None:
                                self.worksheet.write(x+1, y+1, '')

                    self.workbook.close()
                    self.buttonReply = QtWidgets.QMessageBox
                    self.warning = self.buttonReply.question(self, 'File Export', "File berhasil diexport ke "+os.getcwd()+"\\"+self.filename,
                                                             QtWidgets.QMessageBox.Ok)

                    self.back()
                except Exception as e:
                    self.buttonReply = QtWidgets.QMessageBox
                    self.warning = self.buttonReply.question(self, 'WARNING',
                                                             str(e),
                                                             QtWidgets.QMessageBox.Ok)
        else:
            try:
                self.dateRange = (
                self.in_from.dateTime().toString('yyyy-MM-dd'), self.in_to.dateTime().toString('yyyy-MM-dd'))
                if self.exportFile.lower() != "pl":
                    self.query = "select name, unique_code, nama, telp, no_ktp, asal_data, alamat, cc, penghasilan, updated, no" \
                                 "te, approval, approval_date from (select updater, unique_code, nama, telp, no_ktp, asal_data, " \
                                 "alamat, cc, penghasilan, updated, note, approval, approval_date from (select id, nama, telp, " \
                                 "no_ktp, asal_data, alamat, cc, penghasilan from customers) as cst left join prod_"+str(self.exportFile)+" on cst.id " \
                                 "= cust_id where updated is not null and updated between %s and %s) as exp " \
                                 "left join admins on username = updater order by updated;"
                else:
                    self.query = "select name, unique_code, nama, telp, no_ktp, asal_data, alamat, cc, penghasilan, updated, no" \
                                 "te, akad, akad_date from (select updater, unique_code, nama, telp, no_ktp, asal_data, " \
                                 "alamat, cc, penghasilan, updated, note, akad, akad_date from (select id, nama, telp, " \
                                 "no_ktp, asal_data, alamat, cc, penghasilan from customers) as cst left join prod_" + str(
                                 self.exportFile) + " on cst.id = cust_id where updated is not null and updated between %s" \
                                 " and %s) as exp left join admins on username = updater order by updated;"
                self.mycursor.execute(self.query, self.dateRange)
                self.result = self.mycursor.fetchall()

                self.filename = "Export Files/DB_" + self.exportFile + "_" + self.in_from.dateTime().toString(
                    'yyyyMMdd') \
                                + "-" + self.in_to.dateTime().toString('yyyyMMdd') + ".xlsx"
                self.workbook = xlsxwriter.Workbook(self.filename)
                self.worksheet = self.workbook.add_worksheet()

                self.columns = ['No', 'Nama Tele', 'Kode Unik', 'Nama', 'No HP', 'No KTP', 'Asal Data', 'Alamat', 'Punya CC/Tidak',
                                'Penghasilan', 'Tanggal Telepon', 'Minat', 'Approve', 'Tanggal Approve']
                for x in range(len(self.columns)):
                    self.worksheet.write(0, x, self.columns[x])

                for x in range(len(self.result)):
                    self.worksheet.write(x + 1, 0, str(x + 1))
                    for y in range(len(self.result[x])):
                        self.worksheet.write(x + 1, y + 1, str(self.result[x][y]))
                        if self.result[x][11] == 1:
                            self.worksheet.write(x + 1, 12, "Sudah")
                        else:# self.result[x][11] == 0:
                            self.worksheet.write(x + 1, 12, "Belum")
                        '''if str(self.result[x][y]) == "None":
                            self.worksheet.write(x + 1, y + 1, '')'''

                self.workbook.close()
                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'File Export',
                                                         "File berhasil diexport ke " + os.getcwd() + "\\" + self.filename,
                                                         QtWidgets.QMessageBox.Ok)

                self.back()
            except Exception as e:
                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'WARNING',
                                                         str(e),
                                                         QtWidgets.QMessageBox.Ok)

    def back(self):
        self.close()
        #self.parentWin.show()

'''if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    premain = QtWidgets.QWidget()
    premain.ui = Ui()
    sys.exit(app.exec_())'''