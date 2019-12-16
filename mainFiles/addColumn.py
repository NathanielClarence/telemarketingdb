from PyQt5 import QtWidgets, uic
import re

class Ui(QtWidgets.QWidget):
    def __init__(self, mycursor):
        super(Ui, self).__init__()
        uic.loadUi('assets/ui/addColumn.ui', self)
        self.setFixedSize(self.width(), self.height())
        self.show()

        self.mycursor = mycursor

        self.initUI()

        self.btn_delete.clicked.connect(self.deleteCol)
        self.btn_cancel.clicked.connect(self.closeWin)
        self.btn_add.clicked.connect(self.addColumn)

    def closeWin(self):
        self.close()

    def initUI(self):
        try:
            self.query = "SELECT col FROM add_data;"
            self.mycursor.execute(self.query)
            self.res = self.mycursor.fetchall()

            for x in self.res:
                self.cmb_col.addItem(x[0])
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

    def deleteCol(self):
        self.selectedCol = str(self.cmb_col.currentText())

        self.qm = QtWidgets.QMessageBox
        self.confirm = self.qm.question(self, 'PERINGATAN',"Apakah anda yakin ingin menghapus kolom ini?",
                                                     self.qm.Yes|self.qm.No)
        if self.confirm == self.qm.Yes:
            try:
                self.query = "DELETE FROM add_data where col = %s;"
                self.mycursor.execute(self.query,(self.selectedCol,))
                self.query = "ALTER TABLE customers drop column "+self.selectedCol+";"
                self.mycursor.execute(self.query)
                self.mycursor.execute("commit;")
                self.close()
                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'Hapus kolom', "Kolom "+self.selectedCol+" berhasil dihapus",
                                                         QtWidgets.QMessageBox.Ok)
            except Exception as e:
                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                         QtWidgets.QMessageBox.Ok)

    def addColumn(self):
        if self.in_newCol.text()=='':
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', "Tolong isi nama kolom", QtWidgets.QMessageBox.Ok)
        else:
            self.newCol = str(self.in_newCol.text())
            self.newCol = re.sub('[^A-Za-z0-9]+', '_', self.newCol)
            try:
                self.query = "INSERT INTO ADD_DATA (COL) VALUES (%s);"
                self.mycursor.execute(self.query, (self.newCol,))
                self.query = "ALTER TABLE CUSTOMERS ADD "+self.newCol+" varchar(100);"
                self.mycursor.execute(self.query)
                self.mycursor.execute("commit;")
                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'Tambah Kolom', "Kolom berhasil ditambahkan",
                                                         QtWidgets.QMessageBox.Ok)
                self.close()
            except Exception as e:
                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                         QtWidgets.QMessageBox.Ok)

