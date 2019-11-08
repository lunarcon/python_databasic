import ftplib
import os

dbase = []
dbnom = ""

def Convert(string): 
    li = list(string.split(",")) 
    return li

def download(file):
    file += ".txt"
    ftp = ftplib.FTP("ftpupload.net")
    ftp.login("epiz_24763533", "Hyg63aDtH4tjNy")
    ftp.cwd("/htdocs/")
    print("trying to load database...")
    try:
        ftp.retrbinary("RETR " + file, open(file, "wb").write)
        data = open(file, "r").readlines()
        for i in range(0,len(data)):
            data[i] = str(data[i].replace('\n', ''))
            ext = Convert(data[i])
            dbase.append(ext)
        dbnom = file.replace(".txt","")
        os.remove(file)
        print("loaded database '" + dbnom + "' successfully.")
    except:
        print("failed to load database.")    
    ftp.quit()
    
def upload(file):
    ftp = ftplib.FTP("ftpupload.net")
    ftp.login("epiz_24763533", "Hyg63aDtH4tjNy")
    ftp.cwd("/htdocs/")
    ftp.storbinary("STOR " + file, open(file, "rb"), 1024)
    ftp.quit()
    print("done.")

def delete(file):
    ftp = ftplib.FTP("ftpupload.net")
    ftp.login("epiz_24763533", "Hyg63aDtH4tjNy")
    ftp.cwd("/htdocs/")
    ftp.delete(file)
    ftp.quit()
    
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
 open   (name)               open a pre existing database from server
 new    (name)               create new database
 add    (id,data,...)        add record using input CSVs
 show                        show database
 remove (id)                 delete record with specified id")
 ren    (name)               rename the database
 edit   (id,index,new_value) modify value of specified index (0-n)
                             in the row with specified id to given
                             new value.
 delete (name)               Delete a pre existing database from server
                             or from local path (loc is path)
 save                        uploads current database
 
 
 TIP: you can simply put the command and params in the same line.
 for example, typing 'add abc,100' will add 'abc' , '100' to a
 new row in the database. Or, you can input the command and params
 separately as well.

 TIP: for online databases, changes are registered only locally until
 you save the database using the 'save' command.
 
'''
print(intro)
print(hlp)
print("Starting New Session \n")
while True:
    inp = str(input("command (h for help)> "))
    if "open" in inp:
        if inp != "open":
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
        num = [0]
        for i in range(0,len(b)):
            if b[i] == ",":
                num.append(i)
        num.append(len(b))
        nl = []
        for j in range(0, len(num)-1):
            itm = (b[num[j]:num[j + 1]]).lstrip(",")
            nl.append(itm)
        dbase.append(nl)
        print("added entry ",nl," to database")
    elif inp == "show":
        print(" " , dbnom + "\n", ("=" * (len(dbnom)+2)))
        cols = 0
        for l in dbase:
            for j in l:
                print(j, end="\t")
            print("\n")
    elif inp == "save":
        print("saving database...")
        file1 = open(dbnom + ".txt","w")
        txt = ""
        for i in dbase:
            for j in i:
                txt += j + ","
            txt = txt.rstrip(",")
            txt += "\n"                
        file1.writelines(txt)
        file1.close()
        upload(dbnom + ".txt")
    elif "remove" in inp:
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
            delete(dbnom + ".txt")
    elif inp == "h":
        print(hlp)

        
        
                    
                
        

        
