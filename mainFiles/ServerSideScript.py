import fetcher
import mysql.connector as conn
import schedule
import time

class Server():
    def __init__(self):
        self.ipadd, self.dbcore, self.dboth = fetcher.superData()

        self.ipadd = "127.0.0.1"

        self.counter = 0

        try:
            self.mydb = conn.connect(
                host = self.ipadd,
                user = "root",
                passwd = "root",
                database = self.dboth,
                auth_plugin='mysql_native_password',
                buffered=True
            )
            print("connected")

            self.mycursor = self.mydb.cursor()
        except:
            print("Unable to connect, please reset connection!")

    def dailyRun(self):
        self.counter+=1
        #print("running")
        self.query = "SELECT value FROM params where name = 'NeedReset';"
        self.mycursor.execute(self.query)
        self.reset = self.mycursor.fetchone()[0]

        #print(bool(int(self.reset)))
        if bool(int(self.reset)):
            print("reset")
            self.assignCommand()
            self.query = "update params set value = 0 where name = 'NeedReset';"
            self.mycursor.execute(self.query)
            self.mycursor.execute("commit;")
        else:
            #print("not reset")
            self.query = "SELECT value from params where name = 'DataCircle';"
            self.mycursor.execute(self.query)
            self.assign = self.mycursor.fetchone()[0]
            #print(int(self.assign) == self.counter)
            if int(self.assign) <= self.counter:
                print("run command")
                self.assignCommand()
            else:
                print("dont run")

    def assignCommand(self):
        #clear db first
        self.query = "select kode_produk from products;"
        self.mycursor.execute(self.query)
        self.result = self.mycursor.fetchall()

        print("assign db cleared")

        for x in self.result:
            self.query = "delete from assigned_"+x[0]+";"
            self.mycursor.execute(self.query)
            self.mycursor.execute("commit;")

        self.query = "SELECT username, product from admins where privilege = 'telle' and active_status = True;"
        self.mycursor.execute(self.query)
        self.assignTelle = self.mycursor.fetchall()

        self.query = "SELECT value from params where name = 'DataReset';"
        self.mycursor.execute(self.query)
        self.dataReset = self.mycursor.fetchone()[0]

        self.query = "SELECT value from params where name = 'DataPerTelle';"
        self.mycursor.execute(self.query)
        self.dataLimit = self.mycursor.fetchone()[0]

        for x in self.assignTelle:
            try:
                self.clearDB = "delete from telle_"+x[0]+"_"+x[1]+";"
                self.mycursor.execute(self.clearDB)
                self.mycursor.execute("commit;")
                print("telle "+x[0]+" cleared")

                self.appointmentQuery = "select cust_id from prod_cc where date(recontact) = curdate() and updater = %s;"
                self.mycursor.execute(self.appointmentQuery, (x[0],))
                self.appointment = self.mycursor.fetchall()

                self.dataLimit = str(self.dataLimit) - len(self.appointment)

                self.addAppointment = "insert into telle_"+x[0]+"_"+x[1]+" select cust_id from prod_cc where date(recont" \
                                      "act) = curdate() and updater = %s;"
                self.mycursor.execute(self.addAppointment, (x[0],))
                self.mycursor.execute("commit;")

                self.addAppointment = "insert into assigned_"+x[1]+" select cust_id from prod_cc where date(recont" \
                                      "act) = curdate() and updater = %s;"
                self.mycursor.execute(self.addAppointment, (x[0],))
                self.mycursor.execute("commit;")

                #Need to set recontact status = 0 here#
                self.query = "update prod_"+x[1]+" set recontact_status = 0 where date(recontact) = curdate() and updater = %s;"
                self.mycursor.execute(self.query, (x[0],))
                self.mycursor.execute("commit;")

                if self.dataLimit > 0:
                    self.query = "insert into telle_"+x[0]+"_"+x[1]+" select id from (select * from customers where id not in (select cust_id " \
                                 "from prod_"+x[1]+" where updater = %s) and id not in (select cust_id from prod_"+x[1]+" where updated" \
                                 " between date_sub(curdate(), interval "+self.dataReset+" day) and curdate()) and id not in (select * from assigned_"+x[1]+")" \
                                 " order by rand() limit "+str(self.dataLimit)+") as dbc;"
                    self.mycursor.execute(self.query, (x[0],))
                    self.mycursor.execute("commit;")

                    self.query = "insert into assigned_"+x[1]+" select id from (select * from customers where id not in (select cust_id " \
                             "from prod_"+x[1]+" where updater = %s) and id not in (select cust_id from prod_"+x[1]+" where updated" \
                             " between date_sub(curdate(), interval "+self.dataReset+" day) and curdate()) and id not in (select * from assigned_"+x[1]+")" \
                             " order by rand() limit "+str(self.dataLimit)+") as dbc;"
                    self.mycursor.execute(self.query, (x[0],))
                    self.mycursor.execute("commit;")

            except Exception as e:
                print("Assign telle "+x[0]+" failed.")
                print(e)

        self.counter = 0

coba = Server()
coba.dailyRun()
#print("gg")
schedule.every().day.at("01:00").do(coba.dailyRun)#minute.do(coba.dailyRun)

while True:
    schedule.run_pending()
    time.sleep(60)

