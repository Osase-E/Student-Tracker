import sqlite3
from tkinter import *
from tkinter import messagebox
import re
import smtplib

class LoginWindow(object):
          def __init__(self,master):
                    global forgotP
                    global first
                    self.master=master
                    self.master.title('Login')
                    self.master.configure(bg='#4f8305')
                    self.photo = PhotoImage(file = 'Logo.gif')
                    self.SchoolLogo = Label(self.master, image = self.photo,bg = 'white').grid(row=0,column=0,columnspan=4,sticky=W+E)
                    #This opens the main database and creates the teacher login table
                    #to store the login details of each teacher
                    connection = sqlite3.connect('Main Database')
                    crsr = connection.cursor()
                    crsr.execute("""CREATE TABLE IF NOT EXISTS Teacher_Login(
                    User_ID INTEGER PRIMARY KEY, Username VARCHAR(20),Password VARCHAR(20) NOT NULL,
                    Teacher_FID INTEGER, Email VARCHAR(100) NOT NULL,
                    FOREIGN KEY(Teacher_FID) REFERENCES Teacher_Table(Teacher_ID));""")
                    connection.commit()
                    connection.close()
                    #This is the frame for the main login screen
                    first = Frame(self.master,bg='#4f8305')
                    first.grid()
                    #Here,I will be creating login widgets
                    self.usernameL=Label(first, text='Username',bg='#4f8305',fg='white',font=('Arial',12,'bold'))
                    self.passwordL=Label(first, text='Password',bg='#4f8305',fg='white',font=('Arial',12,'bold'))
                    self.usernameE=Entry(first)
                    self.passwordE=Entry(first,show='*')
                    self.loginButton=Button(first, text='Submit', command=self.login,bg='#B3FF00')
                    self.newUserButton=Button(first, text='New User?',command=self.newUser,bg='#4f8305',relief=FLAT,font=('Arial',10,'bold','underline'),fg='#B3FF00')
                    self.forgotButton=Button(first, text='Forgot Password?', command=self.forgot,bg='#4f8305',relief=FLAT,font=('Arial',10,'bold','underline'),fg='#B3FF00')
                    self.line1=Label(first,bg='#4f8305').grid(row=1,column=0)
                    self.usernameL.grid(row=2,column=1,sticky=W)
                    self.usernameE.grid(row=3,column=1,columnspan=2,sticky=W)
                    self.passwordL.grid(row=4,column=1,sticky=W)
                    self.passwordE.grid(row=5,column=1,columnspan=2,sticky=W)
                    self.line2=Label(first,bg='#4f8305').grid(row=6,column=0)
                    self.loginButton.grid(row=7,column=1,columnspan=2)
                    self.line3=Label(first,bg='#4f8305').grid(row=8,column=0)
                    self.newUserButton.grid(row=9,column=3)
                    self.forgotButton.grid(row=9,column=0)
                    #This is the frame for the forgot password screen
                    forgotP = Frame(self.master,bg='#4f8305')
                    self.emailFL= Label(forgotP,text='Enter the Email used to register the account',bg='#4f8305',fg='white',font=('Arial',12,'bold'))
                    self.emailFE=Entry(forgotP)
                    self.emailBtn=Button(forgotP, text='Back',command=self.back,bg='#B3FF00')
                    self.emailSend=Button(forgotP,text='Send',command=self.send,bg='#B3FF00')
                    self.line1=Label(first,bg='#4f8305').grid(row=1,column=0)
                    self.emailFL.grid(row=2,column=1)
                    self.emailFE.grid(row=3,column=1,columnspan=3)
                    self.line2=Label(first,bg='#4f8305').grid(row=4,column=0)
                    self.emailSend.grid(row=5,column=1,columnspan=2)
                    self.line3=Label(first,bg='#4f8305').grid(row=6,column=0)
                    self.emailBtn.grid(row=7,column=0)

          def login(self):
                    username=self.usernameE.get()
                    pswd=self.passwordE.get()
                    connection = sqlite3.connect('Main Database')
                    crsr = connection.cursor()
                    crsr.execute('''SELECT * from Teacher_Login WHERE Username=? AND Password=?''',(username,pswd,))
                    connection.commit()
                    if crsr.fetchone() is not None:
                    #This returns a confirmation if the user's details match, and will redirect them to the main page once that has been coded 
                              messagebox.showinfo('Welcome','Welcome back')
                    else:
                    #This returns an error message if the login details do not match
                              messagebox.showerror('Error', 'Login Failed')

                    
          def newUser(self):
                    self.master.withdraw()
                    #This loads the window that allows the user to create a new account
                    createAccount = Toplevel()
                    createAccount.title('Create an Account')
                    self.usernameL=Label(createAccount, text='Username')
                    self.passwordL=Label(createAccount, text='Password')
                    self.usernameEC=Entry(createAccount)
                    self.passwordEC=Entry(createAccount,show='*')
                    self.passwordLC=Label(createAccount,text='Confirm Password')
                    self.passwordECC=Entry(createAccount,show='*')
                    self.emailL=Label(createAccount, text='Email Address')
                    self.emailE=Entry(createAccount, width='60')
                    self.teacherCodeL=Label(createAccount,text='Teacher Code')
                    self.teacherCodeE=Entry(createAccount)
                    self.createButton=Button(createAccount, text='Create',command=self.create)
                    #handler passes on the 'createAccount' variable to the close function
                    handler = lambda: self.closewindow(createAccount)
                    self.closebutton=Button(createAccount, text='Close',command=handler)
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
                    self.createButton.pack()
                    self.closebutton.pack()
                    
          def closewindow(self,createAccount):
                    createAccount.destroy()
                    self.master.update()
                    self.master.deiconify()
                    
          def forgot(self):
                    global forgotP
                    global first
                    #Packs the forgot password frame to allow user interaction
                    self.master.title('Forgot Password')
                    first.grid_forget()
                    forgotP.grid()
                    
          def back(self):
                    global forgotP
                    global first
                    #Unpacks the forgot password frame and brings up the login frame
                    self.master.title('Login')
                    first.grid()
                    forgotP.grid_forget()

          def send(self):
                    connection = sqlite3.connect('Main Database')
                    crsr = connection.cursor()
                    try:
                        sender = 'sydneyrusselltracker@gmail.com'
                        receive = self.emailFE.get()
                        subject='Login Details'
                        crsr.execute('''SELECT Password FROM Teacher_Login WHERE Email=?''',(receive,))
                        userpass= crsr.fetchone()
                        if crsr.fetchone() is None:
                              messagebox.showinfo('Error','Email Address does not exist')
                        else:
                            userpass=userpass[0][::]
                            print(userpass)
                            crsr.execute('''SELECT Username FROM Teacher_Login WHERE Email=?''',(receive,))
                            useruser = crsr.fetchone()
                            useruser=useruser[0][::]
                            print(useruser)
                            message =(
                    '''This is in response to your password request, please find attached your login details:
                            Username = %s
                            Password = %s''')%(useruser,userpass)       
                            msg = 'From: %s\r\nTo: %s\r\nSubject: %s\r\nX-Mailer: My-Mail\r\n\r\n' %(sender,receive,subject)
                            mail = smtplib.SMTP('smtp.gmail.com',587)
                            mail.ehlo()
                            mail.starttls()
                            mail.login(sender, '6Monkeys?')
                            mail.sendmail(sender, receive, msg+(message))
                            mail.close()
                            messagebox.showinfo('Success!', 'An email has been sent to %s with the login details' % (receive))
                    except smtplib.SMTPException:
                        messagebox.showinfo('Error', 'Please ensure you have typed the correct email address')
                    return

                    
          def create(self):
                    addUser=True
                    connection=sqlite3.connect('Main Database')
                    crsr=connection.cursor()
                    usernameC=self.usernameEC.get()
                    passwordC=self.passwordEC.get()
                    email=self.emailE.get()
                    code=self.teacherCodeE.get()
                    #Checks the password entered if it matches the requirements specified
                    while addUser==True:
                        if ((len(passwordC)>8)and(re.search("[a-z]",passwordC))and(re.search("[0-9]",passwordC))
                        and (re.search("[A-Z]",passwordC))and(re.search("[$#@.!£]",passwordC)) and not(re.search("\s",passwordC))):
                                  addUser=True
                        else:
                                  messagebox.showerror('Error',
    '''Your password must contain at least:
          • 1 Uppercase letter and Lowercase
          • a symbol from [$#@.!£]
          • a number [0-9]
          • 8 characters''')
                                  addUser=False
                                  break
                        #When the password has been verified to match the criteria, it goes on to check if the two passwords match
                        if self.passwordEC.get() == self.passwordECC.get():
                                    addUser=True
                        else:
                                    messagebox.showerror('Oops!','Your Passwords do not match')
                                    addUser=False
                                    break

                        crsr.execute('''SELECT * FROM Teacher_Login WHERE Username=?''',(usernameC,))
                        connection.commit()
                        #Once the passwords match, the program can then check the username for a duplicate in the database
                        if crsr.fetchone() is None:            
                                  addUser=True
                        else:
                                  messagebox.showerror('Error', 'Sorry! Someone already has that Username. Try using a different one')
                                  addUser=False
                                  break
                        #To ensure the forgot password section of the program does not crash when the user enters their email address, the program will check that the email address
                        #is in a particular format
                        match=re.search(r"([^@|\s]+@[^@]+\.[com|org]{3}$)",email,re.I)
                        if match:
                                addUser=True
                        else:
                                messagebox.showerror('Error','Please enter a valid email address in the form: \"emailaddress@email.com\"')
                                addUser=False
                                break
                        
                        if addUser==True:
                            crsr.execute('''INSERT INTO Teacher_Login(Username,Password,
                            Email, Teacher_FID) VALUES (?,?,?,?)''',(usernameC,passwordC,email,code,))
                            connection.commit()
                            messagebox.showinfo('Success!','''You have successfully created an account.
                            \nYou may now close the window using the close button to return to the previous screen''')
                            #Inserts all the data the user has entered into the Teacher_Login table
                            addUser=False
                        

if __name__ == "__main__":
    root = Tk()
    root.geometry("425x350")
    app = LoginWindow(root)
    root.mainloop()

                    
