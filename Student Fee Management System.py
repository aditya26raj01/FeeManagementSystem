import mysql.connector as mod

con=mod.connect(host="localhost",user="root",passwd="2601",database="cs_project")

cur=con.cursor()

print("----------------- ●● Welcome to the Student's Fee Management System ●● -----------------\n")

#function_1

def add_stud():
    name=input("Enter Name of Student: ")
    id=int(input("Enter ID of Student: "))
    clas=int(input("Enter Class of Student: "))
    cur.execute(f"insert into stud_detail values({id},'{name}',{clas})")
    cur.execute(f"insert into fee_detail values({id},NULL,NULL)")
    con.commit()
    print("\nRecord Successfully Registered!\n")

#function_2

def view_stud():
    cur.execute("select * from stud_detail")
    data=cur.fetchall()
    count=0
    if len(data)!=0:
        for i in data:
            count+=1
            print(f"Record {count}---> Stud_ID :",i[0],"\n Stud_Name :",i[1],"\n Stud_Class :",i[2],"\n")
    else:
        print("No Details Available at the Moment!\n")

#function_3

def fee_depo():
    id=int(input("Enter ID of Student: "))
    cur.execute("select * from fee_detail")
    data=cur.fetchall()
    found=False
    for i in data:
        if i[0]==id:
            print("Record Found!")
            month=input("Enter Month of the Fee: ")
            fee=int(input("Enter Fee Amount: "))
            cur.execute(f"update fee_detail set Fee_Depo={fee}, Month='{month}' where Stud_ID={id}")
            con.commit()
            print("\nRecord Successfully Updated!\n")
            found=True
            break
    if not found:
        print("Record with Entered Details Does not Exist!\n")

#function_4

def del_stud():
    id=int(input("Enter Student ID: "))
    cur.execute("select * from stud_detail")
    data=cur.fetchall()
    found=False
    for i in data:
        if i[0]==id:
            cur.execute(f"delete from stud_detail where Stud_ID={id}")
            cur.execute(f"delete from fee_detail where Stud_ID={id}")
            con.commit()
            print("\nRecord Successfully Deleted!\n")
            found=True
            break
    if not found:
        print("Record with Entered Details Does not Exist!\n")

#function_5

def view_stud_dtl():
    id=int(input("Enter Student ID: "))
    found=False
    cur.execute(f"select S.Stud_ID,S.Name,S.Class,F.Fee_Depo,F.Month from stud_detail as S, fee_detail as F where S.Stud_ID={id} and F.Stud_ID={id}")
    data=cur.fetchall()
    found=False
    for i in data:
        print("Stud_ID :",i[0],"\nName :",i[1],"\nClass :",i[2],"\nFee_Depo :",i[3],"\nMonth :",i[4],"\n")
        found=True
    if not found:
        print("Record with Entered Details Does not Exist!\n")

#function_6

def all_fee():
    cur.execute("select * from fee_detail")
    data=cur.fetchall()
    count=0
    if len(data)!=0:
        for i in data:
            count+=1
            print(f"Record {count}---> Stud_ID :",i[0],"\nFee Amount :",i[1],"\n Month :",i[2],"\n")
    else:
        print("No Details Available at the Moment!\n")

#function_7

def upd_stud():
    id=int(input("Enter Student ID: "))
    cur.execute("select * from stud_detail")
    data=cur.fetchall()
    found=False
    for i in data:
        if i[0]==id:
            ch=input("Enter Field Name to update: ")
            if ch.lower() in ["id","name","class"]:
                if ch.lower()=="id":
                    new_id=int(input("Enter New ID: "))
                    cur.execute(f"update stud_detail set Stud_ID={new_id} where Stud_ID={id}")
                    cur.execute(f"update fee_detail set Stud_ID={new_id} where Stud_ID={id}")
                    con.commit()
                    print("\nRecord Updated!\n")
                elif ch.lower()=="name":
                    new_name=input("Enter New Name: ")
                    cur.execute(f"update stud_detail set Name='{new_name}' where Stud_ID={id}")
                    con.commit()
                    print("\nRecord Updated!\n")
                elif ch.lower()=="class":
                    new_class=int(input("Enter New Class: "))
                    cur.execute(f"update stud_detail set Class={new_class} where Stud_ID={id}")
                    con.commit()
                    print("\nRecord Updated!\n")
            else:
                print("Invalid Field Name!\n")
            found=True
            break
    if not found:
        print("Record with Entered Details Does not Exist!\n")


# _main____

while True:
    choice=int(input("●●●●●●●●●●●●●●●● : MENU :●●●●●●●●●●●●●●●●\n\nEnter 1 for Adding NEW Students\nEnter 2 For Viewing ALL Students\nEnter 3 to Deposit Fee\nEnter 4 to Delete Student\nEnter 5 to View a Student Detail\nEnter 6 to view All Fee Details\nEnter 7 to Update Records\nEnter 0 to Exit\n\nEnter your choice: "))
    if choice==1:
        n=int(input("How many Records You want to enter?: "))
        for i in range(n):
            add_stud()
    elif choice==2:
        view_stud()
    elif choice==3:
        fee_depo()
    elif choice==4:
        del_stud()
    elif choice==5:
        view_stud_dtl()
    elif choice==6:
        all_fee()
    elif choice==7:
        upd_stud()
    elif choice==0:
        break
    else:
        print("\nInvalid Choice!")
con.close()