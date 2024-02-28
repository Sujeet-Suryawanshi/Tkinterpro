import tkinter
import mysql.connector
from tkinter import *
#from tkinter import messagebox
from PIL import Image,ImageTk
con = mysql.connector.connect(host="localhost", user="root", password="root")

cur = con.cursor(buffered=True)

try:
    cur.execute("CREATE DATABASE IF NOT EXISTS registration")
except:
    pass

cur.execute("USE registration")

try:
    cur.execute("DESCRIBE persons")
except:
    cur.execute(
        "CREATE TABLE persons(id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(20), Age INT, Email_id VARCHAR(30), Mobile_No VARCHAR(10), Gender VARCHAR(6), City VARCHAR(15))")

def Registration():
    cur.execute(f"INSERT INTO persons (Name, Age, Email_id, Mobile_No, Gender, City) VALUES ('{en1.get()}', '{en2.get()}', '{en3.get()}', '{en4.get()}', '{en5.get()}', '{en6.get()}')")
    con.commit()

# def mass():
#     name=en1.get()
#     age=en2.get()
#     emai=en3.get()
#     mobi=en4.get()
#     gender=en5.get()
#     city=en6.get()

#     if not name or not age or not emai or not mobi or not gender or not city:
#         messagebox.showerror("Error", "Please fill in all fields.")
#         return



#     messagebox.showinfo("Name    ",name)
#     messagebox.showinfo("Age     ",age)
#     messagebox.showinfo("Email ",emai)
#     messagebox.showinfo("Mobile ",mobi)
#     messagebox.showinfo("Gender  ",gender)
#     messagebox.showinfo("City ",city)

def Clear():
    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    en4.delete(0, END)
    en5.delete(0, END)
    en6.delete(0, END)

win = tkinter.Tk()
win.geometry("1366x768")
win.title('Person Registration')

image=Image.open("sujit.jpg")
photo=ImageTk.PhotoImage(image)
lab=Label(win,image=photo)


l0 = Label(win, text="REGISTRATION DETAILS", font=("arial ",40,"bold" ),background="light blue",foreground="#6959CD",relief="raised",border=10)


l1 = Label(win, text="Name          :", font=("arial ",23,"bold" ),bg="powder blue",relief="groove",border=4)
l2 = Label(win, text="Age             :", font=("arial ",23,"bold" ),bg="powder blue",relief="groove",border=4)
l3 = Label(win, text="Email_id     :", font=("arial ",23,"bold" ),bg="powder blue",relief="groove",border=4)
l4 = Label(win, text="Mobile_No  :", font=("arial ",23,"bold" ),bg="powder blue",relief="groove",border=4)
l5 = Label(win, text="Gender       :", font=("arial ",23,"bold" ),bg="powder blue",relief="groove",border=4)
l6 = Label(win, text="City             :", font=("arial ",23,"bold" ),bg="powder blue",relief="groove",border=4)

l0.place(x=300,y=50)
l1.place(x=200, y=150)
l2.place(x=200, y=200)
l3.place(x=200, y=250)
l4.place(x=200, y=300)
l5.place(x=200, y=350)
l6.place(x=200, y=400)

en1 = Entry(win, width=30, bd=5, font=("arial ",20,"bold" ),justify="center",bg="powder blue")
en2 = Entry(win, width=30, bd=5, font=("arial ",20,"bold" ),justify="center",bg="powder blue")
en3 = Entry(win, width=30, bd=5, font=("arial ",20,"bold" ),justify="center",bg="powder blue")
en4 = Entry(win, width=30, bd=5, font=("arial ",20,"bold" ),justify="center",bg="powder blue")
en5 = Entry(win, width=30, bd=5, font=("arial ",20,"bold" ),justify="center",bg="powder blue")
en6 = Entry(win, width=30, bd=5, font=("arial ",20,"bold" ),justify="center",bg="powder blue")

en1.place(x=400, y=150)
en2.place(x=400, y=200)
en3.place(x=400, y=250)
en4.place(x=400, y=300)
en5.place(x=400, y=350)
en6.place(x=400, y=400)

but = Button(win, text="SUBMIT ",font="arial 15", command=Registration,fg="black",bg="#6959CD",bd=12)
but.place(x=475, y=540, width=100)

butClear = Button(win, text="CLEAR ",font="arial 15", command= Clear,fg="black",bg="#6959CD",bd=12)
butClear.place(x=325, y=540, width=100)
lab.pack()
win.mainloop()




