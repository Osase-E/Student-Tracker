import sqlite3
from tkinter import *
from tkinter import messagebox
import re
import smtplib
from datetime import datetime, time
from tkinter import ttk
from tkinter import simpledialog
import io
import ghostscript
import sys
import os
import subprocess
import matplotlib
import numpy as np
from matplotlib.ticker import MaxNLocator
import matplotlib.pyplot as plt

class StudentTracker():
    def __init__(self, master):
        self.master = master
        self.Login()

    def Login(self):
        global forgotP
        global first
        global Login
        Login = Toplevel(self.master)
        Login.title('Login')
        Login.configure(bg='#007534')
        Login.resizable(False, False)
        Login.geometry("460x350")
        self.photo = PhotoImage(file='Logo.gif')
        self.SchoolLogo = Label(Login, image=self.photo, bg='white').grid(row=0, column=0, columnspan=4, sticky=W + E)
        # This opens the main database and creates the teacher login table
        # to store the login details of each teacher
        connection = sqlite3.connect('Main Database')
        crsr = connection.cursor()
        crsr.execute("""CREATE TABLE IF NOT EXISTS Teacher_Login(
            User_ID INTEGER PRIMARY KEY, Username VARCHAR(20),Password VARCHAR(20) NOT NULL,
            Code CHAR(4), Email VARCHAR(100) NOT NULL);""")
        connection.commit()
        connection.close()
        # This is the frame for the main login screen
        first = Frame(Login, bg='#007534')
        first.grid()
        # Here,I will be creating login widgets
        self.usernameL = Label(first, text='Username', bg='#007534', fg='white', font=('Arial', 12, 'bold'))
        self.passwordL = Label(first, text='Password', bg='#007534', fg='white', font=('Arial', 12, 'bold'))
        self.usernameE = Entry(first, width=30)
        self.passwordE = Entry(first, width=30, show='*')
        self.loginButton = Button(first, text='Submit', command=self.login, bg='#B3FF00', font=('Arial', 12, 'bold'))
        self.newUserButton = Button(first, text='New User?', command=self.newUser, bg='#007534', relief=FLAT,
                                    font=('Arial', 10, 'bold', 'underline'), fg='#B3FF00')
        self.forgotButton = Button(first, text='Forgot Password?', command=self.forgot, bg='#007534', relief=FLAT,
                                   font=('Arial', 10, 'bold', 'underline'), fg='#B3FF00')
        self.line1 = Label(first, bg='#007534').grid(row=1, column=0)
        self.usernameL.grid(row=2, column=1, sticky=W)
        self.usernameE.grid(row=3, column=1, columnspan=2, sticky=W)
        self.passwordL.grid(row=4, column=1, sticky=W)
        self.passwordE.grid(row=5, column=1, columnspan=2, sticky=W)
        self.line2 = Label(first, bg='#007534').grid(row=6, column=0)
        self.loginButton.grid(row=7, column=1, columnspan=2)
        self.line3 = Label(first, bg='#007534').grid(row=8, column=0)
        self.newUserButton.grid(row=9, column=3)
        self.forgotButton.grid(row=9, column=0)
        # This is the frame for the forgot password screen
        forgotP = Frame(Login, bg='#007534')
        self.emailFL = Label(forgotP, text='Enter the Email used to register the account', bg='#007534', fg='white',
                             font=('Arial', 12, 'bold'))
        self.emailFE = Entry(forgotP, width=50)
        self.emailBtn = Button(forgotP, text='Back', command=self.back, bg='#B3FF00', font=('Arial', 12, 'bold'))
        self.emailSend = Button(forgotP, text='Send', command=self.send, bg='#B3FF00', font=('Arial', 12, 'bold'))
        self.line4 = Label(forgotP, bg='#007534').grid(row=1, column=0)
        self.emailFL.grid(row=2, column=1)
        self.emailFE.grid(row=3, column=1, columnspan=3)
        self.line5 = Label(forgotP, bg='#007534').grid(row=4, column=0)
        self.emailSend.grid(row=5, column=1, columnspan=2)
        self.line6 = Label(forgotP, bg='#007534').grid(row=6, column=0)
        self.line6 = Label(forgotP, bg='#007534').grid(row=7, column=0)
        self.line6 = Label(forgotP, bg='#007534').grid(row=8, column=0)
        self.line6 = Label(forgotP, bg='#007534').grid(row=9, column=0)
        self.emailBtn.grid(row=10, column=0)

    def login(self):
        global Login
        username = self.usernameE.get()
        pswd = self.passwordE.get()
        connection = sqlite3.connect('Main Database') #Replace with name of database file
        crsr = connection.cursor()
        crsr.execute('''SELECT * from Teacher_Login WHERE Username=? AND Password=?''', (username, pswd,))
        connection.commit()
        if crsr.fetchone() is not None:
            # This returns a confirmation if the user's details match, and will redirect them to the main page once that has been coded
            messagebox.showinfo('Welcome', 'Welcome back')
            Login.destroy()
            self.Main(username)


        else:
            # This returns an error message if the login details do not match
            messagebox.showerror('Error', 'Login Failed')

    def newUser(self):
        Login.withdraw()
        # This loads the window that allows the user to create a new account
        createAccount = Toplevel(bg='#007534')
        createAccount.geometry('600x400')
        createAccount.resizable(False, False)
        createAccount.title('Create an Account')
        self.photos = PhotoImage(file='Logo.gif')
        self.SchoolLogos = Label(createAccount, image=self.photos, bg='white').pack(ipadx=10, pady=(0, 10))
        self.newline2 = Label(createAccount, text=' ', bg='#007534', fg='white', font=('Arial', 32, 'bold'))
        self.usernameL = Label(createAccount, text='Username', bg='#007534', fg='white', font=('Arial', 12, 'bold'))
        self.passwordL = Label(createAccount, text='Password', bg='#007534', fg='white', font=('Arial', 12, 'bold'))
        self.usernameEC = Entry(createAccount, width=30)
        self.passwordEC = Entry(createAccount, show='*', width=30)
        self.passwordLC = Label(createAccount, text='Confirm Password', bg='#007534', fg='white',
                                font=('Arial', 12, 'bold'))
        self.passwordECC = Entry(createAccount, show='*', width=30)
        self.emailL = Label(createAccount, text='Email Address', bg='#007534', fg='white', font=('Arial', 12, 'bold'))
        self.emailE = Entry(createAccount, width=60)
        self.teacherCodeL = Label(createAccount, text='Teacher Code', bg='#007534', fg='white',
                                  font=('Arial', 12, 'bold'))
        self.teacherCodeE = Entry(createAccount)
        self.newline1 = Label(createAccount, text=' ', bg='#007534', fg='white', font=('Arial', 12, 'bold'))
        self.createButton = Button(createAccount, text='Create', command=self.create, bg='#B3FF00',
                                   font=('Arial', 12, 'bold'))
        # handler passes on the 'createAccount' variable to the close function
        handler = lambda: self.closewindow(createAccount)
        self.closebutton = Button(createAccount, text='Close', command=handler, bg='white', fg='black',
                                  font=('Arial', 12, 'bold'))
        self.usernameL.pack()
        self.usernameEC.pack()
        self.passwordL.pack()
        self.passwordEC.pack()
        self.passwordLC.pack()
        self.passwordECC.pack()
        self.emailL.pack()
        self.emailE.pack()
        self.teacherCodeL.pack()
        self.teacherCodeE.pack()
        self.newline1.pack()
        self.createButton.pack(side=RIGHT, padx=20)
        self.closebutton.pack(side=LEFT, padx=20)

    def closewindow(self, createAccount):
        createAccount.destroy()
        Login.update()
        Login.deiconify()

    def forgot(self):
        global forgotP
        global first
        # Packs the forgot password frame to allow user interaction
        Login.title('Forgot Password')
        first.grid_forget()
        forgotP.grid()

    def back(self):
        global forgotP
        global first
        # Unpacks the forgot password frame and brings up the login frame
        Login.title('Login')
        first.grid()
        forgotP.grid_forget()

    def send(self):
        connection = sqlite3.connect('Main Database')
        crsr = connection.cursor()
        try:
            sender = 'EMAIL_ADDRESS' #Enter the email address of the school
            receive = self.emailFE.get()
            subject = 'Login Details'
            crsr.execute('''SELECT Password FROM Teacher_Login WHERE Email=?''', (receive,))
            userpass = crsr.fetchone()
            if userpass is None:
                messagebox.showinfo('Error', 'Email Address does not exist')
            else:
                userpass = userpass[0][::]
                crsr.execute('''SELECT Username FROM Teacher_Login WHERE Email=?''', (receive,))
                useruser = crsr.fetchone()
                useruser = useruser[0][::]
                message = (
                              '''This is in response to your password request, please find attached your login details:
                                     Username = %s
                                     Password = %s''') % (useruser, userpass)
                msg = 'From: %s\r\nTo: %s\r\nSubject: %s\r\nX-Mailer: My-Mail\r\n\r\n' % (sender, receive, subject)
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.ehlo()
                mail.starttls()
                mail.login(sender, '6Monkeys?') #(sender, password)
                mail.sendmail(sender, receive, msg + (message))
                mail.close()
                messagebox.showinfo('Success!', 'An email has been sent to %s with the login details' % (receive))
        except smtplib.SMTPException:
            messagebox.showinfo('Error', 'Please ensure you have typed the correct email address')
        return

    def create(self):
        addUser = True
        connection = sqlite3.connect('Main Database')
        crsr = connection.cursor()
        usernameC = self.usernameEC.get()
        passwordC = self.passwordEC.get()
        email = self.emailE.get()
        code = self.teacherCodeE.get()
        # Checks the password entered if it matches the requirements specified
        while addUser == True:
            if(usernameC == '') or (passwordC=='') or (email=='') or (code=='') or (self.passwordECC.get() == ''):
                messagebox.showerror('Error','Please fill in all fields')
                addUser = False
                break
            if (usernameC != '') and (len(usernameC) > 5):
                addUser = True
            else:
                messagebox.showerror('Error', 'Username should be longer than 5 characters')
                addUser = False
                break
            if ((len(passwordC) > 8) and (re.search("[a-z]", passwordC)) and (re.search("[0-9]", passwordC))
                    and (re.search("[A-Z]", passwordC)) and (re.search("[$#@.!£]", passwordC)) and not (
                    re.search("\s", passwordC))):
                addUser = True
            else:
                messagebox.showerror('Error',
                                     '''Your password must contain at least:
                                     • 1 Uppercase letter and Lowercase
                                     • a symbol from [$#@.!£]
                                     • a number [0-9]
                                     • 8 characters''')
                addUser = False
                break
            # When the password has been verified to match the criteria, it goes on to check if the two passwords match
            if self.passwordEC.get() == self.passwordECC.get():
                addUser = True
            else:
                messagebox.showerror('Oops!', 'Your Passwords do not match')
                addUser = False
                break

            crsr.execute('''SELECT * FROM Teacher_Login WHERE Username=?''', (usernameC,))
            connection.commit()
            # Once the passwords match, the program can then check the username for a duplicate in the database
            if crsr.fetchone() is None:
                addUser = True
            else:
                messagebox.showerror('Error', 'Sorry! Someone already has that Username. Try using a different one')
                addUser = False
                break
            # To ensure the forgot password section of the program does not crash when the user enters their email
            # address, the program will check that the email address
            # is in a particular format
            match = re.search(r"([^@|\s]+@[^@]+\.[com|org]{3}$)", email, re.I)
            if match:
                addUser = True
            else:
                messagebox.showerror('Error',
                                     'Please enter a valid email address in the form: \"emailaddress@email.com\"')
                addUser = False
                break
            try:
                crsr.execute('SELECT Code FROM Teacher_Table WHERE Code=?', (code,))
                if crsr.fetchone() is not None:
                    addUser = True
                else:
                    messagebox.showerror('Error', 'Teacher Code is not registered in the system')
                    addUser = False
                    break
            except sqlite3.OperationalError:
                messagebox.showerror('Error', 'Teacher Code is not registered in the system')
                addUser = False
                break
            if addUser == True:
                crsr.execute('''INSERT INTO Teacher_Login(Username,Password,
                    Email, Code) VALUES (?,?,?,?)''', (usernameC, passwordC, email, code,))
                connection.commit()
                messagebox.showinfo('Success!', '''You have successfully created an account.
                    \nYou may now close the window using the close button to return to the previous screen''')
                # Inserts all the data the user has entered into the Teacher_Login table
                addUser = False

    def Main(self, username):
        global students
        Main = Toplevel(self.master)
        Main.title('Student Tracker')
        Main.configure(bg='#007534')
        Main.geometry('720x480')
        rootFrame = Frame(Main)
        rootFrame.grid(row=0, column=0, sticky='nsew')
        self.photo = PhotoImage(file='Logo.gif')
        Label(rootFrame, image=self.photo, bg='white').grid(row=0, column=0, columnspan=2, sticky=W + E)
        connection = sqlite3.connect('Main Database')
        crsr = connection.cursor()
        crsr.execute('SELECT Code FROM Teacher_Login WHERE Username=?', (username,))
        temp = crsr.fetchone()
        temp = temp[0][::]
        crsr.execute('SELECT TLast_Name FROM Teacher_Table WHERE Code=?', (temp,))
        tempName = crsr.fetchone()
        tempName = tempName[0][::]
        crsr.execute('SELECT Gender FROM Teacher_Table WHERE Code=?', (temp,))
        tempGen = crsr.fetchone()
        tempGen = tempGen[0][::]
        if tempGen == 'M':
            title = 'Mr. '
        else:
            title = 'Ms. '
        mainFrame = Frame(Main)
        mainFrame.grid(row=1, column=0, sticky="nsew")
        leftSide = Frame(mainFrame, bg='#007534')
        leftSide.grid(sticky="nsew", row=0, column=0)
        rightSide = Frame(mainFrame, bg='#A8D59D')
        rightSide.grid(sticky="nsew", row=0, column=1)
        Label(leftSide, text='Welcome,\n ' + title + tempName, fg='white', bg='#007534',
              font=('Arial', 12, 'bold')).grid(row=0, column=0, sticky='news', padx=20)
        Button(leftSide, text='Attendance', bg='white', fg='#007534', command=self.attendance,
               font=('Arial', 12, 'bold')).grid(row=1, column=0, pady=20, padx=20, sticky='news')
        Button(leftSide, text='Graphs', bg='white', fg='#007534', command=self.graphs, font=('Arial', 12, 'bold')).grid(
            row=2, column=0, pady=20, sticky='news', padx=20)
        Button(leftSide, text='Results', bg='white', fg='#007534', command=self.results,
               font=('Arial', 12, 'bold')).grid(row=3, column=0, pady=20, sticky='news', padx=20)
        topRight = Frame(rightSide)
        topRight.grid(row=0, column=0, columnspan=3)
        Label(topRight, text='Student:', bg='#A8D59D', fg='black', font=('Arial', 12, 'bold')).grid(row=0, column=0,
                                                                                                    sticky='news')
        sSearch = Entry(topRight, width=30)
        sSearch.grid(row=0, column=1, sticky='news')
        handler = lambda: self.view(sSearch.get())
        Button(topRight, text='Search', command=handler, bg='#B3FF00', fg='black', font=('Arial', 12, 'bold')).grid(
            row=0, column=2)
        try:
            crsr.execute('SELECT SFirst_Name,SLast_Name FROM Student_Table ')
            scrollbar = Scrollbar(rightSide)
            scrollbar.grid(row=1, column=1, sticky='ns')
            studentList = crsr.fetchall()
            students = Listbox(rightSide, yscrollcommand=scrollbar.set, fg='black', bg='#A8D59D',
                               font=('Arial', 12, 'bold'))
            for i in studentList:
                students.insert(END, i[0][::] + ' ' + i[1][::])
            students.grid(row=1, column=0, sticky='news', padx=(20, 0))
            scrollbar.config(command=students.yview)
        except:
            messagebox.showerror('Error', 'There are no students registered')
        Button(rightSide, text='View Profile', command=self.view, bg='#B3FF00', fg='black',
               font=('Arial', 12, 'bold')).grid(row=2, column=0, columnspan=2, sticky=E, padx=20)
        Main.grid_columnconfigure(0, weight=1)
        Main.grid_rowconfigure(1, weight=1)
        rootFrame.grid_columnconfigure(0, weight=1)
        mainFrame.grid_columnconfigure(0, weight=1)
        mainFrame.grid_columnconfigure(1, weight=4)
        mainFrame.grid_rowconfigure(0, weight=1)
        leftSide.grid_columnconfigure(0, weight=1)
        leftSide.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        rightSide.grid_columnconfigure(0, weight=1)
        rightSide.grid_rowconfigure((0, 1, 2), weight=1)
        topRight.grid_columnconfigure(1, weight=1)

    def refresh(self):
        global Attend
        Attend.destroy()
        self.attendance()

    def attendance(self, stat=None, todaysDate=None):
        global vars, atStudentList, status, Attend
        global atFrame, atView, atEdit, atOverview, View, todayDate
        Attend = Toplevel(self.master)
        Attend.title('Attendance')
        Attend.configure(bg='#A8D59D')
        Attend.geometry('640x480')
        menubar = Menu(Attend, bg='#B3FF00')
        menubar.add_command(label='View Attendance', command=self.atView)
        editmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Edit Attendance', menu=editmenu)
        editmenu.add_command(label='Edit Date', command=self.editAttendDate)
        editmenu.add_command(label='Edit Period', command=self.editAttendPeriod)
        menubar.add_command(label='Refresh', command=self.refresh)
        Attend.config(menu=menubar)
        atFrame = Frame(Attend, bg='#007534')
        atFrame.grid(row=0, column=0, columnspan=5, sticky='news')
        self.photoA = PhotoImage(file='Logo.gif')
        Label(atFrame, image=self.photoA, bg='white').grid(row=0, column=0, columnspan=5, sticky='ew')
        # Creates a dictionary to match the current time to a period in school
        if stat == None:
            times = {
                'P1': (time(9, 00), time(10, 00)),
                'P2': (time(10, 00), time(11, 00)),
                '1st Break': (time(11, 00), time(11, 30)),
                'P3': (time(11, 30), time(12, 30)),
                'P4': (time(12, 30), time(13, 30)),
                '2nd Break': (time(13, 30), time(14, 00)),
                'P5': (time(14, 00), time(15, 00))
            }
            # Retrieves current time
            check_time = datetime.now().time()
            status = 'Break'
            # Corresponds the current time to a relevant time period
            for i in times:
                if (check_time >= times[i][0] and check_time < times[i][1]):
                    # Returns the value of i for which the constraints are met
                    status = i
        else:
            status = stat
        # Formats the date to DD/MM/YYYY
        if todaysDate == None:
            todayDate = str(datetime.now().date().day) + '/' + str(datetime.now().date().month) + '/' + str(
                datetime.now().date().year)
        else:
            todayDate = todaysDate
        Label(atFrame, text=status, fg='white', bg='#007534', font=('Arial', 12, 'bold')).grid(row=1, column=0)
        Button(atFrame, text='Save', command=self.atSave, bg='#B3FF00', fg='black', font=('Arial', 12, 'bold')).grid(
            row=1, column=3)
        Label(atFrame, text='Attendance of \n' + todayDate, fg='white', bg='#007534', font=('Arial', 12, 'bold')).grid(
            row=1, column=1, columnspan=2, sticky='news')
        atView = Frame(Attend, bg='black', borderwidth=0)
        atView.grid(row=1, column=0, columnspan=5, sticky='ew', pady=(10, 0), padx=10)
        Label(atView, text='Student Name', bg='black', fg='white', font=('Arial', 12, 'bold')).grid(row=0, column=0)
        Label(atView, text='Status', bg='black', fg='white', font=('Arial', 12, 'bold')).grid(row=0, column=1,
                                                                                              columnspan=3)
        atEdit = Frame(Attend, borderwidth=0, bg='white')
        atEdit.grid(row=2, column=0, columnspan=5, sticky='news', pady=(0, 10), padx=10)
        self.canvas = Canvas(atEdit, bg='black')
        self.canvas.grid(row=0, column=0, columnspan=5, sticky='news')
        self.mainFC = Frame(self.canvas, borderwidth=0)
        self.mainFC.grid(sticky='news')
        left = Frame(self.mainFC, borderwidth=0, bg='#dbdbdb')
        left.grid(row=0, column=0, sticky='news')
        right = Frame(self.mainFC, borderwidth=0, bg='white')
        right.grid(row=0, column=1, columnspan=4, sticky='news')
        self.mainC = self.canvas.create_window((0, 0), window=self.mainFC, anchor=NW)
        self.canvas.update()
        self.mainFC.bind('<Configure>', self.OnFrameConfigure)
        self.canvas.bind('<Configure>', self.FrameWidth)
        scrollbar = Scrollbar(atEdit)
        scrollbar.grid(row=0, column=5, sticky='ns')
        scrollbar.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=scrollbar.set)

        try:
            # Connects to the database
            conn = sqlite3.connect('Main Database')
            crsr = conn.cursor()
            crsr.execute('''CREATE TABLE IF NOT EXISTS Attendance(SID INTEGER PRIMARY KEY,
            SName VARCHAR(255) NOT NULL);''')
            conn.commit()
            crsr.execute('SELECT SFirst_Name,SLast_Name FROM Student_Table')
            # Retrieves the list of students from the original student table
            mainStudentList = crsr.fetchall()
            tempListA = []
            for i in mainStudentList:
                tempListA.append(i[0][::] + ' ' + i[1][::])
            mainStudentList = tempListA
            tempListB = []
            crsr.execute('SELECT SName FROM Attendance') #StudentName
            # Retrieves the list of students from the attendance table
            atStudentList = crsr.fetchall()
            for i in atStudentList:
                tempListB.append(i[0][::])
            atStudentList = tempListB
            toAdd = []
            for i in mainStudentList:
                if not any(x == i for x in atStudentList):
                    toAdd.append(i)
            for i in toAdd:
                tempN = i
                crsr.execute('INSERT INTO Attendance(SName) VALUES(?)', (tempN,))
                conn.commit()
            crsr.execute('SELECT SName FROM Attendance')
            # Retrieves the list of students from the attendance table
            atStudentList = crsr.fetchall()
            counter = 0
            vars = []
            for i in atStudentList:
                var = StringVar()
                vars.append(var)
                Label(left, text=i[0][::], fg='black', bg='#dbdbdb', font=('Arial', 11, 'bold')).grid(row=counter,
                                                                                                      column=0, pady=13,
                                                                                                      sticky='news')
                Radiobutton(right, text='Present', variable=var, bg='#56ab32', fg='black', value='P', indicatoron=0,
                            font=('Arial', 12, 'bold')).grid(row=counter, column=0, pady=10, padx=20, sticky='news')
                Radiobutton(right, text='Leave', variable=var, bg='#e6a800', fg='black', indicatoron=0, value='L',
                            font=('Arial', 12, 'bold')).grid(row=counter, column=1, pady=10, padx=20, sticky='news')
                Radiobutton(right, text='Absent', variable=var, bg='#bd2900', fg='black', indicatoron=0, value='A',
                            font=('Arial', 12, 'bold')).grid(row=counter, column=2, pady=10, padx=20, sticky='news')
                counter += 1
        except:
            # Returns an error if no students have been registered in the database
            messagebox.showerror('Error', 'There are no students registered')

        Attend.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        Attend.grid_rowconfigure((2), weight=1)
        atFrame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        atFrame.grid_rowconfigure((1, 2, 3, 4), weight=1)
        atView.grid_columnconfigure(0, weight=1)
        atView.grid_columnconfigure(1, weight=3)
        atEdit.grid_columnconfigure(0, weight=1)
        atEdit.grid_rowconfigure((0, 1, 2), weight=1)
        atEdit.grid_columnconfigure((1, 2, 3, 4), weight=3)
        self.canvas.grid_columnconfigure(0, weight=1)
        self.canvas.grid_columnconfigure(1, weight=3)
        left.grid_columnconfigure(0, weight=1)
        right.grid_columnconfigure((0, 1, 2), weight=1)
        self.mainFC.grid_columnconfigure(0, weight=1)
        self.mainFC.grid_rowconfigure(0, weight=1)
        self.mainFC.grid_columnconfigure(1, weight=3)

    def FrameWidth(self, event):
        canvas_width = event.width
        self.canvas.itemconfigure(self.mainC, width=canvas_width)
        w, h = event.width, event.height
        self.canvas.config(width=w, height=h)

    def OnFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def atView(self):
        global Attend, View
        global todayDate, status
        try:
            Attend.destroy()
            View = Toplevel(self.master)
            View.title('Attendance Overview')
            View.geometry('1024x640')
            View.resizable(False, True)
            conn = sqlite3.connect('Main Database')
            crsr = conn.cursor()
            crsr.execute('SELECT SName FROM Attendance')
            # Retrieves the list of students from the attendance table
            atStudentList = crsr.fetchall()

            # --- Start of atOverview initialisation ---#
            atOverview = Frame(View, bg='#007534')
            atOverview.grid(row=0, column=0, columnspan=6, sticky='news')
            self.photoB = PhotoImage(file='Logo.gif')
            Label(atOverview, image=self.photoB, bg='white').grid(row=0, column=0, columnspan=6, sticky='ew')
            Button(atOverview, text='Edit', command=self.atEdit, bg='#B3FF00', fg='black',
                   font=('Arial', 12, 'bold')).grid(row=1, column=2)
            Label(atOverview, text='Attendance of \n' + todayDate, fg='white', bg='#007534',
                  font=('Arial', 12, 'bold')).grid(row=1, column=1, sticky='news')

            atAView = Frame(View, bg='black', borderwidth=0)
            atAView.grid(row=1, column=0, columnspan=5, sticky='ew', pady=(10, 0), padx=10)
            Label(atAView, text='Student Name', bg='black', fg='white', font=('Arial', 12, 'bold')).grid(row=0,
                                                                                                         column=0)
            Label(atAView, text='P1', bg='black', fg='white', font=('Arial', 12, 'bold')).grid(row=0, column=1, padx=10)
            Label(atAView, text='P2', bg='black', fg='white', font=('Arial', 12, 'bold')).grid(row=0, column=2, padx=10)
            Label(atAView, text='P3', bg='black', fg='white', font=('Arial', 12, 'bold')).grid(row=0, column=3, padx=10)
            Label(atAView, text='P4', bg='black', fg='white', font=('Arial', 12, 'bold')).grid(row=0, column=4, padx=10)
            Label(atAView, text='P5', bg='black', fg='white', font=('Arial', 12, 'bold')).grid(row=0, column=5,
                                                                                               padx=(10, 40))
            atAEdit = Frame(View, borderwidth=0, bg='white')
            atAEdit.grid(row=2, column=0, columnspan=5, sticky='news', pady=(0, 10), padx=10)
            self.Acanvas = Canvas(atAEdit, bg='black')
            self.Acanvas.grid(row=0, column=0, columnspan=5, sticky='news')
            self.AmainFC = Frame(self.Acanvas, borderwidth=0)
            self.AmainFC.grid(sticky='news')
            Aleft = Frame(self.AmainFC, borderwidth=0, bg='#dbdbdb')
            Aleft.grid(row=0, column=0, sticky='news')
            Aright = Frame(self.AmainFC, borderwidth=0, bg='white')
            Aright.grid(row=0, column=1, columnspan=4, sticky='news')
            self.AmainC = self.Acanvas.create_window((0, 0), window=self.AmainFC, anchor=NW)
            self.Acanvas.update()
            self.AmainFC.bind('<Configure>', self.AOnFrameConfigure)
            self.Acanvas.bind('<Configure>', self.AFrameWidth)
            Ascrollbar = Scrollbar(atAEdit)
            Ascrollbar.grid(row=0, column=6, sticky='ns')
            Ascrollbar.config(command=self.Acanvas.yview)
            self.Acanvas.config(yscrollcommand=Ascrollbar.set)
            counter = 0
            AtodayDate = todayDate.replace('/', '_')
            # Initiates column headings
            col1 = 'P1_' + AtodayDate
            col2 = 'P2_' + AtodayDate
            col3 = 'P3_' + AtodayDate
            col4 = 'P4_' + AtodayDate
            col5 = 'P5_' + AtodayDate
            # To prevent the software from breaking, the program will only retrieve columns from the table
            # depending on the current time period
            if status == 'P1':
                com = 'select %s from Attendance' % (col1)
            elif status == 'P2' or status == '1st Break':
                com = 'select %s,%s from Attendance' % (col1, col2)
            elif status == 'P3':
                com = 'select %s,%s,%s from Attendance' % (col1, col2, col3)
            elif status == 'P4' or status == '2nd Break':
                com = 'select %s,%s,%s,%s from Attendance' % (col1, col2, col3, col4)
            elif (status == 'P5') or (status == 'Break'):
                com = 'select %s,%s,%s,%s,%s from Attendance' % (col1, col2, col3, col4, col5)
            crsr.execute(com)
            stuStat = crsr.fetchall()
            for i in atStudentList:
                # Iterates over the student list and creates the labels for the name and attendance mark
                Label(Aleft, text=i[0][::], fg='black', bg='#dbdbdb', font=('Arial', 11, 'bold')).grid(row=counter,
                        column=0,pady=13,sticky='news')
                if status == 'P1':
                    Label(Aright, text=stuStat[counter][0], borderwidth=2, relief='solid', fg='black', bg='white',
                          font=('Arial', 11, 'bold')).grid(row=counter, column=0, padx=10, pady=13, sticky='news')
                elif status == 'P2' or status == '1st Break':
                    Label(Aright, text=stuStat[counter][0], fg='black', bg='white', font=('Arial', 11, 'bold')).grid(
                        row=counter, column=0, pady=13, sticky='news')
                    Label(Aright, text=stuStat[counter][1], fg='black', bg='white', font=('Arial', 11, 'bold')).grid(
                        row=counter, column=1, pady=13, sticky='news')
                elif status == 'P3':
                    Label(Aright, text=stuStat[counter][0], fg='black', bg='white', font=('Arial', 11, 'bold')).grid(
                        row=counter, column=0, pady=13, sticky='news')
                    Label(Aright, text=stuStat[counter][1], fg='black', bg='white', font=('Arial', 11, 'bold')).grid(
                        row=counter, column=1, pady=13, sticky='news')
                    Label(Aright, text=stuStat[counter][2], fg='black', bg='white', font=('Arial', 11, 'bold')).grid(
                        row=counter, column=2, pady=13, sticky='news')
                elif status == 'P4' or status == '2nd Break':
                    Label(Aright, text=stuStat[counter][0], fg='black', bg='white', font=('Arial', 11, 'bold')).grid(
                        row=counter, column=0, pady=13, sticky='news')
                    Label(Aright, text=stuStat[counter][1], fg='black', bg='white', font=('Arial', 11, 'bold')).grid(
                        row=counter, column=1, pady=13, sticky='news')
                    Label(Aright, text=stuStat[counter][2], fg='black', bg='white', font=('Arial', 11, 'bold')).grid(
                        row=counter, column=2, pady=13, sticky='news')
                    Label(Aright, text=stuStat[counter][3], fg='black', bg='white', font=('Arial', 11, 'bold')).grid(
                        row=counter, column=3, pady=13, sticky='news')
                elif status == 'P5' or (status == 'Break'):
                    Label(Aright, text=stuStat[counter][0], fg='black', bg='white', font=('Arial', 11, 'bold')).grid(
                        row=counter, column=0, pady=13, sticky='news')
                    Label(Aright, text=stuStat[counter][1], fg='black', bg='white', font=('Arial', 11, 'bold')).grid(
                        row=counter, column=1, pady=13, sticky='news')
                    Label(Aright, text=stuStat[counter][2], fg='black', bg='white', font=('Arial', 11, 'bold')).grid(
                        row=counter, column=2, pady=13, sticky='news')
                    Label(Aright, text=stuStat[counter][3], fg='black', bg='white', font=('Arial', 11, 'bold')).grid(
                        row=counter, column=3, pady=13, sticky='news')
                    Label(Aright, text=stuStat[counter][4], fg='black', bg='white', font=('Arial', 11, 'bold')).grid(
                        row=counter, column=4, pady=13, sticky='news')
                counter += 1

            View.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
            View.grid_rowconfigure((2), weight=1)
            atOverview.grid_columnconfigure((0, 1, 2, 3), weight=1)
            atOverview.grid_rowconfigure((1, 2, 3, 4), weight=1)
            atAView.grid_columnconfigure(0, weight=2)
            atAView.grid_columnconfigure((1, 2, 3, 4, 5), weight=1)
            atAEdit.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
            atAEdit.grid_rowconfigure((0, 1, 2), weight=1)
            self.Acanvas.grid_columnconfigure((0, 1), weight=1)
            Aleft.grid_columnconfigure(0, weight=1)
            Aright.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
            self.AmainFC.grid_columnconfigure(0, weight=2)
            self.AmainFC.grid_rowconfigure(0, weight=1)
            self.AmainFC.grid_columnconfigure(1, weight=8)
        except sqlite3.OperationalError:
            View.destroy()
            self.attendance()
            messagebox.showerror('Error', 'No attendance records found for today')

    def AFrameWidth(self, event):
        canvas_width = event.width
        self.Acanvas.itemconfigure(self.AmainC, width=canvas_width)
        w, h = event.width, event.height
        self.Acanvas.config(width=w, height=h)

    def AOnFrameConfigure(self, event):
        self.Acanvas.configure(scrollregion=self.Acanvas.bbox("all"))

    def editAttendPeriod(self):
        global Attend, status, todayDate
        stat = simpledialog.askstring('Prompt', 'What period would you like to edit?\n In the form: P1,P2,P3,P4 or P5')
        if stat == 'P1' or stat == 'P2' or stat == 'P3' or stat == 'P4' or stat == 'P5':
            Attend.destroy()
            self.attendance(stat, todayDate)
        else:
            messagebox.showerror('Error', 'Please enter a period')

    def editAttendDate(self):
        global Attend, status, todayDate
        date = simpledialog.askstring('Prompt', 'What date would you like to edit?\n In the form: DD/MM/YYYY')
        if len(date) != 10:
            messagebox.showerror('Error', 'Enter a valid date')
        else:
            try:
                if int(date[3:5]) <= datetime.now().date().month and int(date[6:10]) <= datetime.now().date().year:
                    if int(date[3:5]) < datetime.now().date().month:
                        if int(date[0:2]) < 31:
                            date = str(int(date[0:2])) + '/' + str(int(date[3:5])) + '/' + str(int(date[6:10]))
                            Attend.destroy()
                            self.attendance(status, date)
                        else:
                            messagebox.showerror('Error', 'Enter a valid date')
                    elif int(date[3:5]) == datetime.now().date().month:
                        if int(date[0:2]) <= datetime.now().date().day:
                            date = str(int(date[0:2])) + '/' + str(int(date[3:5])) + '/' + str(int(date[6:10]))
                            Attend.destroy()
                            self.attendance(status, date)
                        else:
                            messagebox.showerror('Error', 'Enter a valid date')
                else:
                    messagebox.showerror('Error', 'No day has been selected')
            except ValueError:
                messagebox.showerror('Error', 'Enter a valid date')

    def atEdit(self):
        global Attend, View
        View.destroy()
        self.attendance()

    def atSave(self):
        global status, todayDate
        global vars
        global atStudentList
        # Retrieve the current date in a format that is acceptable to sqlite3
        if status == 'Break' or status == '1st Break' or status == '2nd Break':
            messagebox.showerror('Wait!', 'You can not take attendance during break')
        else:
            if todayDate == None:
                todayDate = str(datetime.now().date().day) + '_' + str(datetime.now().date().month) + '_' + str(
                    datetime.now().date().year)
            counter = 0
            attendanceList = []
            for i in atStudentList:
                # Retrieves the attendance status for each student
                attendanceList.append(vars[counter].get())
                counter += 1
            if any(x == '' for x in attendanceList):
                messagebox.showerror('Error', 'Please make sure all students have been given marks')
                # Clears the attendance list and returns an error if there is an empty item in the list
                attendanceList.clear()
            else:
                counter = 1
                conn = sqlite3.connect('Main Database')
                crsr = conn.cursor()
                tableDesc = crsr.execute('select * from Attendance').description
                tempAdd = []
                for row in tableDesc:
                    tempAdd.append(row[0])
                AtodayDate = todayDate.replace('/', '_')
                columnName = status + '_' + AtodayDate
                # Checks if the date is registered in the system
                if any(x == columnName for x in tempAdd):
                    for stat in attendanceList:
                        # Appends each status to the Attendance Table
                        com = 'UPDATE Attendance SET %s = \'%s\' WHERE SID =%s' % (columnName, stat, counter)
                        crsr.execute(com)
                        conn.commit()
                        counter += 1
                    messagebox.showinfo('Success!', 'The attendance has been taken')
                else:
                    # Adds a column for the current time period if it does not exist
                    com = 'ALTER TABLE Attendance ADD COLUMN %s CHAR(1)' % (columnName)
                    crsr.execute(com)
                    conn.commit()
                    for stat in attendanceList:
                        com = 'UPDATE Attendance SET %s = \'%s\' WHERE SID =%s' % (columnName, stat, counter)
                        crsr.execute(com)
                        conn.commit()
                        counter += 1
                    messagebox.showinfo('Success!', 'The attendance has been taken')

    def graphs(self):
        global students
        try:
            # Retrieves the option the user selected from the listbox
            sel = students.curselection()
            sel = str(int(str(sel[0])) + 1)
            connection = sqlite3.connect('Main Database')
            crsr = connection.cursor()
            crsr.execute(
                '''SELECT SFirst_Name,SLast_Name FROM Student_Table WHERE SID=?''',
                (sel,))
            result = crsr.fetchone()
            First = result[0][::]
            Last = result[1][::]
            crsr.execute('''select * from Attendance where SID=?''', (sel,))
            temp = crsr.fetchone()
            attendResult = []
            for i in temp:
                attendResult.append(i)
            del attendResult[0]
            del attendResult[0]
            # Initiates a counter to keep track of the number of absents the student has, as well as the number of
            # times the student has been present
            Acounter = 0
            Pcounter = 0
            Lcounter = 0
            for x in attendResult:
                if x == 'A':
                    Acounter += 1
                elif x=='P':
                    Pcounter += 1
                elif x=='L':
                    Lcounter += 1
            # Customises the labels of the graph
            plt.xlabel('Attendance Status')
            plt.ylabel('Number of times')
            plt.title('Attendance Result of '+First+' '+Last)
            # Creates the bars, and adds the data to plot
            plt.bar('Present',Pcounter,color='#56ab32',zorder=5)
            plt.bar('Leave', Lcounter, color='#e6a800',zorder=5)
            plt.bar('Absent',Acounter, color='#bd2900',zorder=5)
            plt.ylim(bottom=0)
            plt.rc('axes', axisbelow=True)
            plt.grid(True)
            plt.show()
        except:
            messagebox.showinfo('Info','If no student was selected, the overall class attendance is displayed')
            connection = sqlite3.connect('Main Database')
            crsr = connection.cursor()
            crsr.execute('''select * from Attendance''')
            temp = crsr.fetchall()
            attendResult = []
            count = 0
            tempAdd = []
            for i in temp:
                attendResult.append(i)
            for i in range(len(attendResult)):
                mock = []
                for x in attendResult[i]:
                    mock.append(x)
                del mock[0]
                del mock[0]
                tempAdd= tempAdd+mock
            # Initiates a counter to keep track of the number of absents the student has, as well as the number of
            # times the student has been present
            Acounter = 0
            Pcounter = 0
            Lcounter = 0
            for x in tempAdd:
                if x == 'A':
                    Acounter += 1
                elif x == 'P':
                    Pcounter += 1
                elif x == 'L':
                    Lcounter += 1
            # Customises the labels of the graph
            plt.xlabel('Attendance Status')
            plt.ylabel('Number of times')
            plt.title('Overall Attendance Result')
            # Creates the bars, and adds the data to plot
            plt.bar('Present', Pcounter, color='#56ab32', zorder=5)
            plt.bar('Leave', Lcounter, color='#e6a800', zorder=5)
            plt.bar('Absent', Acounter, color='#bd2900', zorder=5)
            plt.ylim(bottom=0)
            plt.rc('axes', axisbelow=True)
            plt.grid(True)
            plt.show()


    def results(self):
        try:
            global students
            #Creates the Result Window
            self.Result = Toplevel(self.master)
            self.Result.title('Result')
            self.Result.configure(bg='#A8D59D')
            self.Result.geometry('640x500')
            self.Result.resizable(False,False)
            menubar = Menu(self.Result, bg='#B3FF00')
            menubar.add_command(label='Export', command=self.exportFile)
            self.Result.config(menu=menubar)
            self.mainCanvas = Canvas(self.Result, background='#A8D59D')
            self.mainCanvas.pack(expand=1, fill=BOTH)
            self.mainCanvas.update()
            self.mainCanvas.create_rectangle((0,0,640,540),fill='#A8D59D')
            self.mainCanvas.create_rectangle((0, 0, 640, 80), fill='#FFFFFF')
            self.photoH = PhotoImage(file='Logo.gif')
            self.mainCanvas.create_image((0,0),image=self.photoH,anchor=NW)
            self.mainCanvas.create_rectangle(0,80,640,120,fill='#007534')
            # Retrieves the option the user selected from the listbox
            sel = students.curselection()
            sel = str(int(str(sel[0])) + 1)
            connection = sqlite3.connect('Main Database')
            crsr = connection.cursor()
            crsr.execute(
                '''SELECT SFirst_Name,SLast_Name FROM Student_Table WHERE SID=?''',
                (sel,))
            result = crsr.fetchone()
            First = result[0][::]
            Last = result[1][::]
            crsr.execute('''select * from Attendance where SID=?''', (sel,))
            temp = crsr.fetchone()
            attendResult = []
            for i in temp:
                attendResult.append(i)
            del attendResult[0]
            del attendResult[0]
            # Initiates a counter to keep track of the number of absents the student has, as well as the number of
            # times the student has been present
            daysCounter = len(attendResult)
            Acounter = 0
            Pcounter = 0
            for x in attendResult:
                if x == 'A':
                    Acounter += 1
                elif x=='P':
                    Pcounter += 1


            try:
                # Checks the report table for any reports
                crsr.execute('select Report from Reports where SID=?', (sel,))
                toAdd = crsr.fetchone()
                toAdd = toAdd[0][::]
            except:
                # If no reports are found, then the message displayed will be 'No comments'
                toAdd = 'No comments'
            self.mainCanvas.create_text((320, 100), text=(First + ' ' + Last), font=('Arial', 12, 'bold'),
                                        fill='#FFFFFF')
            self.mainCanvas.create_text((140,155), text=('Total Number of Sessions:'), font=('Arial', 12, 'bold'),
                                        fill='#000000')
            self.mainCanvas.create_text((510, 155), text=(daysCounter), font=('Arial', 12, 'bold'),
                                        fill='#000000')
            self.mainCanvas.create_text((140, 200), text=('Total Number of Presents:'), font=('Arial', 12, 'bold'),
                                        fill='#000000')
            self.mainCanvas.create_text((510, 200), text=(Pcounter), font=('Arial', 12, 'bold'),
                                        fill='#000000')
            self.mainCanvas.create_text((140, 245), text=('Total Number of Absents: '), font=('Arial', 12, 'bold'),
                                        fill='#000000')
            self.mainCanvas.create_text((510, 245), text=(Acounter), font=('Arial', 12, 'bold'),
                                        fill='#000000')
            self.mainCanvas.create_text((40, 300), text=('Comments:'), font=('Arial', 12, 'bold'),
                                        fill='#000000',anchor=NW)
            self.mainCanvas.create_text((30, 325), text=(toAdd), font=('Arial', 12, 'bold'),
                                        fill='#000000',anchor=NW)

        except IndexError:
            self.Result.destroy()
            messagebox.showerror('Oops!','Please select a student')

    def exportFile(self):
        self.mainCanvas.update()
        self.mainCanvas.postscript(file="tmp.ps", colormode='color')
        # Creates a .ps file of the canvas contents
        if (sys.platform == 'win32'):
            gs = 'gswin32'
        elif (sys.platform == 'win64'):
            gs= 'gswin64'
        else:
            gs='gs'
        # Uses the command 'gswin32' if the user is using windows 32-bit or 'gswin64' if the user is on the
        # 64-bit windows
        subprocess.check_output([gs, '-q', '-P-', '-dSAFER', '-dNOPAUSE', '-dBATCH',
        '-sDEVICE=pdfwrite', '-sOutputFile=result.pdf', '-c','.setpdfwrite', '-f', 'tmp.ps'])
        #COnverts the .ps file to a .pdf file and saves the file in the program's directory
        self.Result.destroy()

    def view(self, sel=None):
        try:
            if sel == None:
                global students
                # Retrieves the option the user selected from the listbox
                sel = students.curselection()
                sel = str(int(str(sel[0])) + 1)
                connection = sqlite3.connect('Main Database')
                crsr = connection.cursor()
                crsr.execute(
                    '''SELECT SFirst_Name,SLast_Name,Gender,Date_of_Birth,Home_Address,Contact_Number,Block_A,Block_B,Block_C,Block_D FROM Student_Table WHERE SID=?''',
                    (sel,))
                result = crsr.fetchone()
                crsr.execute('''select * from Attendance where SID=?''', (sel,))
                temp = crsr.fetchone()
                attendResult = []
                for i in temp:
                    attendResult.append(i)
                # Brings out the data of the student matching the ID number retrieved
                handler = lambda: self.report(None,sel)
            else:
                try:
                    mockSel = sel
                    sel = sel.split()
                    connection = sqlite3.connect('Main Database')
                    crsr = connection.cursor()
                    crsr.execute('''SELECT SFirst_Name,SLast_Name,Gender,Date_of_Birth,Home_Address,Contact_Number,Block_A,Block_B,Block_C,Block_D FROM Student_Table WHERE SFirst_Name=? AND
                    SLast_Name=?''', (sel[0], sel[1],))
                    result = crsr.fetchone()
                    if result == None:
                        messagebox.showerror('Oops!', 'Please make sure there are no spelling mistakes')
                        return
                    else:
                        crsr.execute('''select * from Attendance where SName=?''', (sel[0] + ' ' + sel[1],))
                        temp = crsr.fetchone()
                        attendResult = []
                        for i in temp:
                            attendResult.append(i)
                        handler = lambda: self.report(mockSel,None)
                except:
                    messagebox.showerror('Oops!', 'Please make sure there are no spelling mistakes')
                    return
            # Deletes the ID column and Name column from the list of items retrieved
            del attendResult[0]
            del attendResult[0]
            daysCounter = len(attendResult)
            Acounter = 0
            # Creates an absent counter, which increments by one for each absent mark received
            for x in attendResult:
                if x == 'A':
                    Acounter += 1
            # Calculates the ratio of absent to total number of sessions, and converts the fraction into a percentage
            percent = int(round(((daysCounter - Acounter) / daysCounter) * 100))
            # Creates the Toplevel to display the results
            self.studentWindow = Toplevel(self.master)
            self.studentWindow.title('Student Info')
            self.studentWindow.configure(bg='#A8D59D')
            self.studentWindow.geometry('640x480')
            self.photoM = PhotoImage(file='Logo.gif')
            Label(self.studentWindow, image=self.photoM, bg='white').grid(row=0, column=0, columnspan=5, sticky='ew')
            self.reportImage = PhotoImage(file='report.gif')
            left = Frame(self.studentWindow, bg='#007534')
            left.grid(row=1, column=0, sticky='news')
            right = Frame(self.studentWindow, bg='#A8D59D')
            right.grid(row=1, column=1, sticky='news')
            fields = ['First Name', 'Last Name', 'Gender', 'Date of Birth', 'Home Address', 'Contact Number',
                      'Subjects']
            for i in range(0, (len(fields) - 1)):
                Label(right, text=fields[i], bg='#007534', fg='white', borderwidth=2, relief="raised",
                      font=('Arial', 12, 'bold')).grid(row=i, column=0, sticky='news', padx=15, pady=8)
                Label(right, text=result[i], bg='#A8D59D', fg='black', borderwidth=2, relief="flat",
                      font=('Arial', 12, 'bold')).grid(row=i, column=1, sticky='news', padx=5, pady=8, columnspan=2)
            Label(right, text=fields[6], bg='#007534', fg='white', borderwidth=2, relief="raised",
                  font=('Arial', 12, 'bold')).grid(row=6, column=0, sticky='news', padx=15, pady=8)
            Label(right, text=result[6], bg='#A8D59D', fg='black', borderwidth=2, relief="flat",
                  font=('Arial', 12, 'bold')).grid(row=6, column=1, sticky='news', padx=5, pady=8)
            Label(right, text=result[7], bg='#A8D59D', fg='black', borderwidth=2, relief="flat",
                  font=('Arial', 12, 'bold')).grid(row=6, column=2, sticky='news', padx=5, pady=8)
            Label(right, text=result[8], bg='#A8D59D', fg='black', borderwidth=2, relief="flat",
                  font=('Arial', 12, 'bold')).grid(row=7, column=1, sticky='news', padx=5, pady=8)
            Label(right, text=result[9], bg='#A8D59D', fg='black', borderwidth=2, relief="flat",
                  font=('Arial', 12, 'bold')).grid(row=7, column=2, sticky='news', padx=5, pady=8)
            Label(left, text='Attendance:\n' + str(percent)+'%', fg='white', bg='#007534', font=('Arial', 12, 'bold')).grid(
                row=1, column=0, sticky='news', padx=5,pady=(10,0))

            Button(left, image=self.reportImage,width=30,height=30,bg='#007534',command=handler).grid(row=2, column=0, padx=5,pady=5)
            self.studentWindow.grid_columnconfigure(0, weight=1)
            self.studentWindow.grid_columnconfigure(1, weight=3)
            left.grid_columnconfigure(0, weight=1)
            left.grid_rowconfigure((0,3),weight=1)
            right.grid_columnconfigure((0, 1, 2), weight=1)
            right.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
            self.studentWindow.grid_rowconfigure(1, weight=1)
        except IndexError:
            messagebox.showinfo('Info', 'If no student was selected, the overall class attendance is displayed')
            connection = sqlite3.connect('Main Database')
            crsr = connection.cursor()
            crsr.execute('''select * from Attendance''')
            temp = crsr.fetchall()
            attendResult = []
            count = 0
            tempAdd = []
            for i in temp:
                attendResult.append(i)
            for i in range(len(attendResult)):
                mock = []
                for x in attendResult[i]:
                    mock.append(x)
                del mock[0]
                del mock[0]
                tempAdd = tempAdd + mock
            # Initiates a counter to keep track of the number of absents the student has, as well as the number of
            # times the student has been present
            crsr.execute('''select * from Attendance''')
            temp2 = crsr.fetchone()
            atTemp = []
            for i in temp2:
                atTemp.append(i)
            daysCounter = len(atTemp)
            Acounter = 0
            for x in tempAdd:
                if x == 'A':
                    Acounter += 1
            Acounter = (len(attendResult))/Acounter
            # Calculates the ratio of absent to total number of sessions, and converts the fraction into a percentage
            percent = int(round(((daysCounter - Acounter) / daysCounter) * 100))
            messagebox.showinfo('Class Attendance','Overall class attendance is '+str(percent)+'%')

    def report(self,name=None,id=None):
        if (name == None) and (id ==None):
            # Returns an error if no student was selected
            messagebox.showerror('Error','No student found')
        else:
            if name == None:
                currentStudent = id
                handler = lambda: self.reportSave(None,currentStudent)
            elif id == None:
                currentStudent = name
                handler = lambda: self.reportSave(currentStudent,None)
            # Creates the report window
            self.Report = Toplevel(self.studentWindow)
            self.Report.geometry('435x120')
            self.Report.title('Report')
            self.Report.configure(bg='#007534')
            self.Report.resizable(False,False)
            self.reportText = Text(self.Report,width=60,height=7,font=('Arial',10))
            self.reportText.grid()
            self.reportText.bind("<Key>",self.check)
            menubar = Menu(self.Report)
            menubar.add_command(label='Save',command = handler)
            self.Report.config(menu=menubar)
            try:
                # Tries to retrieve reports from the database to allow teachers to be able to edit them
                conn = sqlite3.connect('Main Database')
                crsr = conn.cursor()
                if name == None:
                    crsr.execute('select Report from Reports where SID=?',(currentStudent,))
                elif id == None:
                    crsr.execute('select Report from Reports where SName=?', (currentStudent,))
                toAdd = crsr.fetchone()
                toAdd = toAdd[0][::]
                self.reportText.insert('1.0',toAdd)
            except:
                pass

    def check(self,event):
        checkL = self.reportText.get("1.0","end-1c")
        checker = [59,119,179,239,299,359]
        if len(checkL) in checker:
            self.reportText.insert(INSERT,'\n')
        if len(checkL)>413:
            self.reportText.delete('7.58')

    def reportSave(self,name=None,id=None):
        # Creating the table for the report files and add populating the table
        conn = sqlite3.connect('Main Database')
        crsr = conn.cursor()
        crsr.execute('create table if not exists Reports(SID INTEGER PRIMARY KEY ,SName TEXT,Report TEXT);')
        conn.commit()
        crsr.execute('SELECT SFirst_Name,SLast_Name FROM Student_Table')
        # Retrieves the list of students from the original student table
        mainStudentList = crsr.fetchall()
        tempListA = []
        for i in mainStudentList:
            tempListA.append(i[0][::] + ' ' + i[1][::])
        mainStudentList = tempListA
        tempListB = []
        crsr.execute('SELECT SName FROM Reports')
        # Retrieves the list of students from the attendance table
        atStudentList = crsr.fetchall()
        for i in atStudentList:
            tempListB.append(i[0][::])
        atStudentList = tempListB
        toAdd = []
        for i in mainStudentList:
            if not any(x == i for x in atStudentList):
                toAdd.append(i)
        for i in toAdd:
            tempN = i
            crsr.execute('INSERT INTO Reports(SName) VALUES(?)', (tempN,))
            conn.commit()
        # Saving report text into the database
        toSave = self.reportText.get("1.0","end-1c")
        if name == None:
            crsr.execute('update Reports SET Report =? WHERE SID =?',(toSave,id,))
            conn.commit()
            messagebox.showinfo('Success','Report successfully saved')
            self.Report.destroy()
        elif id == None:
            crsr.execute('update Reports SET Report =? WHERE SName =?', (toSave, name,))
            conn.commit()
            messagebox.showinfo('Success', 'Report successfully saved')
            self.Report.destroy()

if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    app = StudentTracker(root)
    root.mainloop()
