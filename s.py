from tkinter import *
import pymysql
db = pymysql.connect(user="root",password="", host="localhost",database="m")
#00905366172210\l "prepare a cursor object using cursor() method
cursor = db.cursor()
   # Prepare SQL query to INSERT a record into the database.
print('m')
#n=p=0

        
def Newu():
    r=Tk()
    r.geometry('450x300+700+10')
    ro.title('User')

    r.mainloop


    L3 = Label(r, text="Name")
    L3.pack( side = TOP)
    
    E3 = Entry(r, bd =5)
    E3.pack()

    L3 = Label(r, text="Password")
    L3.pack( side = TOP)
    
    E4 = Entry(r, bd =5)
    E4.pack()

    L3 = Label(r, text="Answer")
    L3.pack( side = TOP)
    
    E4 = Entry(r, bd =5)
    E4.pack()

    def Addu():
        n=E3.get()
        p=E4.get()
        
        try:
        # Execute the SQL command
            cursor.execute("INSERT INTO u(n, \
        p) \
        VALUES ('%s', '%s')" % \
        (n,p))
        # Commit your changes in the database
            db.commit()
        except:
        # Rollback in case there is any error
            db.rollback()
            L3 = Label(r, text="e")
            L3.pack( side = TOP)
        #print('Added')
          
    B4 = Button(r, text ="Add", command = Addu)
    B4.pack(side = TOP)


def Users():
    ro=Tk()
    ro.geometry('450x300+700+10')
    ro.title('Patient Medicine Collection System')

    '''

    L3 = Label(ro, text='Username')
    L3.pack( side = LEFT)

    L3 = Label(ro, text='Password')
    L3.pack( side = RIGHT)
    '''
    t="Username:    Password:"
    L3 = Label(ro, text=t)
    L3.pack( side = TOP)
    
    try:
        # Execute the SQL command
        cursor.execute('SELECT * FROM u ')
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            na = row[0]
            pw = row[1]
            t=na+"           "+pw
            L3 = Label(ro, text=t)
            L3.pack( side = TOP)
            
            L3 = Label(ro, text='')
            L3.pack( side = TOP)
            

    except:
    # Rollback in case there is any error
        db.rollback() 

    

    B4 = Button(ro, text ="Edit", command = Users)
    B4.pack(side = TOP)
    L3 = Label(ro, text='')
    L3.pack( side = TOP)
            
    B5 = Button(ro, text ="New", command = Newu)
    B5.pack(side = TOP)
    L3 = Label(ro, text='')
    L3.pack( side = TOP)
    B6 = Button(ro, text ="Delete", command = Users)
    B6.pack(side = TOP)
    
    #ro.title('Users Management')
    ro.mainloop


    L3 = Label(ro, text="")
    L3.pack( side = TOP)
#Users()


def login():
    ro=Tk()
    ro.geometry('450x300+700+10')


    
    
    ro.title('Patient Medicine Collection System')
    ro.mainloop


    L3 = Label(ro, text="")
    L3.pack( side = TOP)


    B4 = Button(ro, text ="Patients", command = Patients)
    B4.pack(side = TOP)

    L3 = Label(ro, text="")
    L3.pack( side = TOP)

    B4 = Button(ro, text ="Prescriptions", command = Prescriptions)
    B4.pack(side = TOP)


    L3 = Label(ro, text="")
    L3.pack( side = TOP)
    B4 = Button(ro, text ="Users", command = Users)
    B4.pack(side = TOP)



    L3 = Label(ro, text="")
    L3.pack( side = TOP)

    B4 = Button(ro, text ="Reports", command = Reports)
    B4.pack(side = TOP)


    L3 = Label(ro, text="")
    L3.pack( side = TOP)
    

def Addp():
    ro=Tk()
    #ro.geometry('450x300+700+10')
    
    ro.title('Patient Management')
    L3 = Label(ro, text="Name")
    L3.pack( side = TOP)
    E5 = Entry(ro, bd =5)
    E5.pack()
    L3 = Label(ro, text="Birthday")
    L3.pack( side = TOP)
    E3 = Entry(ro, bd =5)
    E3.pack()
    L3 = Label(ro, text="Address")
    L3.pack( side = TOP)
    E4 = Entry(ro, bd =5)
    E4.pack()
    L3 = Label(ro, text="NICNO")
    L3.pack( side = TOP)
    E6 = Entry(ro, bd =5)
    E6.pack()
    L3 = Label(ro, text="Image")
    L3.pack( side = TOP)
    E7 = Entry(ro, bd =5)
    E7.pack()
    L3 = Label(ro, text="Contact No")
    L3.pack( side = TOP)
    E8 = Entry(ro, bd =5)
    E8.pack()
    L3 = Label(ro, text="Contact Person")
    L3.pack( side = TOP)
    E9 = Entry(ro, bd =5)
    E9.pack()

    def Addp():
        n=E5.get()
        
        b=E3.get()
        
        a=E4.get()
        
        cp=E9.get()
        
        ni=E6.get()
        
        i=E7.get()
        
        cn=E8.get()
        
        try:
        # Execute the SQL command
            cursor.execute("INSERT INTO p(n, \
        b,a,i,cn,cp,ni) \
        VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
        (n,b,a,i,cn,cp,ni))
        # Commit your changes in the database
            db.commit()
            L3 = Label(ro, text="added")
            L3.pack( side = TOP)
        except:
        # Rollback in case there is any error
            db.rollback()
            L3 = Label(ro, text="error")
            L3.pack( side = TOP)
        #print('Added')
            
    B4 = Button(ro, text ="Add", command = Addp)
    B4.pack(side = TOP)


    ro.mainloop
    


