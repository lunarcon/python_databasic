import ftplib
import os
import time

dbase = []
dbnom = ""
usnm,pasw = "epiz_24763533", "Yg91ovaLLqOkeg"
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
    try:
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
    except:
        print("login failed")

def tutorial():
    ftp = ftplib.FTP("ftpupload.net")
    try:
        ftp.login(usnm,pasw)
        ftp.cwd("/htdocs/")
        print("downloading tutorial file...")
        try:
            ftp.retrbinary("RETR " + "tutorial.txt", open("tutorial.txt", "wb").write)
            data = open("tutorial.txt", "r").readlines()
            print("TUTORIAL (approx 45 seconds long)")
            for i in range(0,len(data)):
                print(data[i].rstrip("\n"))
                time.sleep(1)
            os.remove("tutorial.txt")
        except:
            print("there was a problem.")
    except:
        print("could not access server")

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
 NAME     PARAMS              FUNCTION
 load     (name)              loads a pre existing database from server
 lcsv     (name)              loads a local csv file as a database
 uload                        unloads current database from memory. changes are
                              not saved
 new      (name)              creates new database
 list                         lists all databases on server
 add      (id,data,...)       adds row using input CSVs
 show                         shows database 
 raw                          prints raw data
 
 rem      (data)              deletes record(s) which contains specified data
 rem at   (row,col)           deletes record at given position (zero-based)
 
 ren      (name)              renames the database
 edit     (row,col)           modifies value at specified position (zero-based)
 sort                         sorts database in descending al-num order
 delete   (name)              deletes a pre existing database from server
                              or local file (if unsaved)
 commit                       uploads current database
 
 disp     (data)              displays row(s) with given data
 disp at  (row)               displays row at specified position (zero-based)
 
 h                            displays help
 
 cols add                     adds new column at the rightmost position
 cols rem (col)               removes the column at specified position (zero-based)
 
 idices   (data)              prints row,col(s) at which specified data is located
 exit                         exits databasic. changes are not saved
 ?                            begin tutorial (yes, that IS a question mark)

 TIP: arguments and parameters are case sensitive.
