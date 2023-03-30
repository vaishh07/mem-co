from tkinter import *
from tkinter import messagebox
import ast
import login

window=Tk()
window.title("Sign Up")
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False,False)

def signup():
    username=user.get()
    password=psw.get()
    confirm_password=c_psw.get()

    if password == confirm_password :
        try :
            messagebox.showinfo('Signup',"Successful sign up")
            window.destroy()
        except :
            print("Exception")

    else :
        messagebox.showerror('Invalid',"Invalid Username or Password")

def sign():
    login.root.mainloop()
    

img = PhotoImage(file='./blogs/logo1.png')
Label(window,image=img,border=0,bg='white').place(x=35,y=35)

frame=Frame(window,width=350,height=390,bg='#fff')
frame.place(x=480,y=50)

heading=Label(frame,text='Sign up',fg='green',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

#username
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name =='':
        user.insert(0,'Username')

user = Entry(frame,width=25,fg='green',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

#password
def on_enter(e):
    psw.delete(0,'end')

def on_leave(e):
    if psw.get() =='':
        user.insert(0,'Password')

psw = Entry(frame,width=25,fg='green',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
psw.place(x=30,y=150)
psw.insert(0,'Password')
psw.bind('<FocusIn>',on_enter)
psw.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)


#confirmpasssword
def on_enter(e):
    c_psw.delete(0,'end')

def on_leave(e):
    if c_psw.get() =='':
        user.insert(0,'Confirm Password')

c_psw = Entry(frame,width=25,fg='green',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
c_psw.place(x=30,y=220)
c_psw.insert(0,'Confirm Password')
c_psw.bind('<FocusIn>',on_enter)
c_psw.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=255)



Button(frame,width=39,pady=7,text='Sign Up',bg='green',fg='white',border=0,command=signup).place(x=35,y=280)
label = Label(frame,text="Already have an account ?",fg='black',bg='white',font=('Microsoft YaHei UI Light',11))
label.place(x=90,y=340)
sign_in=Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='green',font=('Microsoft YaHei UI Light',11),command=sign)
sign_in.place(x=150,y=365)


window.mainloop()

