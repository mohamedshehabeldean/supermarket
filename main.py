from tkinter import *
from tkinter import messagebox
import webbrowser
import sys
import os


var = Tk()


var.geometry('800x460+350+200')

def open1():
    webbrowser.open('https://www.facebook.com/profile.php?id=100048432642443')

def open2():
     webbrowser.open('https://www.instagram.com/hamadahelaleg/')

def information1():
     messagebox.showinfo(' BFCAI')

def information2():
     messagebox.showinfo(' سوبر ماركت بأستخدام البايثون               ')

def login():
    user = en1.get()
    user_id = en2.get()
    if user == 'mohamed' and user_id == '123456':
        messagebox.showinfo('مرحبا بك في سوبر ماركت المتوكل                  ')
    else:
        messagebox.showerror('لقد قمت التسجيل بطريقة خاطئة حاول مرة اخري               ')

var.resizable(False, False)
var.title('سوبر ماركت المتوكل')
var.iconbitmap('C:\\Users\\mohamed sabry\\Desktop\\Inipagi-Business-Economic-Store.ico')
title = Label(var, text='Super Market System', fg='gold', bg='black', font=('tajawal', 16, 'bold'))
title.pack(fill=X)
fr1 = Frame(var, width=230, height=440, bg='#0B2F3A')
fr1.place(x=570, y=34)
title1 = Label(fr1, text='    مرحبا بك   ', bg='#0B2F3A', fg='white', font=('tajawal', 16, 'bold'), width=10)
title1.place(x=65, y=10)
title2 = Label(fr1, text='وسائل الاتصال بنا', bg='#0B2F3A', fg='white', font=('normal', 18, 'bold'), width=10)
title2.place(x=55, y=50)
b1 = Button(fr1, text='حسابنا علي فيسبوك', width=26, fg='black', bg='#BDA901', cursor='mouse', command=open1)
b1.place(x=20, y=150)
b2 = Button(fr1, text='حسابنا علي الانستجرام', width=26, fg='black', bg='#BDA901', cursor='mouse', command=open2)
b2.place(x=20, y=200)
b3 = Button(fr1, text='لمحة عن المشروع', width=26, fg='black', bg='#BDA901', cursor='mouse', command=information2)
b3.place(x=20, y=250)
b4 = Button(fr1, text='لمحة عن المبرمج', width=26, fg='black', bg='#BDA901', cursor='mouse', command=information1)
b4.place(x=20, y=300)
photo = PhotoImage(file="E:\\sup.png")
mad = Label(var, image=photo)
mad.place(x=120, y=40, width=450, height=395)
b5 = Button(fr1, text='تسجيل الخروج', width=26, fg='black', bg='#BDA901', cursor='mouse', command=quit)
b5.place(x=20, y=345)

f2 = Frame(var, width=570, height=120, bg='#0B2F3A')
f2.place(x=0, y=350)
photo1 = PhotoImage(file="E:\\loginnn.png")
mad1 = Label(var, image=photo1)
mad1.place(x=440, y=355, width=130, height=95)
l1 = Label(f2, text='اسم المستخدم', fg='gold', bg='#41627E', font=('tajawal', 12, 'bold'))
l1.place(x=315, y=15)
l2 = Label(f2, text='  هوية الشخص', fg='gold', bg='#41627E', font=('tajawal', 12, 'bold'))
l2.place(x=315, y=50)
en1 = Entry(f2, font=('tajawal', 12, 'bold'), justify='center')
en1.place(x=105, y=17)
en2 = Entry(f2, font=('tajawal', 12, 'bold'), justify='center')
en2.place(x=105, y=50)
b6 = Button(f2, text='تسجيل الدخول', bg='#1589FF', font=('tajawal', 12), width=12, height=1,command=login)
b6.place(x=170, y=77)



var.mainloop()
