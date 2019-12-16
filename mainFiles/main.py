'''import mysql.connector as conn'''
from PyQt5 import QtWidgets, uic
import sys
from superLogin import Ui as spLogin
from standardLogin import Ui as stdLogin

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('assets/ui/chooseLogin.ui', self)
        #self.wdw = self
        self.setFixedSize(self.width(), self.height())
        self.show()
        self.sa_Login.clicked.connect(self.superLogin)
        self.adm_Login.clicked.connect(lambda: self.standard("adm"))
        self.tel_Login.clicked.connect(lambda: self.standard("tele"))
        self.exit.clicked.connect(self.clsWindow)

    def superLogin(self):
        self.openWindow = QtWidgets.QDialog()
        self.openWindow.ui = spLogin(self)

    def standard(self, priv):
        self.openWindow = QtWidgets.QDialog()
        self.openWindow.ui = stdLogin(priv, self)

    def clsWindow(self):
        QtWidgets.qApp.quit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    premain = QtWidgets.QMainWindow()
    premain.ui = Ui()
    sys.exit(app.exec_())

'''mydb = conn.connect(
    host = "localhost",
    user = "ruchid",
    passwd = "admin",
    database = "dbtest",
    #port = 3306,
    auth_plugin='mysql_native_password'#,
    #wait_timeout = 28800,
    #interactive_timeout = 28800
)'''

#admin/add user syntax
#CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
#GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost' with grant option; #-> for admin only
#grant all privileges on *.* to 'newuser'@'localhost'; #-> for user/mod

'''mycursor = mydb.cursor()
n_input = input('Masukkan nama: ')'''
#a_input = input('Masukkan alamat: ')

'''mycursor.execute("""Select * from customers where name = %s""", (n_input, ))'''
#mycursor.execute("""Select * from admins""")
#mycursor.execute("Select * from customers where name = '"+n_input+"'", multi=True)
'''result = mycursor.fetchall() #-> list of list'''
#result = mycursor.fetchone() #-> list
'''try:
    print(result)
except TypeError:
    print("invalid input")'''

#mycursor.close()
#mydb.close()

'''create table admins(
    -> id int(15) not null auto_increment,
    -> username varchar(32) not null
    -> , password varchar(1000),
    -> constraint id_pk primary key(id)
    -> );
Query OK, 0 rows affected, 1 warning (1.00 sec)

mysql> select * from admins;
Empty set (0.00 sec)

mysql>'''

'''insert into admins(username, password) values ('admin1', sha2('admin1', 512));

mysql> select * from admins;
+----+----------+----------------------------------------------------------------------------------------------------------------------------------+
| id | username | password                                                                                                                         |
+----+----------+----------------------------------------------------------------------------------------------------------------------------------+
|  1 | admin1   | 58b5444cf1b6253a4317fe12daff411a78bda0a95279b1d5768ebf5ca60829e78da944e8a9160a0b6d428cb213e813525a72650dac67b88879394ff624da482f |
+----+----------+----------------------------------------------------------------------------------------------------------------------------------+'''

'''CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost' WITH GRANT OPTION;

CREATE USER 'username'@'%' IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON *.* TO 'username'@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;
'''