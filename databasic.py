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
 add    (id,data,...)        add record using input CSVs
 show                        show database
 delete (id)                 delete record with specified id")
 ren    (name)               rename the database
 edit   (id,index,new_value) modify value of specified index (0-n)
                             in the row with specified id to given
                             new value.
 
 TIP: you can simply put the command and params in the same line.
 for example, typing 'add abc,100' will add 'abc' , '100' to a
 new row in the database. Or, you can input the command and params
 separately as well.
 
'''
lst = []
print(intro)
print(hlp)
print("Starting New Session \n")
dname = str(input("enter name of database> "))
while True:
    inp = str(input("command (h for help)> "))
    if "add" in inp:
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
        lst.append(nl)
        print("ADDED",nl,"TO RECORD")
    elif inp == "show":
        print(" ",dname,"\n", ("=" * (len(dname)+2)))
        cols = 0
        for l in lst:
            for j in l:
                print(j, end="\t")
            print("\n")
    elif "delete" in inp:
        if inp == "delete":
            inc = str(input("enter record id> "))
        else:
            inc = inp[7:len(inp)]
        flg = 0
        for l in lst:
            if inc in l[0]:
                flg = 1
                lst.remove(l)
        if flg == 0:
            print("Entry with given id not found")
        else:
            print("Entry/entries successfully removed")
            
    elif inp == "h":
        print(hlp)
    elif inp == "export":        
        file1 = open("C:/Users/adity/Desktop/" + dname + ".txt","w")
        txt =""
        for l in lst:
            for j in l:
                txt += j + "\t"
            txt += "\n"
        file1.writelines(txt)
        file1.close()
        
        
                    
                
        

        
