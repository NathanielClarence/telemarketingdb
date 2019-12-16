import mysql.connector as conn

uname = input('Masukkan username: ')
passw = input('Masukkan password: ')

mydb = conn.connect(
    host = "localhost",
    user = uname,
    passwd = passw,
    database = "dbtest",
    auth_plugin='mysql_native_password'
)

new_uname = input('Pengguna baru: ')
new_pwd = input('Password pengguna: ')

mycursor = mydb.cursor()
#try:
add_user = "CREATE USER %s@'localhost' IDENTIFIED BY %s;"
data = (new_uname, new_pwd)
print("pass")
mycursor.execute(add_user, data)
mycursor.execute("""GRANT ALL PRIVILEGES ON *. * TO %s@'localhost' with grant option;""", (new_uname,)) #-> new acc can add user
#mycursor.execute("""GRANT ALL PRIVILEGES ON dbtest. * TO %s@'localhost' with grant option;""", (new_uname,)) #-> new acc cant add new user
mycursor.execute("""show grants for %s@'localhost'""",(new_uname, ))
grants = mycursor.fetchall()
print(grants)

conn.close()
#except:
#    print("failed")

#Plan:
# admin can add user
# admin got *.* + grant option
# mod can only in db (dbtest.*) w/o grant option
# do not use autocommit (default disabled)

#Revoke access (by admin):
#REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'username'@'localhost';
#drop user 'username'@'localhost'