lst = []
dname = str(input("enter name of database> "))
while True:
    inp = str(input("command (h for help)> "))
    if inp == "add":        
        b = str(input("Enter CSVs (id,data,...)> "))
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
        print("       ",dname,"   \n ================")
        cols = 0
        for l in lst:
            for j in l:
                print(j, end="\t")
            print("\n")
    elif inp == "delete":
        inc = str(input("enter record id> "))
        for l in lst:
            if l[0] == inc:
                print("Entry removed")
                lst.remove(l)
    elif inp == "h":
        print("help \n add     add record \n show    show database \n del     delete record")
    elif inp == "export":
        file1 = open("C:/Users/student/Desktop/" + dname + ".txt","w")
        txt =""
        for l in lst:
            for j in l:
                txt += j + "\t"
            txt += "\n"
        file1.writelines(txt)
        file1.close()
        
        
                    
                
        

        
