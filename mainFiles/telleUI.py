from PyQt5 import uic, QtWidgets, QtCore
from searchHistory import Ui as srcHistory
from datetime import datetime
from followUp_PL import Ui as follupPL
from followUp_CC import Ui as follupCC
import sys

class Ui(QtWidgets.QWidget):
    def __init__(self, priv, parentWin, mycursor, user, product, target=None, recontact = None):
        super(Ui, self).__init__()
        uic.loadUi('assets/ui/telleUI.ui', self)
        self.showFullScreen()

        self.priv = priv
        self.parentWin = parentWin
        self.mycursor = mycursor
        self.user = user
        self.prd = product
        self.table = "prod_"+product
        self.assign = "assign_"+product
        self.targetID = target
        self.recontact = recontact

        self.setFixedSize(self.width(), self.height())
        self.scrollArea.setGeometry(self.scrollArea.geometry().x(), self.scrollArea.geometry().x(), self.width() - 20,
                                    self.height() - 20)

        #print("badabu")
        self.initUi()
        #print("baboon")
        self.initAddCol()

        if self.recontact:
            self.btn_save.setEnabled(True)
            self.btn_save.setVisible(True)

    def initAddCol(self):
        try:
            self.query = "SELECT col FROM add_data;"
            self.mycursor.execute(self.query)
            self.addtColumn = self.mycursor.fetchall()
            if len(self.addtColumn) > 0:
                self.colAdded = []
                for x in self.addtColumn:
                    #self.nLabel =
                    self.insertData = QtWidgets.QLineEdit()
                    if self.priv == "adm":
                        self.insertData.setEnabled(True)
                    else:
                        self.insertData.setEnabled(False)
                    #print("dobon")
                    self.formLayout.addRow(QtWidgets.QLabel(x[0]), self.insertData)
                    #print("db")
                    self.colAdded.append(self.insertData)

            if len(self.addtColumn) != 0:
                self.query = "SELECT "
                for x in range(len(self.addtColumn)):
                    if x+1==len(self.addtColumn):
                        self.query += self.addtColumn[x][0].lower()+" "
                    else:
                        self.query += self.addtColumn[x][0].lower() + ", "
                self.query += "from customers WHERE id = "+str(self.targetID)+";"
                self.mycursor.execute(self.query)
                self.dd = self.mycursor.fetchone()
                for x in range(len(self.colAdded)):
                    print(self.dd[x])
                    self.colAdded[x].setText(self.dd[x])
        except Exception as e:
            #pass
            print("No additional data")
            print(str(e))

    def initUi(self):
        self.prospect_value = "2"
        self.comment = ""
        self.appointment_type = "Call"
        '''
        self.btn_pickup.setVisible(False)
        self.btn_fpickup.setVisible(False)
        self.btn_info.setVisible(False)
        self.btn_finfo.setVisible(False)
        self.btn_interest.setVisible(False)
        self.btn_finterest.setVisible(False)
        self.btn_abstain.setVisible(False)
        self.lbl_bank.setVisible(False)
        self.cmb_banks.setVisible(False)
        self.lbl_hub.setVisible(False)
        self.in_recontact.setVisible(False)
        self.btn_save.setVisible(False)
        self.btn_next.setEnabled(False)
        self.in_dob.setMaximumDateTime(datetime.now())
        self.txt_reason.setVisible(False)
        self.lbl_reason.setVisible(False)
        self.btn_hp.setVisible(False)
        self.btn_wp.setVisible(False)
        self.btn_cp.setVisible(False)
        self.cmb_appType.setVisible(False)'''

        self.btn_info_0.setVisible(False)
        self.btn_info_1.setVisible(False)
        self.btn_pros_0.setVisible(False)
        self.btn_pros_1.setVisible(False)
        self.btn_pros_2.setVisible(False)
        self.btn_pros_3.setVisible(False)
        self.btn_pros_4.setVisible(False)
        self.btn_leas_0.setVisible(False)
        self.btn_leas_1.setVisible(False)
        self.btn_notInfo_0.setVisible(False)
        self.btn_notInfo_1.setVisible(False)
        self.btn_notInfo_2.setVisible(False)

        #below is same with prev
        self.in_dob.setMaximumDateTime(datetime.now())
        self.txt_reason.setVisible(False)
        self.lbl_reason.setVisible(False)
        self.lbl_bank.setVisible(False)
        self.cmb_banks.setVisible(False)
        self.lbl_hub.setVisible(False)
        self.in_recontact.setVisible(False)
        self.btn_save.setVisible(False)
        self.btn_next.setEnabled(False)

        if self.priv != "adm":
            self.in_name.setEnabled(False)
            self.in_phone.setEnabled(False)
            self.in_merek.setEnabled(False)
            self.in_alamat.setEnabled(False)
            self.in_tipe.setEnabled(False)
            self.in_tahun.setEnabled(False)
            self.in_nopol.setEnabled(False)
            self.in_source.setEnabled(False)
            self.in_dob.setEnabled(False)
            self.btn_save.setVisible(False)
        else:
            self.btn_save.setEnabled(True)
            self.btn_save.setVisible(True)

        self.btn_cls.clicked.connect(self.closeWin)
        self.btn_next.clicked.connect(self.next)

        self.btn_conn_0.clicked.connect(lambda: self.connect(1))
        self.btn_conn_1.clicked.connect(lambda: self.connect(2))
        self.btn_conn_2.clicked.connect(lambda: self.connect(3))
        self.btn_conn_3.clicked.connect(lambda: self.connect(4))
        self.btn_conn_4.clicked.connect(lambda: self.connect(5))

        self.btn_info_0.clicked.connect(lambda: self.informed(1))
        self.btn_info_1.clicked.connect(lambda: self.informed(2))

        self.btn_pros_0.clicked.connect(lambda: self.followInfo(1))
        self.btn_pros_1.clicked.connect(lambda: self.followInfo(2))
        self.btn_pros_2.clicked.connect(lambda: self.followInfo(3))
        self.btn_pros_3.clicked.connect(lambda: self.followInfo(4))
        self.btn_pros_4.clicked.connect(lambda: self.followInfo(5))

        self.btn_notInfo_0.clicked.connect(lambda: self.noInfo(1))
        self.btn_notInfo_1.clicked.connect(lambda: self.noInfo(2))
        self.btn_notInfo_2.clicked.connect(lambda: self.noInfo(3))

        self.btn_history.clicked.connect(self.openHistory)
        self.btn_save.clicked.connect(self.save)
        '''self.btn_connect.clicked.connect(self.cnt)
        self.btn_fconnect.clicked.connect(self.fcnt)
        self.btn_pickup.clicked.connect(self.pick)
        self.btn_fpickup.clicked.connect(self.fpick)
        self.btn_info.clicked.connect(self.inf)
        self.btn_finfo.clicked.connect(self.finf)
        #need to be changed
        self.btn_interest.clicked.connect(self.prospect)
        self.btn_hp.clicked.connect(self.inter)
        self.btn_wp.clicked.connect(self.warmProspect)
        self.btn_cp.clicked.connect(self.coldProspect)
        self.btn_finterest.clicked.connect(self.finter)
        self.btn_abstain.clicked.connect(self.abs)
        self.btn_history.clicked.connect(self.openHistory)
        self.btn_follup.clicked.connect(self.followUp)'''

        self.lbl_product.setText(self.prd.upper())

        #get customer data
        if self.targetID!= None:
            #nama, telp, date_of_birth, alamat, merek_mobil, tipe_mobil, tahun_mobil, nopol, asal_data
            #self.query = "select nama, telp, alamat, asal_data, no_ktp, penghasilan, unique_code, id, cc, date_of_birth" \
            self.query = "select unique_code, nama, telp, date_of_birth, alamat, merek_mobil, tipe_mobil, tahun_mobil, nopol," \
                         " asal_data, id from customers where id = "+str(self.targetID)+";"
            self.btn_next.setVisible(False)
            self.btn_next.setEnabled(False)
        else:
            self.btn_save.setEnabled(False)
            self.query = "select cst.unique_code, nama, telp, date_of_birth, alamat, merek_mobil, tipe_mobil, " \
                         "tahun_mobil, nopol, asal_data, id from " \
                         "(select * from customers where id in (select cust_id from telle_"+self.user+"_"+self.prd+")" \
                         ") as cst left join "+self.table+ \
                         " on id = cust_id where connected = true and note not like 'Hot Prospect' and cust_id not in " \
                         "(select cust_id from "+self.table+" where updated between" \
                         " date_sub(now(), interval 30 day) and now()) or cust_id is null and fetched = false order by updated;"
            # print(self.query)
        self.mycursor.execute(self.query)
        self.cust_data = self.mycursor.fetchone()
        #print(self.cust_data)

        if not (self.cust_data):
            self.btn_history.setEnabled(False)
            self.btn_conn_0.setEnabled(False)
            self.btn_conn_1.setEnabled(False)
            self.btn_conn_2.setEnabled(False)
            self.btn_conn_3.setEnabled(False)
            self.btn_conn_4.setEnabled(False)
            '''self.btn_fconnect.setEnabled(False)
            self.btn_connect.setEnabled(False)'''

            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'Tidak ada data', "Masukkan data baru",
                                                     QtWidgets.QMessageBox.Ok)

        try:
            self.query = "select data_id, connected, received, explained, note, unique_code, updated from "+self.table+" where " \
                            "cust_id = "+str(self.cust_data[10])+" order by updated;"
            self.mycursor.execute(self.query)
            self.n_data = self.mycursor.fetchone()
            try:
                '''self.connected = self.n_data[1]
                self.received = self.n_data[2]
                self.explained = self.n_data[3]
                self.note = self.n_data[4]'''
                #need to revamp data below
                '''self.connect = 
                self.info = None
                self.follows = None
                self.note = None
                self.recontact = None'''

                if self.n_data[0]!= None:
                    self.uniqueCode.setText(self.n_data[0])
                    self.btn_follup.setEnabled(True)
            except:
                print("this")
                self.connected = 0
                self.info = 0
                self.follows = 0
                self.note = None
                self.recontact = None
                '''self.connected = None
                self.received = None
                self.explained = None
                self.note = None
                self.recontact = None'''
        except Exception as e:
            print(e)
            print("or this")
            #print(self.query)
            #print(self.n_data)
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', "Belum ada data",
                                                     QtWidgets.QMessageBox.Ok)

        # kalau ada null di db, ganti jadi ""
        if self.cust_data:
            for x in self.cust_data:
                if x is None:
                    x = ""
            #select unique_code, nama, telp, date_of_birth, alamat, merek_mobil, tipe_mobil, tahun_mobil, nopol, asal
            self.in_name.setText(self.cust_data[1])
            self.in_phone.setText(self.cust_data[2])
            self.in_dob.setDate(self.cust_data[3])
            self.in_alamat.setText(self.cust_data[4])
            self.in_merek.setText(self.cust_data[5])
            self.in_tipe.setText(self.cust_data[6])
            self.in_tahun.setText(self.cust_data[7])
            self.in_nopol.setText(self.cust_data[8])
            self.in_source.setText(self.cust_data[9])

            # terakhir dikontak oleh telle (bisa telle yang sama atau yang berbeda)
            self.lastDate()

    def lastDate(self):
        self.query = "SELECT updated from "+self.table+" where cust_id = "+str(self.cust_data[10])+" order by updated desc;"
        self.mycursor.execute(self.query)
        self.lastUpdate = self.mycursor.fetchall()
        if len(self.lastUpdate) != 0:
            self.dt_lastContact.setDate(self.lastUpdate[0][0])
        else:
            self.dt_lastContact.setDate(QtCore.QDate.currentDate())

    def followUp(self):
        if self.prd.lower() == 'pl':
            self.saveCallResult()
            self.follupWindow = QtWidgets.QWidget()
            self.follupWindow.ui = follupPL(self.priv, self.parentWin, self.mycursor, self.user, self.prd, str(self.cust_data[10]))
            self.close()
        else:
            self.saveCallResult()
            self.follupWindow = QtWidgets.QWidget()
            self.follupWindow.ui = follupCC(self.priv, self.parentWin, self.mycursor, self.user, self.prd,
                                            str(self.cust_data[10]))
            self.close()

    def openHistory(self):
        try:
            self.query = "select id, nama, telp, alamat, asal_data, fetched, merek_mobil, tipe_mobil, " + self.table + ".unique_code, tahun_mobil" \
                            ", updated, followup_date, note, berkas, data_masuk, approval, recontact from customers as cst left " \
                            "join prod_cc on id = cust_id where cust_id = %s order by updated;"
            self.mycursor.execute(self.query,(self.cust_data[10],))
            self.result = self.mycursor.fetchall()
            self.follow = QtWidgets.QWidget()
            self.follow.ui = srcHistory(self.priv, self, self.mycursor, self.result, self.user,
                                    self.prd)
        except Exception as e:
            print("kk")
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

    def save(self):
        if self.in_source.text() != '' and self.in_phone.text() != '':
            try:
                self.data = []
                self.data.append(str(self.in_name.text()))
                self.data.append(str(self.in_phone.text()))
                self.data.append(str(self.in_alamat.toPlainText()))
                #self.data.append(str(self.in_ktp.text()))
                #self.data.append(str(self.in_income.text()))
                #self.data.append(str(self.in_source.text()))
                #self.data.append(self.uniqueCode.text())
                #self.data.append(str(self.in_cc.text()))
                self.data.append(self.in_dob.dateTime().toString('yyyy-MM-dd'))
                self.data.append(self.in_merek.text())
                self.data.append(self.in_tipe.text())
                self.data.append(self.in_tahun.text())
                self.data.append(self.in_nopol.text())
                self.data.append(str(self.in_source.text()))
                self.uniqueCd = self.uniqueCode.text()
                if self.uniqueCd == "":
                    self.uniqueCd = None
                for x in range(len(self.data)):
                    if self.data[x] == '':
                        self.data[x]=None
                self.query = "UPDATE customers SET nama = %s, telp = %s, alamat = %s, date_of_birth = %s, merek_mobil = %s," \
                             "tipe_mobil = %s, tahun_mobil = %s, nopol = %s, asal_data = %s where id = " + str(self.cust_data[10]) + ";"
                #self.query = "UPDATE customers set nama = %s, telp = %s, alamat = %s, asal_data = %s, no_ktp = %s, " \
                #             "penghasilan = %s, cc = %s, date_of_birth = %s where id = " + str(self.cust_data[7]) +";"
                self.inse = (self.data[0], self.data[1], self.data[2], self.data[3], self.data[4], self.data[5],
                             self.data[6], self.data[7], self.data[8])
                self.mycursor.execute(self.query, self.inse)
                self.mycursor.execute("commit;")
            except Exception as e:

                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                         QtWidgets.QMessageBox.Ok)

            #if self.uniqueCd!=None:
            self.prodData()

            self.btn_save.setEnabled(False)
        else:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', 'Phone number and source cannot be empty',
                                                     QtWidgets.QMessageBox.Ok)
        if len(self.addtColumn) > 0:
            self.saveAddt()

    def saveAddt(self):
        self.newDat = []

        for x in self.colAdded:
            if x.text() == '':
                self.newDat.append(None)
            else:
                self.newDat.append(x.text())
        self.newDat = tuple(self.newDat)

        try:
            self.query = "UPDATE customers SET "
            for x in range(len(self.addtColumn)):
                if x+1==len(self.addtColumn):
                    self.query += self.addtColumn[x][0]+"= %s "
                else:
                    self.query += self.addtColumn[x][0] + "= %s, "
            self.query += "WHERE id = "+str(self.cust_data[10])+";"
            self.mycursor.execute(self.query, self.newDat)
            self.mycursor.execute("commit;")
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e), QtWidgets.QMessageBox.Ok)

    def prodData(self):
        try:
            if self.note == "Pikir-pikir":
                self.recontact = self.in_recontact.dateTime().toString('yyyy-MM-dd hh:mm:ss')
                self.appointment_type = "Telepon"
            else:
                self.recontact = None
                self.appointment_type = None
            self.bankChoice = str(self.cmb_banks.currentText())
            self.query = "insert into "+self.table+" (cust_id, connected, received, explained, note, unique_code, updated, updater, recontact, bank" \
                                                   ", prospect, app_type, comment) values" \
                                                    "(%s,"+str(self.connected)+","+str(self.info)+","+str(self.follows)+"" \
                                                    ",%s,%s, curdate(), %s, %s, %s, %s, %s, %s);"
            self.uniqueCd = self.uniqueCode.text()
            if self.uniqueCd == "":
                self.uniqueCd = None
            self.mycursor.execute(self.query, (str(self.cust_data[10]),self.note,self.uniqueCd, self.user, self.recontact
                                               , self.bankChoice, self.follows, self.appointment_type, self.comment))
            self.mycursor.execute("commit;")
        except Exception as e:
            #print(str(e))
            print("ll")
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

    def connect(self, cnn):
        self.btn_conn_0.setEnabled(False)
        self.btn_conn_1.setEnabled(False)
        self.btn_conn_2.setEnabled(False)
        self.btn_conn_3.setEnabled(False)
        self.btn_conn_4.setEnabled(False)

        self.connected = cnn

        '''print(type(cnn))
        print(cnn)'''
        #open next phase if cnn 1
        if (cnn == 1):
            self.btn_info_0.setEnabled(True)
            self.btn_info_1.setEnabled(True)
            #set visible
            self.btn_info_0.setVisible(True)
            self.btn_info_1.setVisible(True)

    def informed(self, inf):
        self.btn_info_0.setEnabled(False)
        self.btn_info_1.setEnabled(False)
        self.info = inf

        #yes
        if (inf == 1):
            self.btn_pros_0.setEnabled(True)
            self.btn_pros_1.setEnabled(True)
            self.btn_pros_2.setEnabled(True)
            self.btn_pros_3.setEnabled(True)
            self.btn_pros_4.setEnabled(True)

            #set visible
            self.btn_pros_0.setVisible(True)
            self.btn_pros_1.setVisible(True)
            self.btn_pros_2.setVisible(True)
            self.btn_pros_3.setVisible(True)
            self.btn_pros_4.setVisible(True)

        elif (inf == 2):
            self.btn_notInfo_0.setEnabled(True)
            self.btn_notInfo_1.setEnabled(True)
            self.btn_notInfo_2.setEnabled(True)

            #set visible
            self.btn_notInfo_0.setVisible(True)
            self.btn_notInfo_1.setVisible(True)
            self.btn_notInfo_2.setVisible(True)

    def followInfo(self, foll):
        self.btn_pros_0.setEnabled(False)
        self.btn_pros_1.setEnabled(False)
        self.btn_pros_2.setEnabled(False)
        self.btn_pros_3.setEnabled(False)
        self.btn_pros_4.setEnabled(False)

        self.follows = foll

        #dont forget to edit the db and process here
        if (foll == 1):
            #continue to leasing
            self.lbl_bank.setVisible(True)
            self.cmb_banks.setVisible(True)
            self.cmb_banks.setEnabled(True)


        elif (foll == 5):
            self.lbl_reason.setVisible(True)
            self.txt_reason.setVisible(True)
            self.txt_reason.setEnabled(True)
        else:
            self.lbl_hub.setVisible(True)
            self.in_recontact.setVisible(True)
            self.in_recontact.setEnabled(True)

        if foll == 1:
            self.note = "Hot Prospect"
            self.btn_next.setEnabled(True)
            self.btn_follup.setEnabled(True)

            self.prod = self.prd.upper()
            self.cd = self.cust_data[0][:4] + "/" + self.prod + self.cust_data[0][4:]
            try:
                self.uniqueCode.setText(self.cd)
            except Exception as e:
                print(e)
                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                         QtWidgets.QMessageBox.Ok)

            try:
                self.query = "SELECT nama_bank from bank_" + self.prd + ";"
                self.mycursor.execute(self.query)
                self.banks = self.mycursor.fetchall()
                for x in self.banks:
                    self.cmb_banks.addItem(x[0])

            except Exception as e:
                self.buttonReply = QtWidgets.QMessageBox
                self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                         QtWidgets.QMessageBox.Ok)

            self.btn_save.setVisible(True)
            self.btn_save.setEnabled(True)
        elif foll == 2:
            self.note = "Warm Prospect"
        elif foll == 3:
            self.note = "Pertimbangan"
        elif foll == 4:
            self.note = "Telepon Ulang"
        else:
            self.note = "Tidak Tertarik"

    def noInfo(self, nIf):
        self.btn_notInfo_0.setEnabled(False)
        self.btn_notInfo_1.setEnabled(False)
        self.btn_notInfo_2.setEnabled(False)

        self.follows = nIf

        if str(nIf) == "6":
            self.note = "Salah Sambung"
        elif str(nIf) == "7":
            self.note = "Reject"
        else:
            self.note = "Sibuk"
    '''#Fungsi warm prospect
    def warmProspect(self):
        self.prospect_value = "2"
        self.comment = "Warm Prospect"
        self.btn_next.setEnabled(True)
        self.btn_next.setVisible(True)
        self.btn_cp.setEnabled(False)
        self.btn_hp.setEnabled(False)
        self.btn_wp.setEnabled(False)
        #self.btn_

    #Fungsi cold prospect
    def coldProspect(self):
        self.prospect_value = "3"
        self.comment = "Cold Prospect"
        self.btn_next.setEnabled(True)
        self.btn_next.setVisible(True)
        self.btn_wp.setEnabled(False)
        self.btn_hp.setEnabled(False)
        self.btn_cp.setEnabled(False)

    def prospect(self):
        self.note = "Tertarik"
        self.btn_hp.setVisible(True)
        self.btn_wp.setVisible(True)
        self.btn_cp.setVisible(True)
        self.btn_hp.setEnabled(True)
        self.btn_wp.setEnabled(True)
        self.btn_cp.setEnabled(True)
        self.btn_finterest.setEnabled(False)
        self.btn_abstain.setEnabled(False)
        self.btn_interest.setEnabled(False)

    def abs(self):
        self.note = "Pikir-pikir"
        self.prospect_value = "2"
        self.comment = "Appointment"
        self.lbl_hub.setVisible(True)
        self.in_recontact.setVisible(True)
        self.in_recontact.setEnabled(True)
        self.btn_next.setEnabled(True)
        self.in_recontact.setDateTime(datetime.now())
        self.cmb_appType.setVisible(True)
        self.cmb_appType.setEnabled(True)

    def finter(self):
        self.note = "Tidak"
        self.prospect_value = "2"
        self.btn_interest.setEnabled(False)
        self.btn_finterest.setEnabled(False)
        self.btn_abstain.setEnabled(False)
        self.btn_next.setEnabled(True)
        self.txt_reason.setVisible(True)
        self.lbl_reason.setVisible(True)
        self.txt_reason.setEnabled(True)
        self.lbl_reason.setEnabled(True)

    def inter(self):
        self.prospect_value = "1"
        self.comment = "Hot Prospect"
        #print(self.note)
        self.prod = self.prd.upper()
        self.cd = self.cust_data[6][:4]+"/"+self.prod+self.cust_data[6][4:]
        try:
            self.uniqueCode.setText(self.cd)
        except Exception as e:
            print(e)
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)
        #print(self.uniqueCode.text())
        #print(self.note)
        self.btn_wp.setEnabled(False)
        self.btn_cp.setEnabled(False)
        self.btn_hp.setEnabled(False)

        self.btn_interest.setEnabled(False)
        #self.btn_finterest.setEnabled(False)
        #self.btn_abstain.setEnabled(False)
        self.lbl_bank.setVisible(True)
        self.cmb_banks.setVisible(True)
        self.btn_next.setEnabled(True)
        self.btn_follup.setEnabled(True)

        try:
            self.query = "SELECT nama_bank from bank_"+self.prd+";"
            self.mycursor.execute(self.query)
            self.banks = self.mycursor.fetchall()
            for x in self.banks:
                self.cmb_banks.addItem(x[0])
        except Exception as e:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                     QtWidgets.QMessageBox.Ok)

    def finf(self):
        self.explained = False
        self.note= "Tidak"
        self.btn_info.setEnabled(False)
        self.btn_finfo.setEnabled(False)
        self.btn_next.setEnabled(True)
        self.txt_reason.setVisible(True)
        self.lbl_reason.setVisible(True)
        self.txt_reason.setEnabled(True)
        self.lbl_reason.setEnabled(True)

    def inf(self):
        self.explained = True
        self.btn_info.setEnabled(False)
        self.btn_finfo.setEnabled(False)
        self.btn_interest.setVisible(True)
        self.btn_finterest.setVisible(True)
        self.btn_abstain.setVisible(True)
        self.btn_interest.setEnabled(True)
        self.btn_finterest.setEnabled(True)
        self.btn_abstain.setEnabled(True)

    def fpick(self):
        self.received = False
        self.explained = False
        self.note = "Tidak"
        self.btn_pickup.setEnabled(False)
        self.btn_fpickup.setEnabled(False)
        self.btn_next.setEnabled(True)
        self.txt_reason.setVisible(True)
        self.lbl_reason.setVisible(True)
        self.txt_reason.setEnabled(True)
        self.lbl_reason.setEnabled(True)

    def pick(self):
        self.received = True
        self.btn_pickup.setEnabled(False)
        self.btn_fpickup.setEnabled(False)
        self.btn_info.setVisible(True)
        self.btn_finfo.setVisible(True)
        self.btn_info.setEnabled(True)
        self.btn_finfo.setEnabled(True)

    def fcnt(self):
        self.connected=False
        self.received=False
        self.explained=False
        self.note="Tidak"
        self.btn_fconnect.setEnabled(False)
        self.btn_connect.setEnabled(False)
        self.btn_next.setEnabled(True)
        self.txt_reason.setVisible(True)
        self.lbl_reason.setVisible(True)
        self.txt_reason.setEnabled(True)
        self.lbl_reason.setEnabled(True)

    def cnt(self):
        self.connected = True
        self.btn_connect.setEnabled(False)
        self.btn_fconnect.setEnabled(False)
        self.btn_pickup.setVisible(True)
        self.btn_fpickup.setVisible(True)
        self.btn_pickup.setEnabled(True)
        self.btn_fpickup.setEnabled(True)
'''
    def closeWin(self):
        self.parentWin.show()
        self.close()

    def saveCallResult(self):
        print("dasdasd")
        if self.note != "Pikir-pikir":
            self.appointment_type = "-"
        else:
            self.appointment_type = self.cmb_appType.currentText()

        if self.comment == "" and self.note == "Tidak Tertarik":
            self.comment = self.txt_reason.toPlainText()
        else:
            self.comment = self.note

        if self.comment!="":
            self.uniqueCd = self.uniqueCode.text()
            if self.uniqueCode.text() != '':
                self.prodData()
            else:
                try:
                    #vars = connected, info, follows
                    self.bankChoice = str(self.cmb_banks.currentText())
                    self.query = "insert into " + self.table + " (cust_id, connected, received, explained, note, updated, " \
                                                               "updater, prospect, app_type, comment) values" \
                                                               "(%s," + str(self.connected) + "," + str(self.info) + ","\
                                                                + str(self.follows) + "" \
                                                                ",%s, curdate(), %s, %s, %s, %s);"
                    #self.query, (str(self.cust_data[7]), self.note, self.user)
                    self.mycursor.execute(self.query,
                                          (str(self.cust_data[10]), self.note, self.user, str(self.follows),
                                           self.appointment_type, self.comment))

                    self.mycursor.execute("commit;")
                    print("success")
                    return True
                except Exception as e:
                    print("Masuk exc insert")
                    # print(str(e))
                    self.buttonReply = QtWidgets.QMessageBox
                    self.warning = self.buttonReply.question(self, 'WARNING', str(e),
                                                             QtWidgets.QMessageBox.Ok)
                    return False
        else:
            self.buttonReply = QtWidgets.QMessageBox
            self.warning = self.buttonReply.question(self, 'WARNING', "Reason cannot be empty",
                                                     QtWidgets.QMessageBox.Ok)
            return False

    def next(self):
        clear = self.saveCallResult()
        if clear:
            self.nextCust = QtWidgets.QWidget()
            self.nextCust.ui = Ui(self.priv, self.parentWin, self.mycursor, self.user, self.prd)
            self.close()
        #ambil lagi dari result yang fetched = 0, set yang ini fetched = 1
        #waktu insert updated
        #self.parentWin

'''if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    premain = QtWidgets.QMainWindow()
    premain.ui = Ui()
    sys.exit(app.exec_())'''