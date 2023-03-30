from tkinter import *
from tkinter import messagebox
import ast
import register
import home

root=Tk()
root.title('Login')
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False,False)

def signin():
    username=user.get()
    password=psw.get()

    if username == 'admin' and password == '1234':
        home.root.mainloop()

    elif username !='admin' and  password != '1234':
        messagebox.showerror("Invalid username or password") 

def signup_command():
    register.window.mainloop()


img = PhotoImage(file='./blogs/logo1.png')
label1 = Label(root,image=img,bg='white').place(x=35,y=35)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in',fg='green',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
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
    name=psw.get()
    if name =='':
        psw.insert(0,'Password')


psw = Entry(frame,width=25,fg='green',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
psw.place(x=30,y=150)
psw.insert(0,'Password')
psw.bind('<FocusIn>',on_enter)
psw.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)


#login button
Button(frame,width=39,pady=7,text='Sign In',bg='green',fg='white',border=0,command=signin).place(x=35,y=204)
label = Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',11))
label.place(x=70,y=270)
sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='green',font=('Microsoft YaHei UI Light',11),command=signup_command)
sign_up.place(x=240,y=267)


root.mainloop()