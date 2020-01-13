# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 17:05:29 2019

@author: Mahfuz
"""

import os
import winsound
#import tkMessageBox
import pyttsx3
import pymysql
from tkinter import *
import speech_recognition as sr

db = pymysql.connect(user="root",password="", host="localhost",database="m")
# prepare a cursor object using cursor() method
cursor = db.cursor()

engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id )
#engine.sroot()
winsound.MessageBeep()
engine.say("welcome to voice command app")
engine.runAndWait()

root = Tk()
#to = Tk()
root.title('Voice Command Application')
root.geometry('350x300+700+10')
#root.title('Output')
#global c

c=''
print("opened")

def wikit():
    import wikipedia
    command =E2.get()
        
    
    c=wikipedia.summary(command, sentences=1)
    ro=Tk()
    ro.title('From Wikipedia')
    ro.geometry('350x300+700+10')
    L3 = Label(ro, text=wikipedia.summary(command))
    L3.pack( side = TOP)
    L3 = Label(ro, text="By Mashkur")
    L3.pack( side = BOTTOM)
    ro.mainloop
    
    print(wikipedia.summary(command))
       
    #winsound.MessageBeep()
    engine.say(c)
    engine.runAndWait()
    engine.stop()


def wikiv():
    import wikipedia
    
    engine = pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id )
    
    
    #my_input = input("Question: ")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        engine.say('Ask something...')
        engine.runAndWait()
        print('Ask something...')
       # r.pause_threshold = 1
        #r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
        engine.say('You said: ')
        engine.say(command)
    
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
    
    
    c=wikipedia.summary(command, sentences=1)
    ro=Tk()
    ro.title('From Wikipedia')
    ro.geometry('350x300+700+10')
    L3 = Label(ro, text=wikipedia.summary(command))
    L3.pack( side = TOP)
    L3 = Label(ro, text="By Mashkur")
    L3.pack( side = BOTTOM)
    ro.mainloop
    
    print(wikipedia.summary(command))
       
    #winsound.MessageBeep()
    engine.say(c)
    engine.runAndWait()
    engine.stop()

def OpenTask():
    global c
#    c=E1.get()    
    #L5 = Label(root, text="Opening")
    #L5.pack( side = TOP)


        
    '''L7 = Label(root, text=c)
    L7.pack( side = TOP)
    #print(c)
    #print('Opening')
    #if c=="hello" :
        #print("ok")
    '''
       # Prepare SQL query to INSERT a record into the database.
        
    try:
        # Execute the SQL command
        cursor.execute('SELECT * FROM t \
        WHERE c="%s"'% \
        (c))
    # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:            
            Task = row[1]
            name=row[2]
        
        #engine.say(c)    
        #engine.setProperty('rate',120)
        #engine.setProperty('volume', 0.8)
        #engine.runAndWait()
        os.startfile(Task)
        
        engine.say("opening")
        engine.runAndWait()
        
        engine.say(name)
        engine.runAndWait()

        roo=Tk()
        roo.title('Confirmation Window')
        roo.geometry('350x300+700+10')
        L3 = Label(roo, text="Opened")
        L3.pack( side = TOP)
        L4= Label(roo, text=name)
        L4.pack( side = TOP)
        
        engine.say('opened')
        engine.say(name)
        engine.runAndWait()
                
        winsound.MessageBeep()        
    # Now print fetched result
        #print (l)
    except:
        print ("Error: no data")
        roo=Tk()
        roo.title('Error Window')
        roo.geometry('350x300+700+10')
        L3 = Label(roo, text="Error: no data for")
        L3.pack( side = TOP)
        L4= Label(roo, text=c)
        L4.pack( side = TOP)

        engine.say("Error: no data")
        engine.runAndWait()        
      
def voice():
    global c
    #L9 = Label(root, text="speak")
    #L9.pack( side = TOP)
    '''
    to = Tk()
    L9 = Label(to, text="speak")
    L9.pack( side = TOP)
    '''
    recording = sr.Recognizer()
    with sr.Microphone() as source:         
        recording.adjust_for_ambient_noise(source)
        #engine = pyttsx3.init()
        
        engine.say("How may i help u")
        engine.say("speak now")
        
        #engine.setProperty('rate',120)
        #engine.setProperty('volume', 0.8)
        engine.runAndWait()
        print("Speak now")
        #global c
        audio = recording.listen(source)
        #print("said")
    try:
        global c
        c=recording.recognize_google(audio)
        print("You said: \n" + c)        
        #print(c)        
        engine.say("You said")
        engine.say(c)
        engine.runAndWait()
        OpenTask()
        
    except Exception as n:
            print(n)
            engine.say(n)
            engine.runAndWait()            
            #L8 = Label(root, text=e)
            #L8.pack( side = TOP)    
    #to.mainloop()    
    reopen()
    
def reopen():
    recording = sr.Recognizer()
    with sr.Microphone() as source:         
        recording.adjust_for_ambient_noise(source)
        #engine = pyttsx3.init()
        engine.say("Want to continue")
        #engine.setProperty('rate',120)
        #engine.setProperty('volume', 0.8)
        engine.runAndWait()
        print("Speak now")
        #global c
        audio = recording.listen(source)
        #print("said")
    try:
        global c
        c=recording.recognize_google(audio)
        print("You said: \n" + c)        
        #print(c)        
        engine.say("You said")
        engine.say(c)
        engine.runAndWait()

        if(c=='yes'):                        
            voice()

        else:
            #print("You said: \n" + c)        
            #print(c)        
            engine.say("Bye")
            #engine.say(c)
            engine.runAndWait()
            
    except Exception as n:
            print(n)
            engine.say(n)
            engine.runAndWait()            
            #L8 = Label(root, text=e)
            #L8.pack( side = TOP)    
    #to.mainloop()        

def voicef():
    global c
    #L9 = Label(root, text="speak")
    #L9.pack( side = TOP)
    '''
    to = Tk()
    L9 = Label(to, text="speak")
    L9.pack( side = TOP)
    '''
    recording = sr.Recognizer()
    with sr.Microphone() as source:         
        recording.adjust_for_ambient_noise(source)        
        #engine = pyttsx3.init()
        engine.say("speak now")
        #engine.setProperty('rate',120)
        #engine.setProperty('volume', 0.8)
        engine.runAndWait()
        print("Speak now")
        #global c        
        audio = recording.listen(source)
        #print("said")

    try:
        global c
        c=recording.recognize_sphinx(audio)
        print("You said: \n" + c)        
        #print(c)        
        engine.say("You said")
        engine.say(c)
        engine.runAndWait()
        OpenTask()
        
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
        L8 = Label(root, text="Sphinx could not understand audio")
        L8.pack( side = TOP)
    
    except sr.RequestError as n:
        print("Sphinx error; {0}".format(n))
        L8 = Label(root, text=n)
        L8.pack( side = TOP)            #L8 = Label(root, text=e)
            #L8.pack( side = TOP)    
    #to.mainloop()
      
def task():
    global c
    c=E1.get()
    OpenTask()    
    print(c)

def ADMINV():
          
    def add():
        p=E2.get()
        n=E4.get()
        global b
          
        try:
        # Execute the SQL command
            cursor.execute("INSERT INTO t(c, \
        t,n) \
        VALUES ('%s', '%s', '%s')" % \
        (b,p,n))
        # Commit your changes in the database
            db.commit()
            roo=Tk()
            roo.title('Confirmation Window')
            roo.geometry('350x300+700+10')
            
            L4 = Label(roo, text="Added command")
            L4.pack( side = TOP)
            
            L4 = Label(roo, text=b)
            L4.pack( side = TOP)
            
            L4 = Label(roo, text='For the task')
            L4.pack( side = TOP)
            
            L4 = Label(roo, text=n)
            L4.pack( side = TOP)
            
            engine.say("Added command")
            engine.say(b)
            engine.say("for For the task")
            engine.say(n)
            
            engine.runAndWait()        
            
        except:
        # Rollback in case there is any error
            db.rollback() 
        #print('Added')
            engine.say("failed to Add for duplicate command")
            engine.say(b)
            
            engine.runAndWait()        
            
            roo.title('Error Window')
            L4 = Label(roo, text="Failed to Add for duplicate command")
            L4.pack( side = TOP)
        #root.mainloop()
    
    #global c
    def ad():
        #!/usr/bin/python
        # Open a file
        global b
        b=E3.get()
        add()
        
    def addv():
        #!/usr/bin/python
        # Open a file
        global c
        recording = sr.Recognizer()
        with sr.Microphone() as source:         
            recording.adjust_for_ambient_noise(source)
            print("Please Say something:")
            #global c
            audio = recording.listen(source)
        try:
            global c        
            b=recording.recognize_google(audio)
            print("You said: \n" + b)        
            print(b)        
        except Exception as n:
                print(n)
                engine.say(n)
                engine.runAndWait()            
    
        add()
            
    roo=Tk()
    roo.title('Add Voice Command')
    
    roo.geometry('350x300+700+10')
    L2 = Label(roo, text="ADMIN PANEL")
    L2.pack( side = TOP)
    L4 = Label(roo, text="")
    L4.pack( side = TOP)


    
    L3 = Label(roo, text="Path(as c:/folder/file.extension)")
    L3.pack( side = TOP)
    
    E2 = Entry(roo, bd =5)
    E2.pack()
        
    L3 = Label(roo, text="Name")
    L3.pack( side = TOP)
    
    E4 = Entry(roo, bd =5)
    E4.pack()
    B2 = Button(roo, text ="Add Voice Command", command = addv)
    B2.pack(side = TOP) 
    L3 = Label(roo, text="By Mashkur")
    L3.pack( side = BOTTOM)
    roo.mainloop

def ADMINT():
          
    def add():
        p=E2.get()
        n=E4.get()
        global b
          
        try:
        # Execute the SQL command
            cursor.execute("INSERT INTO t(c, \
        t,n) \
        VALUES ('%s', '%s', '%s')" % \
        (b,p,n))
        # Commit your changes in the database
            db.commit()
            roo=Tk()
            
            L4 = Label(roo, text="Added")
            L4.pack( side = TOP)
            
            L4 = Label(roo, text='Command')
            L4.pack( side = TOP)
            
            L4 = Label(roo, text=b)
            L4.pack( side = TOP)
            
            L4 = Label(roo, text='Task')
            L4.pack( side = TOP)
            
            L4 = Label(roo, text=p)
            L4.pack( side = TOP)
            
            engine.say("Added")
            engine.runAndWait()        
            
        except:
        # Rollback in case there is any error
            db.rollback() 
        #print('Added')
            engine.say("failed to Add")
            engine.runAndWait()        
            
            L4 = Label(roo, text="Failed to Add")
            L4.pack( side = TOP)
        #root.mainloop()
    
    #global c
    def ad():
        #!/usr/bin/python
        # Open a file
        global b
        b=E3.get()
        add()
                    
    roo=Tk()
    roo.title('Add Text Command')
    
    roo.geometry('350x300+700+10')
    L2 = Label(roo, text="ADMIN PANEL")
    L2.pack( side = TOP)
    L4 = Label(roo, text="")
    L4.pack( side = TOP)
    L1 = Label(roo, text="Text Command")
    L1.pack( side = TOP)
    
    E3 = Entry(roo, bd =5)
    E3.pack()
    
    L3 = Label(roo, text="Path(as c:/folder/file.extension)")
    L3.pack( side = TOP)
    
    E2 = Entry(roo, bd =5)
    E2.pack()
        
    L3 = Label(roo, text="Name")
    L3.pack( side = TOP)
    
    E4 = Entry(roo, bd =5)
    E4.pack()

    B3 = Button(roo, text ="Add", command = ad)
    B3.pack(side = TOP)

    L3 = Label(roo, text="By Mashkur")
    L3.pack( side = BOTTOM)
    roo.mainloop

'''    
def donothing():
    print("m")
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()
'''
def Help():
    ro=Tk()
    ro.geometry('350x300+700+10')
    ro.title('Help')
    L3 = Label(ro, text="Help \n offline one works offline\n online one works online")
    L3.pack( side = TOP)
    L3 = Label(ro, text="By Mashkur")
    L3.pack( side = BOTTOM)
    ro.mainloop

def About():
    ro=Tk()
    ro.title('About')
    ro.geometry('350x300+700+10')
    L3 = Label(ro, text="This is a voice command Application")
    L3.pack( side = TOP)
    L3 = Label(ro, text="By Mashkur")
    L3.pack( side = BOTTOM)
    ro.mainloop

#print('Text Command')
#os.startfile('A:/Cse 499/m.m4a')
#L2 = Label(root, text="Voice Command Window")
#L2.pack( side = TOP)
L2 = Label(root, text="USER PANEL")
L2.pack( side = TOP)
L2 = Label(root, text="Text Command")
L2.pack( side = TOP)

E1 = Entry(root, bd =5)
E1.pack()
    
B = Button(root, text ="RUN", command = task)
B.pack(side = TOP)

L2 = Label(root, text="")
L2.pack( side = TOP)

L2 = Label(root, text="Voice Command")
L2.pack( side = TOP)

B4 = Button(root, text ="Command", command =voicef)
B4.pack(side = TOP)

B4 = Button(root, text ="Command(online)", command = voice)
B4.pack(side = TOP)

L2 = Label(root, text="")
L2.pack( side = TOP)

E2 = Entry(root, bd =5)
E2.pack()
    
B4 = Button(root, text ="Search(online)", command = wikit)
B4.pack(side = TOP)

B4 = Button(root, text ="Ask(online)", command = wikiv)
B4.pack(side = TOP)

L4 = Label(root, text="")
L4.pack( side = TOP)


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Add Voice Command", command=ADMINV)
filemenu.add_command(label="Add Text Command", command=ADMINT)
        
'''filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
'''
menubar.add_cascade(label="Add Command", menu=filemenu)
'''
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
'''
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=Help)
helpmenu.add_command(label="About...", command=About)

menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
    
L3 = Label(root, text="By Mashkur")
L3.pack( side = BOTTOM)


root.mainloop()
#tp.mainloop()

winsound.MessageBeep()
engine.say("thank u for using voice command Application")
engine.runAndWait()
engine.stop()
# disconnect from server
db.close()
print('closed')
