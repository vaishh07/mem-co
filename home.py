from tkinter import *
import login

def signin():
    login.root.mainloop()


# Create the main window
root = Tk()
root.title('Home')
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False,False)

# Add an image of your choice
img = PhotoImage(file='./blogs/logo1.png')
label1 = Label(root,image=img,bg='white').place(x=35,y=35)


# Add some buttons to navigate to other pages
frame = Frame(root, width=350,height=390,bg='#fff')
frame.place(x=480,y=50)

# Add a welcome message label
heading=Label(frame,text='Jump to you favourite spot !',fg='green',bg='white',font=('Microsoft YaHei UI Light',15,'bold'))
heading.place(x=65,y=5)

games_button = Button(frame, text='Play Games',border=0, font=('Microsoft YaHei UI Light',15), fg='green', bg='white')
games_button.place(x=130,y=80)

blogs_button = Button(frame, text='Read Blogs', border=0,font=('Microsoft YaHei UI Light',15), fg='green', bg='white')
blogs_button.place(x=130,y=150)

todo_button = Button(frame, text='To Do List',border=0, font=('Microsoft YaHei UI Light',15), fg='green', bg='white')
todo_button.place(x=132,y=220)

label = Label(frame,text="Don't leave us!",fg='black',bg='white',font=('Microsoft YaHei UI Light',11))
label.place(x=140,y=315)

log_out_button = Button(frame,text='LogOut',border=0, font=('Microsoft YaHei UI Light',10), fg='green', bg='white',command = signin)
log_out_button.place(x=165,y=340)



# Run the main event loop
root.mainloop()
