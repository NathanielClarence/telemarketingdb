import fetcher
import mysql.connector as conn
import schedule
import time

class Server():
    def __init__(self):
        self.ipadd, self.dbcore, self.dboth = fetcher.superData()

        self.ipadd = "127.0.0.1"

        self.counter = 768

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
        #print("running")
        self.query = "SELECT value FROM params where name = 'NeedReset';"
        self.mycursor.execute(self.query)
        self.reset = self.mycursor.fetchone()[0]

        #print(bool(int(self.reset)))
        if bool(int(self.reset)):
            print("reset")
        else:
            #print("not reset")
            self.query = "SELECT value from params where name = 'DataCircle';"
            self.mycursor.execute(self.query)
            self.assign = self.mycursor.fetchone()[0]
            #print(int(self.assign) == self.counter)
            if int(self.assign) == self.counter:
                print("run command")
            else:
                print("dont run")

    def assignCommand(self):
        self.query = "SELECT username, product from admins where privilege = 'telle' and active_status = True;"
        self.mycursor.execute(self.query)
        self.assignTelle = self.mycursor.fetchall()

        '''for x in self.assignTelle:
            self.query = "insert into telle_"+x[0]+"_"+x[1]'''

coba = Server()
coba.dailyRun()
#print("gg")
'''schedule.every().day.at("01:00").do(coba.runCommand)

while True:
    schedule.run_pending()
    time.sleep(60)
    '''