def Updatep():
    ro=Tk()
    #ro.geometry('450x300+700+10')
    
    ro.title('Patient Management')
    L3 = Label(ro, text="Name")
    L3.pack( side = TOP)
    E2 = Entry(ro, bd =5)
    E2.pack()
    L3 = Label(ro, text="Birthday")
    L3.pack( side = TOP)
    E3 = Entry(ro, bd =5)
    E3.pack()
    L3 = Label(ro, text="Address")
    L3.pack( side = TOP)
    E4 = Entry(ro, bd =5)
    E4.pack()
    L3 = Label(ro, text="NICNO")
    L3.pack( side = TOP)
    E2 = Entry(ro, bd =5)
    E2.pack()
    L3 = Label(ro, text="Image")
    L3.pack( side = TOP)
    E3 = Entry(ro, bd =5)
    E3.pack()
    L3 = Label(ro, text="Contact No")
    L3.pack( side = TOP)
    E4 = Entry(ro, bd =5)
    E4.pack()
    L3 = Label(ro, text="Contact Person")
    L3.pack( side = TOP)
    E4 = Entry(ro, bd =5)
    E4.pack()
    
    B4 = Button(ro, text ="Add", command = Patients)
    B4.pack(side = TOP)


    ro.mainloop
    
def Patients():
    ro=Tk()
    ro.geometry('450x300+700+10')

    L3 = Label(ro, text="Patients list")
    L3.pack( side = TOP)
    L3 = Label(ro, text="Name| nic | contac no |photo |  action")
    L3.pack( side = TOP)
    L3 = Label(ro, text="name | 77|  787675765|      |edit| delete")
    L3.pack( side = TOP)
    L3 = Label(ro, text="name | 77|  787675765|      |edit| delete")
    L3.pack( side = TOP)
    
    #B4 = Button(ro, text ="v", command = Patients)
    #B4.pack(side = TOP)
    B4 = Button(ro, text ="edit", command = Updatep)
    B4.pack(side = TOP)
    B4 = Button(ro, text ="delete", command = Patients)
    B4.pack(side = TOP)
    ro.title('Patient Management')
    B4 = Button(ro, text ="Add", command = Addp)
    B4.pack(side = TOP)


    ro.mainloop

#Patients()


def a():
    ro=Tk()
    ro.geometry('450x300+700+10')
    
    ro.title('Users Management')
    ro.mainloop

    
def Prescriptions():
    ro=Tk()
    ro.geometry('450x300+700+10')


    
    ro.title('Priscription List')
    L3 = Label(ro, text="Select Paitent")
    L3.pack( side = TOP)

    L3 = Label(ro, text="medicine| qty| time    | before/after | action")
    L3.pack( side = TOP)

    L3 = Label(ro, text="para         | 2 | morning |after          |edite/ delete")
    L3.pack( side = TOP)

    L3 = Label(ro, text="napa       | 1 | morning|after          |edite/ delete")
    L3.pack( side = TOP)

    
    E22 = Entry(ro, bd =5)
    E22.pack()
    
    def Search():
        
        n=E22.get()
        
        try:
            # Execute the SQL command
            cursor.execute('SELECT * FROM p \
            WHERE n="%s"'% \
            (n))
            # Fetch all the rows in a list of lists.
            results = cursor.fetchall()
            for row in results:
                na = row[0]
                pw = row[1]



                if (na==n) :
                        ro=Tk()
                        ro.title('Error')
                        ro.geometry('450x300+700+10')
                        L3 = Label(ro, text=na)
                        L3.pack( side = TOP)
                        ro.mainloop

                        
                '''else:
                    ro=Tk()
                    ro.title('Error')
                    ro.geometry('450x300+700+10')
                    L3 = Label(ro, text="Forgot password")
                    L3.pack( side = TOP)

                    B4 = Button(ro, text ="Forgot password", command = Forgot)
                    B4.pack(side = TOP)    
                   ''' 
        except:
        # Rollback in case there is any error
            db.rollback() 
        
    
    B4 = Button(ro, text ="Search", command = Search)
    B4.pack(side = TOP)

    
    
    ro.mainloop

#Prescriptions()
    
def Reports():
    ro=Tk()
    ro.geometry('450x300+700+10')
    
    ro.title('Reports')


    L3 = Label(ro, text="List all paitents prescription")
    L3.pack( side = TOP)


    L3 = Label(ro, text="Paitent name: name")
    L3.pack( side = TOP)

    
    L3 = Label(ro, text="")
    L3.pack( side = TOP)
    
    ro.mainloop

