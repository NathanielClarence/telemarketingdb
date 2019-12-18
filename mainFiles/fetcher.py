def superData():
    dt = open("assets/superadmin.dct", 'r')
    ipadd = dt.readline().rstrip()
    dbcore = dt.readline().rstrip()
    othdb = dt.readline().rstrip()
    dt.close()
    return ipadd, dbcore, othdb

def admData():
    dt = open("assets/othadmin.dct",'r')
    ipadd = dt.readline().rstrip()
    uname = dt.readline().rstrip()
    psw = dt.readline().rstrip()
    dbcore = dt.readline().rstrip()
    dt.close()
    return ipadd, uname, psw, dbcore