from PyQt5 import uic, QtWidgets
#import mysql.connector as conn
#import sys

class Ui(QtWidgets.QWidget):
    def __init__(self, priv, parentWin, mycursor, user, product, target):
        super(Ui, self).__init__()
        uic.loadUi('assets/ui/followUp_PL.ui', self)
        self.setFixedSize(self.width(), self.height())
        self.show()

        self.priv = priv
        self.parentWin = parentWin
        '''self.mydb = conn.connect(
            host="127.0.0.1",
            user="ruchid",  # sesuaikan user khusus
            passwd="admin",  # sesuaikan user khusus
            database="dbtest",
            auth_plugin='mysql_native_password',
            buffered=True
        )'''
        self.mycursor = mycursor
        self.user = user
        self.prd = product
        self.table = "prod_"+product
        self.targetID = target

        self.initUI()
        #self.getData()

    def cancel(self):
        self.parentWin.show()
        self.close()

    def save(self):
        try:
            self.query = "UPDATE customers set fetched = false where id = %s;"
            self.mycursor.execute(self.query, (self.targetID,))
            self.mycursor.commit()
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

        try:
            self.query = "UPDATE "+self.table+" SET berkas = %s, data_masuk = %s, agent = %s, owner = %s, setuju = %s, " \
                         "ondesk_keluar = %s, cst_approve = %s, visit = %s, vis_approval = %s, akad = %s, updater = %s" \
                         " where data_id = %s;"
            self.mycursor.execute(self.query, (self.berkas, self.ondesk, self.agent, self.owner,self.setuju, self.ondeskRes,
                                               self.cstAppr, self.visit, self.appr, self.akad, self.user, self.targetID))
            self.mycursor.execute("commit;")
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'Save Successful', "Data berhasil disimpan", QtWidgets.QMessageBox.Ok)
            self.cancel()
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e), QtWidgets.QMessageBox.Ok)

        if self.akad:
            try:
                self.query = "UPDATE "+self.table+" set akad_date = curdate() where data_id = %s;"
                self.mycursor.execute(self.query, (self.targetID,))
                self.mycursor.execute("commit;")
            except Exception as e:
                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'WARNING', str(e), QtWidgets.QMessageBox.Ok)

    def getData(self):
        try:
            self.query = "SELECT pl.unique_code, nama, telp, bank, berkas, data_masuk, agent, owner, setuju, ondesk_keluar, " \
                     "cst_approve, visit, vis_approval, akad from (select * from customers where fetched = 0) as cst " \
                     "left join prod_pl as pl on cust_id = id where pl.data_id = %s;"
            self.mycursor.execute(self.query, (self.targetID,))
            self.fetchResult = self.mycursor.fetchone()
            #print(self.fetchResult)
            self.uniqueCode.setText(self.fetchResult[0])
            self.in_name.setText(self.fetchResult[1])
            self.in_phone.setText(self.fetchResult[2])
            self.in_bank.setText(self.fetchResult[3])
            if self.fetchResult[4]:
                self.chk_berkas.setChecked(True)
            if self.fetchResult[5]:
                self.chk_ondesk.setChecked(True)
            if self.fetchResult[6]:
                self.chk_agent.setChecked(True)
            if self.fetchResult[7]:
                self.chk_owner.setChecked(True)

            if self.fetchResult[8]==1:
                self.chk_setuju.setChecked(True)
            elif self.fetchResult[8]==0:
                self.chk_tidakSetuju.setChecked(True)

            if self.fetchResult[9]:
                self.chk_ondeskResult.setChecked(True)

            if self.fetchResult[10] == 1:
                self.chk_cstApp.setChecked(True)
            elif self.fetchResult[10] == 0:
                self.chk_cstNotApp.setChecked(True)

            if self.fetchResult[11]:
                self.chk_Visit.setChecked(True)

            if self.fetchResult[12] == 1:
                self.chk_Approve.setChecked(True)
            elif self.fetchResult[12] == 0:
                self.chk_tidakApprove.setChecked(True)

            if self.fetchResult[13]:
                self.chk_akad.setChecked(True)
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e), QtWidgets.QMessageBox.Ok)

        try:
            self.query = "UPDATE customers set fetched = True where id = %s;"
            self.mycursor.execute(self.query, (self.targetID,))
            self.mycursor.commit()
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

    def checkerAll(self):
        if self.chk_berkas.isChecked():
            self.berkas = True
        else:
            self.berkas = False

        if self.chk_ondesk.isChecked():
            self.ondesk = True
        else:
            self.ondesk = False

        if self.chk_ondeskResult.isChecked():
            self.ondeskRes = True
        else:
            self.ondeskRes = False

        if self.chk_cstApp.isChecked():
            self.cstAppr = True
        elif self.chk_cstNotApp.isChecked():
            self.cstAppr = False
        else:
            self.cstAppr = '2'

        if self.chk_Visit.isChecked():
            self.visit = True
        else:
            self.visit = False

        if self.chk_Approve.isChecked():
            self.appr = True
        elif self.chk_tidakApprove.isChecked():
            self.appr = False
        else:
            self.appr = '2'

        if self.chk_akad.isChecked():
            self.akad = True
        else:
            self.akad = False

    def nextandDouble(self, selfchk, contrachk, nextchk):
        if selfchk.isChecked():
            contrachk.setChecked(False)
            nextchk.setEnabled(True)
            if self.chk_cstNotApp.isChecked() or self.chk_tidakApprove.isChecked():
                nextchk.setEnabled(False)
                nextchk.setChecked(False)
        else:
            nextchk.setEnabled(False)
            nextchk.setChecked(False)

        self.checkerAll()

    def nextProcess(self, selfchk, otherchk):
        if selfchk.isChecked():
            otherchk.setEnabled(True)
        else:
            otherchk.setChecked(False)
            otherchk.setEnabled(False)

        self.checkerAll()

    def doubleopts(self, selfchk, nextchk1, nextchk2):
        if selfchk.isChecked():
            nextchk1.setEnabled(True)
            nextchk2.setEnabled(True)
        else:
            nextchk1.setEnabled(False)
            nextchk1.setChecked(False)
            nextchk2.setEnabled(False)
            nextchk2.setChecked(False)

        self.checkerAll()

    def persetujuan(self, selfchk, otherchk):
        if selfchk.isChecked():
            otherchk.setChecked(False)

        if self.chk_setuju.isChecked():
            self.setuju = True
        elif self.chk_tidakSetuju.isChecked():
            self.setuju = False
        else:
            self.setuju = '2'

        #print(str(self.setuju))

    def activate1st(self, selfchk, otherchk, act1, act2):
        if self.chk_agent.isChecked():
            self.agent = True
        else:
            self.agent = False
        if self.chk_owner.isChecked():
            self.owner = True
        else:
            self.owner = False

        if selfchk.isChecked() or otherchk.isChecked():
            act1.setEnabled(True)
            act2.setEnabled(True)
        else:
            self.setuju = '2'
            act1.setEnabled(False)
            act1.setChecked(False)
            act2.setEnabled(False)
            act2.setChecked(False)
        #print(str(self.owner)+"-"+str(self.agent))

    def initUI(self):
        self.agent = False
        self.owner = False
        self.setuju = '2'
        self.berkas = False
        self.ondesk = False
        self.ondeskRes = False
        self.cstAppr = None
        self.visit = False
        self.appr = None
        self.akad = False

        self.chk_agent.stateChanged.connect(
            lambda: self.activate1st(self.chk_agent, self.chk_owner, self.chk_setuju, self.chk_tidakSetuju))
        self.chk_owner.stateChanged.connect(
            lambda: self.activate1st(self.chk_agent, self.chk_owner, self.chk_setuju, self.chk_tidakSetuju))
        self.chk_setuju.stateChanged.connect(lambda: self.persetujuan(self.chk_setuju, self.chk_tidakSetuju))
        self.chk_tidakSetuju.stateChanged.connect(lambda: self.persetujuan(self.chk_tidakSetuju, self.chk_setuju))
        self.chk_berkas.stateChanged.connect(lambda: self.nextProcess(self.chk_berkas, self.chk_ondesk))
        self.chk_ondesk.stateChanged.connect(lambda: self.nextProcess(self.chk_ondesk, self.chk_ondeskResult))
        self.chk_ondeskResult.stateChanged.connect(
            lambda: self.doubleopts(self.chk_ondeskResult, self.chk_cstApp, self.chk_cstNotApp))
        self.chk_cstApp.stateChanged.connect(
            lambda: self.nextandDouble(self.chk_cstApp, self.chk_cstNotApp, self.chk_Visit))
        self.chk_cstNotApp.stateChanged.connect(
            lambda: self.nextandDouble(self.chk_cstNotApp, self.chk_cstApp, self.chk_Visit))
        self.chk_Visit.stateChanged.connect(
            lambda: self.doubleopts(self.chk_Visit, self.chk_Approve, self.chk_tidakApprove))
        self.chk_Approve.stateChanged.connect(
            lambda: self.nextandDouble(self.chk_Approve, self.chk_tidakApprove, self.chk_akad))
        self.chk_tidakApprove.stateChanged.connect(
            lambda: self.nextandDouble(self.chk_tidakApprove, self.chk_Approve, self.chk_akad))
        self.btn_save.clicked.connect(self.save)
        self.btn_return.clicked.connect(self.cancel)

        self.getData()

'''if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    premain = QtWidgets.QWidget()
    premain.ui = Ui()
    sys.exit(app.exec_())'''