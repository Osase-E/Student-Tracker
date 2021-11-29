import sqlite3
from tkinter import *
from tkinter import messagebox
import random
import re

#Creates the class for the registration window 
class RegistrationMainWindow:
          def __init__(self, master):
                    global studentFrame
                    global teacherFrame
                    global subjectFrame                   
                    #currentFrame will be used to let the program know what frame is initialised
                    #This will be used by the save function to append the information to the appropriate table
                    #It needs to be changed by each function, so it has been assigned as a global variable
                    global currentFrame
                    global variableOP1
                    global variableOP2
                    global variableOP3
                    global variableOP4
                    global OPTIONS
                    currentFrame=''
                    self.master = master
                    self.master.title('Registration Window')
                    self.master.geometry('710x620')
                    self.master.configure(bg='#A8D59D')
                    OPTIONS = ['']
                    #Variable specification for Drop Down Menus
                    try:
                        connection = sqlite3.connect('Main Database')
                        crsr = connection.cursor()
                        crsr.execute('SELECT Subject FROM Subjects')
                        OPTIONS = list(crsr.fetchall())
                        connection.close()
                    except:
                        pass
                    variableOP1 = StringVar(self.master)
                    variableOP1.set('Subject')
                    variableOP2 = StringVar(self.master)
                    variableOP2.set('Subject')
                    variableOP3 = StringVar(self.master)
                    variableOP3.set('Subject')
                    variableOP4 = StringVar(self.master)
                    variableOP4.set('Subject')
                    #End of variable specification
                    #Defining Widgets for the main window
                    self.photo = PhotoImage(file = 'Logo.gif')
                    self.SchoolLogo = Label(self.master, image = self.photo,bg = 'white').grid(row=0,column=0,columnspan=5,sticky=W+E)
                    Label(self.master,text=' ',bg='#A8D59D').grid(row=1,column=0)
                    Label(self.master,text=' ',bg='#A8D59D').grid(row=1,column=4)
                    mainFrame = Frame(self.master,bg='#A8D59D')
                    self.studentBtn = Button(mainFrame, text='Student', command=self.studentWindow,font=('Arial',12,'bold'))
                    self.teacherBtn = Button(mainFrame,text='Teacher', command=self.teacherWindow,font=('Arial',12,'bold'))
                    self.subjectBtn = Button(mainFrame, text='Subject', command=self.subjectWindow,font=('Arial',12,'bold'))
                    studentFrame = Frame(self.master,bg='#A8D59D')
                    teacherFrame = Frame(self.master,bg='#A8D59D')
                    subjectFrame = Frame(self.master,bg='#A8D59D')
                    #Defining the widgets for each frame                    
                    #Widgets for the subject frame
                    self.subjectL = Label(subjectFrame, text='Subject Name',bg='#A8D59D',font=('Arial',12,'bold'))
                    self.subjectE = Entry(subjectFrame,font=('Arial',12))
                    self.saveB = Button(subjectFrame, text='Save', command=self.save,bg='#B3FF00',font=('Arial',12,'bold'))
                    #Initialising the widgets to allow user interaction
                    Label(subjectFrame,bg='#A8D59D').grid(row=0,column=1,padx=20,sticky=W+E)
                    Label(subjectFrame,bg='#A8D59D').grid(row=0,column=2,padx=70)
                    self.subjectL.grid(row=1,column=1)
                    self.subjectE.grid(row=1,column=2)
                    Label(subjectFrame,bg='#A8D59D').grid(row=2,column=1,padx=70)
                    self.saveB.grid(row=3,column=3)
                    #End of subject widgets
                    
                    #Widgets for the teacher frame
                    self.TFirstL = Label(teacherFrame, text='First Name',bg='#A8D59D',font=('Arial',12,'bold'))
                    self.TFirstE = Entry(teacherFrame,font=('Arial',12))
                    self.TLastL = Label(teacherFrame, text='Last Name',bg='#A8D59D',font=('Arial',12,'bold'))
                    self.TLastE = Entry(teacherFrame,font=('Arial',12))
                    self.TGenderL = Label(teacherFrame, text='Gender\n(M/F)',bg='#A8D59D',font=('Arial',12,'bold'))
                    self.TGenderE = Entry(teacherFrame,width=5,font=('Arial',12),justify=CENTER)
                    self.DOBL = Label(teacherFrame, text = 'Date of Birth\nDD/MM/YYYY',bg='#A8D59D',font=('Arial',12,'bold'))
                    self.TDOBE = Entry(teacherFrame,font=('Arial',12))
                    self.THomeAddressL = Label(teacherFrame, text='Home Address',bg='#A8D59D',font=('Arial',12,'bold'))
                    self.THomeAddressE = Entry(teacherFrame,font=('Arial',12))
                    self.TContactNumberL = Label(teacherFrame, text='Contact Number',bg='#A8D59D',font=('Arial',12,'bold'))
                    self.TContactNumberE = Entry(teacherFrame,font=('Arial',12))
                    self.SubjectDDL = Label(teacherFrame, text = 'Subjects',bg='#A8D59D',font=('Arial',12,'bold'))
                    self.TSubjectDD1 = OptionMenu(teacherFrame, variableOP1, *OPTIONS,command=self.OP1)
                    self.TSubjectDD1.config(font=('Arial',12,'bold'))
                    self.saveB = Button(teacherFrame, text='Save', command=self.save,bg='#B3FF00',font=('Arial',12,'bold'))
                    #Initialising the widgets to allow user interaction
                    Label(teacherFrame,bg='#A8D59D').grid(row=0,column=1,padx=20,sticky=W+E)
                    Label(teacherFrame,bg='#A8D59D').grid(row=0,column=0,padx=70)
                    self.TFirstL.grid(row=2,column=0,pady=10)
                    self.TFirstE.grid(row=2,column=1,columnspan=2,sticky=W+E)
                    self.TLastL.grid(row=3,column=0,pady=10)
                    self.TLastE.grid(row=3,column=1,columnspan=2,sticky=W+E)
                    self.TGenderL.grid(row=4,column=3,pady=10,padx=(5,0))
                    self.TGenderE.grid(row=4,column=4,columnspan=1,sticky=W+E,padx=(10,0))
                    self.DOBL.grid(row=4,column=0,pady=10)
                    self.TDOBE.grid(row=4,column=1,columnspan=2,sticky=W)
                    self.THomeAddressL.grid(row=6,column=0,pady=10)
                    self.THomeAddressE.grid(row=6,column=1,columnspan=4,sticky=W+E)
                    self.TContactNumberL.grid(row=7,column=0,pady=10)
                    self.TContactNumberE.grid(row=7,column=1,columnspan=2,sticky=W+E)
                    self.SubjectDDL.grid(row=8,column=0,pady=10)
                    self.TSubjectDD1.grid(row=8,column=1,padx=(0,20),pady=10,sticky=W)
                    self.saveB.grid(row=10,column=4)
                    #End of teacher widgets

                    #Widgets for the student frame
                    self.SFirstL = Label(studentFrame, text='First Name',bg='#A8D59D',font=('Arial',12,'bold'))
                    self.SFirstE = Entry(studentFrame,font=('Arial',12))
                    self.SLastL = Label(studentFrame, text='Last Name',bg='#A8D59D',font=('Arial',12,'bold'))
                    self.SLastE = Entry(studentFrame,font=('Arial',12))
                    self.SGenderL = Label(studentFrame, text='Gender\n(M/F)',bg='#A8D59D',font=('Arial',12,'bold'))
                    self.SGenderE = Entry(studentFrame,width=5,font=('Arial',12),justify=CENTER)
                    self.DOBL = Label(studentFrame, text = 'Date of Birth\nDD/MM/YYYY',bg='#A8D59D',font=('Arial',12,'bold'))
                    self.DOBE = Entry(studentFrame,font=('Arial',12))
                    self.SHomeAddressL = Label(studentFrame, text='Home Address',bg='#A8D59D',font=('Arial',12,'bold'))
                    self.SHomeAddressE = Entry(studentFrame,font=('Arial',12))
                    self.SContactNumberL = Label(studentFrame, text='Contact Number',bg='#A8D59D',font=('Arial',12,'bold'))
                    self.SContactNumberE = Entry(studentFrame,font=('Arial',12))
                    self.SubjectDDL = Label(studentFrame, text = 'Subjects',bg='#A8D59D',font=('Arial',12,'bold'))
                    self.SubjectDD1 = OptionMenu(studentFrame, variableOP1, *OPTIONS,command=self.OP1)
                    self.SubjectDD1.config(font=('Arial',12,'bold'))
                    self.SubjectDD2 = OptionMenu(studentFrame, variableOP2, *OPTIONS,command=self.OP2)
                    self.SubjectDD2.config(font=('Arial',12,'bold'))
                    self.SubjectDD3 = OptionMenu(studentFrame, variableOP3, *OPTIONS,command=self.OP3)
                    self.SubjectDD3.config(font=('Arial',12,'bold'))
                    self.SubjectDD4 = OptionMenu(studentFrame, variableOP4, *OPTIONS,command=self.OP4)
                    self.SubjectDD4.config(font=('Arial',12,'bold'))
                    self.saveB = Button(studentFrame, text='Save', command=self.save,bg='#B3FF00',font=('Arial',12,'bold'))
                    #Initialising the widgets to allow user interaction
                    Label(studentFrame,bg='#A8D59D').grid(row=0,column=1,padx=20,sticky=W+E)
                    Label(studentFrame,bg='#A8D59D').grid(row=0,column=0,padx=70)
                    self.SFirstL.grid(row=2,column=0,pady=10)
                    self.SFirstE.grid(row=2,column=1,columnspan=2,sticky=W+E)
                    self.SLastL.grid(row=3,column=0,pady=10)
                    self.SLastE.grid(row=3,column=1,columnspan=2,sticky=W+E)
                    self.SGenderL.grid(row=4,column=3,pady=10,padx=(5,0))
                    self.SGenderE.grid(row=4,column=4,columnspan=1,sticky=W+E,padx=(10,0))
                    self.DOBL.grid(row=4,column=0,pady=10)
                    self.DOBE.grid(row=4,column=1,columnspan=2,sticky=W)
                    self.SHomeAddressL.grid(row=6,column=0,pady=10)
                    self.SHomeAddressE.grid(row=6,column=1,columnspan=4,sticky=W+E)
                    self.SContactNumberL.grid(row=7,column=0,pady=10)
                    self.SContactNumberE.grid(row=7,column=1,columnspan=2,sticky=W+E)
                    self.SubjectDDL.grid(row=8,column=0,pady=10)
                    self.SubjectDD1.grid(row=8,column=1,padx=(0,20),pady=10,sticky=W)
                    self.SubjectDD2.grid(row=8,column=2,sticky=W)
                    self.SubjectDD3.grid(row=9,column=1,pady=10,sticky=W)
                    self.SubjectDD4.grid(row=9,column=2,sticky=W)
                    self.saveB.grid(row=10,column=4)
                    #End of student widgets
                    
                    #Initialising Widgets the windows to allow user interaction
                    mainFrame.grid()
                    self.studentBtn.grid(row=1,column=1,padx=80)
                    self.teacherBtn.grid(row=1,column=2,padx=80)
                    self.subjectBtn.grid(row=1,column=3,padx=80)
          def OP1(self,value):
              global OP1
              OP1 = value[0][::]
          def OP2(self,value):
              global OP2
              OP2 = value[0][::]
          def OP3(self,value):
              global OP3
              OP3 = value[0][::]
          def OP4(self,value):
              global OP4
              OP4 = value[0][::]

          def studentWindow(self):
                    global studentFrame
                    global teacherFrame
                    global subjectFrame
                    global currentFrame
                    currentFrame ='Student'
                    #This tries to clear the contents of the window to allow the 
                    #student frame to be clearly visible 
                    try:
                              teacherFrame.grid_forget()
                              subjectFrame.grid_forget()
                    except:
                              pass
                    #Opens the connection to the main database
                    connection= sqlite3.connect('Main Database')
                    crsr = connection.cursor()
                    #Creates a table for the student data if no table is found on the system
                    crsr.execute("""CREATE TABLE IF NOT EXISTS Student_Table(SID INTEGER PRIMARY KEY,
                    SFirst_Name VARCHAR(25) NOT NULL,
                    SLast_Name VARCHAR (25) NOT NULL,
                    Gender CHAR(1) NOT NULL CHECK (length(Gender) < 2),
                    Date_of_Birth Date NOT NULL,
                    Home_Address VARCHAR (50) NOT NULL,
                    Contact_Number VARCHAR (14) NOT NULL,
                    Block_A VARCHAR(20) NOT NULL,
                    Block_B VARCHAR(20) NOT NULL,
                    Block_C VARCHAR(20) NOT NULL,
                    Block_D VARCHAR(20) NOT NULL);""")
                    connection.commit()
                    connection.close()
                    studentFrame.grid()
                    
          def teacherWindow(self):
                    global studentFrame
                    global teacherFrame
                    global subjectFrame
                    global currentFrame
                    currentFrame ='Teacher'
                    #This tries to clear the contents of the window to allow the 
                    #teacher frame to be clearly visible 
                    try:
                              studentFrame.grid_forget()
                              subjectFrame.grid_forget()
                    except:
                              pass
                    #Opens the connection to the main database
                    connection= sqlite3.connect('Main Database')
                    crsr = connection.cursor()
                    #Creates a table for the teacher data if no table is found on the system
                    crsr.execute("""CREATE TABLE IF NOT EXISTS Teacher_Table(Teacher_ID INTEGER PRIMARY KEY,
                    TFirst_Name VARCHAR(25) NOT NULL,
                    TLast_Name VARCHAR (25) NOT NULL,
                    DOB DATE NOT NULL,
                    Gender CHAR(1) NOT NULL CHECK (length(Gender) < 2),
                    Home_Address VARCHAR (50) NOT NULL,
                    Contact_Number VARCHAR (14) NOT NULL,
                    Subject VARCHAR (20) NOT NULL,
                    Code CHAR(4) NOT NULL);""")
                    connection.commit()
                    connection.close()
                    teacherFrame.grid()
                    
          def subjectWindow(self):
                    global studentFrame
                    global teacherFrame
                    global subjectFrame
                    global currentFrame
                    currentFrame ='Subject'
                    try:
                              studentFrame.grid_forget()
                              teacherFrame.grid_forget()
                    except:
                              pass
                    #Opens the connection to the main database
                    connection= sqlite3.connect('Main Database')
                    crsr = connection.cursor()
                    #Creates a table for the subject data if no table is found on the system
                    crsr.execute("""CREATE TABLE IF NOT EXISTS Subjects(Subject_Code INTEGER PRIMARY KEY,
                    Subject VARCHAR(20));""")
                    connection.commit()
                    connection.close()
                    subjectFrame.grid()
    
          def save(self):
                global currentFrame
                global OP1
                global OP2
                global OP3
                global OP4
                global OPTIONS
                try:            
                    connection = sqlite3.connect('Main Database')
                    crsr = connection.cursor()
                    
                    if currentFrame == 'Subject':
                        add = str(self.subjectE.get())
                        #Checks if the string entered is empty, and returns an error if it is
                        if (len(add)<1):
                            messagebox.showerror('Error','Please type a Subject Name')
                        elif (re.search("[$#@.!£%^&*()=+]",add) or re.search("[0-9]", add) or re.search("-", add)):
                            messagebox.showerror('Error', 'Subjects may only contain letters')
                        else:
                            crsr.execute("""INSERT INTO Subjects(Subject) VALUES(?)""",(add,))
                            connection.commit()
                            messagebox.showinfo('Success','Subject has been successfully added to the list')
                    elif currentFrame == 'Teacher':
                        TFirst = str(self.TFirstE.get())
                        TLast = str(self.TLastE.get())
                        TGender = str(self.TGenderE.get())
                        THomeAddress = str(self.THomeAddressE.get())
                        TContactNumber = str(self.TContactNumberE.get())
                        TDOB = self.TDOBE.get()
                        TSub = OP1
                        crsr.execute('''SELECT Code FROM Teacher_Table''')
                        codes= crsr.fetchall()
                        while True:
                            #Creates a unique random 4 digit number that will serve as an access code for teachers 
                            Rcode = random.randint(0,9999)
                            Rcode= '{:d}'.format(Rcode).zfill(4)
                            if Rcode not in codes:
                                break
                        if (len(TFirst) < 1) or (len(TLast) < 1) or (len(THomeAddress) < 1) or (
                        len(TContactNumber) < 1):
                            messagebox.showerror('Error', 'Please Fill in all the fields')
                        elif (re.search("[$#@.!£]", TDOB) or re.search("[$#@.!£]", TDOB) or re.search("[A-Z]", TDOB)
                                or re.search("[a-z]", TDOB)):
                            messagebox.showerror('Error', 'Dates should not contain special characters or letters')
                        elif (re.search("[$#@.!£]", TFirst) or re.search("[$#@.!£]", TLast) or re.search("[0-9]",TFirst)
                        or re.search("[0-9]", TLast)):
                            messagebox.showerror('Error', 'Names should not contain special characters or numbers')
                        #Checks the Date entered to make sure they are old enough to be teachers
                        elif (TDOB=='')or(len(TDOB)!=10)or(int(TDOB[0:2])>31) or (int(TDOB[0:2])<1) or (int(TDOB[3:5])>12) or (int(TDOB[3:5])<1) or (int(TDOB[6:10])>2000) or (int(TDOB[6:10])<1900):
                            messagebox.showerror('Error','Enter a valid date')
                        #Ensures the only values for Gender are 'M' or 'F'
                        elif (TGender != 'M') and (TGender!='F'):
                            messagebox.showerror('Error','The Gender field should only contain \'M\' or \'F\'')
                        #Ensures the other fields are not empty
                        elif(re.search("[$#@.!£]", TDOB) or re.search("[$#@.!£]", TDOB) or re.search("[A-Z]", TDOB)
                        or re.search("[a-z]", TDOB)or (re.search("\s", TDOB))):
                            messagebox.showerror('Error','Dates should not contain special characters or letters')
                        #Ensures the contact number is only numbers
                        elif (re.search("[a-z]", TContactNumber)) or (re.search("[A-Z]", TContactNumber))or \
                                (re.search("[$#@.!£]", TContactNumber)) or (re.search("\s", TContactNumber)):
                            messagebox.showwarning('Wait!','Phone numbers should only be integer numbers')
                        else:
                            crsr.execute(("""INSERT INTO Teacher_Table(TFirst_Name,TLast_Name,Gender,Home_Address,Contact_Number,DOB,Subject,Code)
                            VALUES(?,?,?,?,?,?,?,?)"""), (TFirst,TLast,TGender,THomeAddress,TContactNumber,TDOB,TSub,Rcode,))
                            connection.commit()
                            messagebox.showinfo('Code','The Teacher Code for this Account is %s'%(Rcode))
                    elif currentFrame == 'Student':
                        SFirst = str(self.SFirstE.get())
                        SLast = str(self.SLastE.get())
                        SGender = str(self.SGenderE.get()).upper()
                        SHomeAddress = str(self.SHomeAddressE.get())
                        SContactNumber = str(self.SContactNumberE.get())
                        SDOB = str(self.DOBE.get())
                        BLA=OP1
                        BLB=OP2
                        BLC=OP3
                        BLD=OP4
                        # Ensures the other fields are not empty
                        if (len(SFirst) < 1) or (len(SLast) < 1) or (len(SHomeAddress) < 1) or (len(SContactNumber) < 1):
                            messagebox.showerror('Error', 'Please Fill in all the fields')
                        elif (re.search("[$#@.!£]", SDOB) or re.search("[$#@.!£]", SDOB) or re.search("[A-Z]", SDOB)
                              or re.search("[a-z]", SDOB)):
                            messagebox.showerror('Error', 'Dates should not contain special characters or letters')
                         #Checks the Date entered to make sure they are old enough to be sixth formers
                        elif (SDOB=='')or(len(SDOB)!=10)or(int(SDOB[0:2])>31) or (int(SDOB[0:2])<1) or (int(SDOB[3:5])>12) or (int(SDOB[3:5])<1) or (int(SDOB[6:10])>2002) or (int(SDOB[6:10])<1999):
                            messagebox.showerror('Error','Enter a valid date')
                        #Ensures the only values for Gender are 'M' or 'F'
                        elif SGender != 'M' and SGender!='F':
                            messagebox.showerror('Error','The Gender field should only contain \'M\' or \'F\'')
                        elif(BLA==BLB)or(BLA==BLC)or(BLA==BLD)or(BLB==BLC)or(BLB==BLD)or(BLC==BLD):
                            messagebox.showerror('Error','Subjects cannot be the same')
                        elif (re.search("[$#@.!£]", SFirst) or re.search("[$#@.!£]", SLast) or re.search("[0-9]",SFirst)
                              or re.search("[0-9]", SLast)):
                            messagebox.showerror('Error', 'Names should not contain special characters or numbers')
                        elif (re.search("[a-z]", SContactNumber)) or (re.search("[A-Z]", SContactNumber))or \
                                (re.search("[$#@.!£]", SContactNumber)) or (re.search("\s", SContactNumber)):
                            messagebox.showwarning('Wait!','Phone numbers should only be integer numbers')
                        else:
                            crsr.execute(("""INSERT INTO Student_Table(SFirst_Name,SLast_Name,Gender,Date_of_Birth,Home_Address,Contact_Number,Block_A,Block_B,Block_C,Block_D)
                            VALUES(?,?,?,?,?,?,?,?,?,?)"""), (SFirst,SLast,SGender,SDOB,SHomeAddress,SContactNumber,BLA,BLB,BLC,BLD,))
                            connection.commit()
                            messagebox.showinfo('Success', 'Student has been successfully added to the list')
                except NameError:
                    messagebox.showerror('Error','Please Fill in all the fields')
                

         

                    

root = Tk()
root.resizable(False,False)
app = RegistrationMainWindow(root)
root.mainloop()
