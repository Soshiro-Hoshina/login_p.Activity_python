from tkinter import *
from PIL import Image
from tkinter import messagebox


window = Tk()
window.geometry('500x400+250+100')
window.resizable(False,False)
window.title('Login')

def login():
    if userentry.get() == '' or passentry.get() == '':
        messagebox.showerror('Error','Please fill in the box')
    elif userentry.get() == 'admin' and passentry.get() == 'password':
        messagebox.showinfo('Login','Login Successfully')
        print('hello world')
    else:
        messagebox.showwarning('No user Found','Enter User Correctly')


#usernamepic = Image.open('id-card.png').resize((20,20)) image=CTkImage(dark_image=usernamepic)
username = Label(window,compound='left',text=" Username: ",font=('Arial',15))
username.place(x=75,y=150)
userentry=Entry(window,font=('times new roman',18),width=19)
userentry.place(x=181,y=150)

#password
##passwordpic = Image.open('locked.png').resize((20,20)),image=CTkImage(dark_image=passwordpic)
password = Label(window,text=" Password: ",compound='left',font=('Arial',15))
password.place(x=75,y=200)
passentry=Entry(window,font=('times new roman',19),width=19,show='*')
passentry.place(x=181,y=200)



Submit = Button(window,text='LOGIN',font=("arial",15,'bold'),command=login)
Submit.place(x=215,y=250)

window.mainloop()