import ftplib
import os

dbase = []
dbnom = ""
usnm,pasw = "epiz_24763533", "Hyg63aDtH4tjNy"
def Convert(string): 
    li = list(string.split(",")) 
    return li

def display(dn):
    nms = dbase[0]
    dbstr = ""
    lenrow = 0
    mltms = []
    cols = []
    for l in dbase:
        if len(l) > lenrow:
            lenrow += len(l) + 1
    for j in range(0,lenrow - 1):
        mltms.append("0")
    for t in mltms:
        cols.append("" * int(t))
    for k in dbase:
        for n in range(0, len(mltms)):
            if len(k[n]) > int(mltms[n]):
                mltms[n] = str(len(k[n]))
    for k in dbase:
        item = ""
        for h in range(0,len(k)):
            itm = ""
            itm += " | " + k[h]
            itm += " " * ((int(mltms[h]) - len(k[h])) + 2)
            item += itm              
        dbstr += item + "|" + "\n"         
    dbstr = dbstr.rstrip("\n")
    print(" " * ((len(item) // 2) - (len(dn) // 2)) + dn.upper() + "\n", ("=" * (len(item))))
    print(dbstr)
    print("","=" * (len(item)))

def download(file):
    file += ".db"
    ftp = ftplib.FTP("ftpupload.net")
    ftp.login(usnm,pasw)
    ftp.cwd("/htdocs/")
    print("trying to load database...")
    try:
        ftp.retrbinary("RETR " + file, open(file, "wb").write)
        data = open(file, "r").readlines()
        for i in range(0,len(data)):
            data[i] = str(data[i].replace('\n', ''))
            ext = Convert(data[i])
            dbase.append(ext)
        dbnom = file.replace(".db","")
        os.remove(file)
        print("loaded database '" + dbnom + "' successfully.")
        print()
        display(file.replace(".db",""))
        print()
    except:
        print("failed to load database.")
        os.remove(file + ".db")
    ftp.quit()
    
def upload(file):
    ftp = ftplib.FTP("ftpupload.net")
    ftp.login(usnm,pasw)
    ftp.cwd("/htdocs/")
    ftp.storbinary("STOR " + file, open(file, "rb"), 1024)
    ftp.quit()
    os.remove(file)
    print("saved database successfully.")
    
def getdbs():
    ftp = ftplib.FTP("ftpupload.net")
    ftp.login(usnm,pasw)
    ftp.cwd("/htdocs/")
    contents = ftp.nlst()
    ftp.quit()
    return contents

def delete(file):
    ftp = ftplib.FTP("ftpupload.net")
    ftp.login(usnm,pasw)
    ftp.cwd("/htdocs/")
    ftp.delete(file)
    ftp.quit()
    os.remove(file)
    
intro = '''
  _____        _        ____            _                  
 |  __ \      | |      |  _ \          (_)                 
 | |  | | __ _| |_ __ _| |_) | __ _ ___ _  ___             
 | |  | |/ _` | __/ _` |  _ < / _` / __| |/ __|            
 | |__| | (_| | || (_| | |_) | (_| \__ \ | (__ _           
 |_____/ \__,_|\__\__,_|____/ \__,_|___/_|\___( )__      __
 | |               /\      | (_) |            |/ \ \    / /
 | |__  _   _     /  \   __| |_| |_ _   _  __ _   \ \  / / 
 | '_ \| | | |   / /\ \ / _` | | __| | | |/ _` |   \ \/ /  
 | |_) | |_| |  / ____ \ (_| | | |_| |_| | (_| |    \  /   
 |_.__/ \__, | /_/    \_\__,_|_|\__|\__, |\__,_|     \(_)  
         __/ |                       __/ |                 
        |___/                       |___/
        
'''
hlp = '''
 DATABASE HELP
 ----------------------------------------------------------------
 NAME   PARAMS               FUNCTION
 load   (name)               loads a pre existing database from server
 new    (name)               creates new database. add column names on
                             prompt, as CSVs
 lst                         lists all databases on server
 add    (id,data,...)        adds record using input CSVs
 show                        shows database
 raw                         prints raw data
 rem    (id)                 deletes record with specified id
 ren    (name)               renames the database
 edit   (row,col,data)       modifies value at specified position
                             in the row with specified id to given
                             new value.
 swap   (id1,id2)            swaps position of records of specified ids
 sort                        sorts database in descending al-num order
 delete (name)               deletes a pre existing database from server
                             or local file (if unsaved)
 commit                      uploads current database
 disp   (id)                 displays record with given id
 h                           displays help
 export                      exports database as a json file
 cols   (add) or (rem srl)   add new column, or remove the column at
                             position srl

 TIP: you can simply put the command and params in the same line.
 for example, typing 'add abc,100' will add 'abc' , '100' to a
 new row in the database. Or, you can input the command and params
 separately as well.

 TIP: for online databases, changes are not registered until you
 upload the database using the 'commit' command.  
'''
print(intro)
print("starting session...")
while True:
    inp = str(input("command (h for help)> "))
    if "load" in inp:
        if inp != "load":
            inp = inp[5:len(inp)]
        else:
            inp = str(input("enter name of database> "))
        download(inp)
        if len(dbase) > 0:
            dbnom = inp
        else:
            dbnom = ""
    elif "new" in inp:
        if inp != "new":
            inp = inp[4:len(inp)]           
        else:
            inp = str(input("enter name of database> "))
        dbnom = inp
        dbase = []
        print("new database '" + dbnom + "' created.")
    elif "add" in inp:
        if inp == "add":
            b = str(input("Enter CSVs (id,data,...)> "))
        else:
            b = inp[4:len(inp)]
        dta = []
        dta = Convert(b)
        if len(dbase) > 0:
            if len(dta) == len(dbase[0]):
                dbase.append(dta)
            else:
                print("cannot add data due to incorrect number of items")
        else:
            dbase.append(dta)
            print("added entry ",dta," to database")
    elif inp == "show":
        display(dbnom)
    elif inp == "commit":
        print("saving database...")
        file1 = open(dbnom + ".db","w")
        txt = ""
        for i in dbase:
            for j in i:
                txt += j + ","
            txt = txt.rstrip(",")
            txt += "\n"                
        file1.writelines(txt)
        file1.close()
        upload(dbnom + ".db")
    elif "rem" in inp:
        if inp == "delete":
            inc = str(input("enter record id> "))
        else:
            inc = inp[7:len(inp)]
        flg = 0
        for l in dbase:
            if inc in l[0]:
                flg = 1
                dbase.remove(l)
        if flg == 0:
            print("Entry with given id not found")
        else:
            print("Entry/entries successfully removed")
    elif "delete" in inp:
        if inp == "delete":
            delete(dbnom + ".db")
    elif inp == "raw":
        print(dbase)
    elif "swap" in inp:
        if inp != swap:
            inp = inp[5:len(inp)]
        else:
            inp = str(input("enter ids (id1,i2)> "))
            swapit = Convert(inp)
    elif inp == "h":
        print(hlp)
    elif "sort" in inp:
        dbase.sort()
        print("sorted successfully")
        display(dbnom)
    elif "disp" in inp:
        if inp != "disp":
            inp = inp[5:len(inp)]
        else:
            inp = str(input("enter record id> "))
        flag = 0
        for dt in dbase:
            if (dt[0] in inp) or (inp in dt[0]):
                print("found record",dt)
                flag = 1
        if flag == 0:
            print("no matches found")
    elif "list" in inp:
        dbs = getdbs()
        for itr in dbs:
            if ".db" in itr:
                print("-",itr.rstrip(".db"))
    else:
        print("incorrect command or syntax")