'''
print(intro)
print("starting session...")
ctr = 0
while True:
    if ctr == 0:
        inp = str(input("Start Tutorial? (y/n)> "))
        if inp == "y":
            tutorial()
        print()
    inp = str(input("command (h for help)> "))
    ctr = 1
    if inp[0:4] == "load":
        if inp != "load":
            inp = inp[5:len(inp)]
            download(inp)
            if len(dbase) > 0:
                dbnom = inp
            else:
                dbnom = ""
        else:
            print("no arguments specified.")
            print("tip: to load database named 'data', type load data")
    elif inp[0:4] == "lcsv":
        if inp != "load":
            inp = inp[5:len(inp)]
            try:
                data = open(inp + ".csv", "r").readlines()
                for i in range(0,len(data)):
                    data[i] = str(data[i].replace('\n', ''))
                    ext = Convert(data[i])
                    dbase.append(ext)
                dbnom = file.replace(".csv","")
                os.remove(file)
                print("loaded database '" + dbnom + "' successfully.")
                print()
                display(file.replace(".csv",""))
            except:
                print("an error occured. check if file exists, and is in the same directory")
            if len(dbase) > 0:
                dbnom = inp
            else:
                dbnom = ""            
        else:
            print("no arguments specified.")
            print("tip: to load csv named 'data', type lcsv data")
            
    elif "new" in inp:
        if inp != "new":
            inp = inp[4:len(inp)]
            dbnom = inp
            dbase = []
            print("new database '" + dbnom + "' created.")            
        else:
            print("no arguments specified")
            print("tip: to create a database named 'data', type new data")
    elif inp == "unload":
        inp = input("changes will not be saved. proceed? (y\n)> ")
        if inp == "y":
            dbnom = inp
            dbase = []
        else:
            print("operation was cancelled.")        
    elif inp[0:3] == "add":
        if inp == "add":
            b = str(input("enter CSVs (data0,data1,...)> "))
        else:
            b = inp[4:len(inp)]
        dta = []
        dta = Convert(b)
        if len(dbase) > 0:
            if len(dta) == len(dbase[0]):
                dbase.append(dta)
            else:
                print("cannot add row due to incorrect number of items")
        else:
            dbase.append(dta)
            print("added row ",dta," to database")
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
    elif inp[0:3] == "rem":
        if inp == "rem":
            print("no arguments specified.")
            print("tip: to remove item at position 0,1 type rem at 0,1")
            print("     to remove all items with data 'x' type rem x")
        elif "rem at" in inp:
            ij = Convert(inp[6:len(inp)])
            try:
                dbase[int(ij[0])][int(ij[1])] = ""
                print("removed item at specified index.")
            except:
                if len(ij) == 2:
                    print("some index was out of range. max row index is",str(len(dbase)-1)+ ",","max col index is",str(len(dbase[0])-1))
                    print("tip: indices start from 0")
                else:
                    print("no indices specified")
        else:
            inc = inp[4:len(inp)]
            flg = 0
            for l in range(0,len(dbase)):
                for i in range(0,len(dbase[l])):
                    if inc in dbase[l][i]:
                        dbase[l][i] = ""
                        flg = 1
            if flg == 0:
                print("record(s) with given data not found")
            else:
                print("record(s) successfully removed")
    elif inp[0:6] == "delete":
        if inp == "delete":
            delete(dbnom + ".db")
    elif inp[0:2] == "raw":
        print(dbase)
    elif inp[0:4] == "edit":
        if inp != "edit":
            inp = inp[5:len(inp)]
        else:
            inp = str(input("enter id (row,col)> "))
        ij = Convert(inp)
        try:
            inp = input("editing '"+dbase[int(ij[0])][int(ij[1])]+"'. new data(\c to cancel)> ")
            if inp != "\c":
                dbase[int(ij[0])][int(ij[1])] = inp
            else:
                print("operation was cancelled.")
        except:
            print("some index was out of range. max row index is",str(len(dbase)-1)+ ",","max col index is",str(len(dbase[0])-1))
            print("tip: indices start from 0")
    elif inp == "h":
        print(hlp)
    elif inp == "sort":
        dbase.sort()
        print("sorted successfully")
        display(dbnom)
    elif inp[0:4] == "disp":
        if inp == "disp":
            print("no arguments specified.")
            print("tip: to display row at position 0 type disp at 0")
            print("     to display all items with data 'x' type disp x")
        elif "disp at" in inp:
            ij = Convert(inp[7:len(inp)])
            try:
                print(dbase[int(ij[0])])
            except:
                if len(ij) == 1:
                    print("some index was out of range. max row index is",str(len(dbase)-1))
                    print("tip: indices start from 0")
                else:
                    print("no indices specified")
        else:
            inc = inp[5:len(inp)]
            flg = 0
            for l in range(0,len(dbase)):
                for j in range(0,len(dbase[l])):
                    if inc in dbase[l][j]:
                        print(dbase[l])
                        flg = 1
            if flg == 0:
                print("row(s) with given data not found.")
    elif inp == "list":
        dbs = getdbs()
        for itr in dbs:
            if ".db" in itr:
                print("-",itr.rstrip(".db"))
    elif inp[0:4] == "cols":
        if inp != "cols":
            if inp == "cols add":
                for i in range(0,len(dbase)):
                    dbase[i].append("")
                print("added empty column at position",str(len(dbase[0])-1))
            elif "cols rem" in inp and inp != "cols rem":
                ij = int(inp[8:len(inp)])
                try:
                    for i in range(0,len(dbase)):
                        dbase[i].pop(ij)
                    print("removed column at position",ij)
                except:
                    print("some index was out of range. max col index is",str(len(dbase[0])-1))
                    print("tip: indices start from 0")
            else:
                print("no arguments specified.")
                print("tip: to add a blank column at rightmost position, type cols add")
                print("     to remove the column as position x (zero-based), type cols rem x")
        else:
            print("no arguments specified.")
            print("tip: to add a blank column at rightmost position, type cols add")
            print("     to remove the column as position x (zero-based), type cols rem x")            
    elif inp == "?":
        inp = str(input("Start Tutorial? (y/n)> "))
        if inp == "y":
            tutorial()
        print()
    elif inp[0:6] == "idices":
        if inp != "idices":
            inc = inp[7:len(inp)]
            flg = 0
            for l in range(0,len(dbase)):
                for j in range(0,len(dbase[l])):
                    if inc in dbase[l][j]:
                        print("found at",l,",",j)
                        flg = 1
            if flg == 0:
                print("row(s) with given data not found.")
        else:
            print("no arguments specified.")
            print("tip: to get row,col of items with data 'x', type idices x")
    else:
        print("incorrect command or syntax")