#Reports()

def Recover():
    
    ro=Tk()
    ro.geometry('450x300+700+10')

    L3 = Label(ro, text="Security Question")
    L3.pack( side = TOP)
    E2 = Entry(ro, bd =5)
    E2.pack()
    L3 = Label(ro, text="New Login Credential")
    L3.pack( side = TOP)
    L3 = Label(ro, text="New Password")
    L3.pack( side = TOP)
    E3 = Entry(ro, bd =5)
    E3.pack()
    L3 = Label(ro, text="Retype Password")
    L3.pack( side = TOP)
    E4 = Entry(ro, bd =5)
    E4.pack()
    B4 = Button(ro, text ="Submit", command = main)
    B4.pack(side = TOP)


    ro.mainloop



def Forgot():
    
    ro=Tk()
    ro.geometry('450x300+700+10')

    L3 = Label(ro, text="Username")
    L3.pack( side = TOP)
    E2 = Entry(ro, bd =5)
    E2.pack()
    B4 = Button(ro, text ="Search", command = Recover)
    B4.pack(side = TOP)
    ro.mainloop

def loginc():
    global n
    global p
    n=E1.get()
    
    p=E2.get()
    
    try:
        # Execute the SQL command
        cursor.execute('SELECT * FROM u \
        WHERE n="%s"'% \
        (n))
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            na = row[0]
            pw = row[1]



            if (na==n) :
                if(pw==p):
                    
                    login()
                else :
                    ro=Tk()
                    ro.title('Error')
                    ro.geometry('450x300+700+10')
                    L3 = Label(ro, text="Forgot password")
                    L3.pack( side = TOP)

                    B4 = Button(ro, text ="Forgot password", command = Forgot)
                    B4.pack(side = TOP)
                    
            '''else:
                ro=Tk()
                ro.title('Error')
                ro.geometry('450x300+700+10')
                L3 = Label(ro, text="Forgot password")
                L3.pack( side = TOP)

                B4 = Button(ro, text ="Forgot password", command = Forgot)
                B4.pack(side = TOP)    
               ''' 
    except:
    # Rollback in case there is any error
        db.rollback()

        ro=Tk()
        ro.title('Error')
        ro.geometry('450x300+700+10')
        L3 = Label(ro, text="Forgot password")
        L3.pack( side = TOP)

        B4 = Button(ro, text ="Forgot password", command = Forgot)
        B4.pack(side = TOP)
        
    
def main():
    

    ro=Tk()
    ro.title('Patient Medicine Collection System')
    ro.geometry('450x300+700+10')
    L3 = Label(ro, text="Patient Medicine Collection System")
    L3.pack( side = TOP)


    L3 = Label(ro, text="")
    L3.pack( side = TOP)

    L3 = Label(ro, text="Username")
    L3.pack( side = TOP)
    E1 = Entry(ro, bd =5)
    E1.pack()
    L3 = Label(ro, text="Password")
    L3.pack( side = TOP)
    E2 = Entry(ro, bd =5)
    E2.pack()

    B4 = Button(ro, text ="Login", command = loginc)
    B4.pack(side = TOP)


    B4 = Button(ro, text ="Forgot password", command = Forgot)
    B4.pack(side = TOP)

    L3 = Label(ro, text="Created By \n Nethmi T Mayadunna \n Icordium Software Solutions")
    L3.pack( side = BOTTOM)
    #L3 = Label(ro, text="General Details")
    #L3.pack( side = BOTTOM)

    L3 = Label(ro, text="Address:sss,Telephone:0565656,Email:isdojao@gmail.com")
    L3.pack( side = BOTTOM)

    ro.mainloop
#main()


ro=Tk()
ro.title('Patient Medicine Collection System')
ro.geometry('450x300+700+10')
L3 = Label(ro, text="Patient Medicine Collection System")
L3.pack( side = TOP)


L3 = Label(ro, text="")
L3.pack( side = TOP)

L3 = Label(ro, text="Username")
L3.pack( side = TOP)
E1 = Entry(ro, bd =5)
E1.pack()
L3 = Label(ro, text="Password")
L3.pack( side = TOP)
E2 = Entry(ro, bd =5)
E2.pack()

B4 = Button(ro, text ="Login", command = loginc)
B4.pack(side = TOP)

L3 = Label(ro, text='')
L3.pack( side = TOP)
    
B4 = Button(ro, text ="Forgot password", command = Forgot)
B4.pack(side = TOP)

L3 = Label(ro, text="Created By \n Nethmi T Mayadunna \n Icordium Software Solutions")
L3.pack( side = BOTTOM)
#L3 = Label(ro, text="General Details")
#L3.pack( side = BOTTOM)

L3 = Label(ro, text="Address:sss,Telephone:0565656,Email:isdojao@gmail.com")
L3.pack( side = BOTTOM)

ro.mainloop

print('c')
