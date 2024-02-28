from tkinter import *
val=""
def btnClick(number):
    global val
    val=val+str(number)
    data.set(val)

def btnclear():
    global val
    val=""
    data.set("")

def btnequals():
    global val
    result=str(eval(val))
    data.set(result)

root=Tk()
root.title("CALCULATOR_demo")
root.geometry("361x381+500+200")

data=StringVar()
display= Entry(root,justify="right",bd=30,bg="powder blue",font=("ariel",20),textvariable=data)
display.grid(row=0, columnspan=4)
# 7,8,9,+
xii=Button(root,text="7",font=("ariel",13,"bold"),bd=12,bg="pink",height=2,width=6,command=lambda:btnClick(7))
xiii=Button(root,text="8",font=("ariel",13,"bold"),bd=12,bg="pink",height=2,width=6,command=lambda:btnClick(8))
ix=Button(root,text="9",font=("ariel",13,"bold"),bd=12,bg="pink",height=2,width=6,command=lambda:btnClick(9))
add=Button(root,text="+",font=("ariel",13,"bold"),bd=12,bg="pink",height=2,width=6,command=lambda:btnClick('+'))

xii.grid(row=1,column=0)
xiii.grid(row=1,column=1) 
ix.grid(row=1,column=2)
add.grid(row=1,column=3)
#4,5,6,-
iv=Button(root,text="4",font=("ariel",13,"bold"),bd=12,bg="pink",height=2,width=6,command=lambda:btnClick(4))
v=Button(root,text="5",font=("ariel",13,"bold"),bd=12,bg="pink",height=2,width=6,command=lambda:btnClick(5))
vi=Button(root,text="6",font=("ariel",13,"bold"),bd=12,bg="pink",height=2,width=6,command=lambda:btnClick(6))
sub=Button(root,text="-",font=("ariel",13,"bold"),bd=12,bg="pink",height=2,width=6,command=lambda:btnClick('-'))

iv.grid(row=2,column=0)
v.grid(row=2,column=1) 
vi.grid(row=2,column=2)
sub.grid(row=2,column=3)
#1,2,3,x
i=Button(root,text="1",font=("ariel",13,"bold"),bd=12,bg="pink",height=2,width=6,command=lambda:btnClick(1))
ii=Button(root,text="2",font=("ariel",13,"bold"),bd=12,bg="pink",height=2,width=6,command=lambda:btnClick(2))
iii=Button(root,text="3",font=("ariel",13,"bold"),bd=12,bg="pink",height=2,width=6,command=lambda:btnClick(3))
mult=Button(root,text="x",font=("ariel",13,"bold"),bd=12,bg="pink",height=2,width=6,command=lambda:btnClick('*'))

i.grid(row=3,column=0)
ii.grid(row=3,column=1) 
iii.grid(row=3,column=2)
mult.grid(row=3,column=3)

#C,0,÷,=
c=Button(root,text="C",font=("ariel",13,"bold"),bd=12,bg="pink",height=2,width=6,command=btnclear)
b_0=Button(root,text="0",font=("ariel",13,"bold"),bd=12,bg="pink",height=2,width=6,command=lambda:btnClick(0))
divi=Button(root,text="÷",font=("ariel",13,"bold"),bd=12,bg="pink",height=2,width=6,command=lambda:btnClick('/'))
equal=Button(root,text="=",font=("ariel",13,"bold"),bd=12,bg="pink",height=2,width=6,command=btnequals)

c.grid(row=4,column=0)
b_0.grid(row=4,column=1) 
divi.grid(row=4,column=2)
equal.grid(row=4,column=3)




root.mainloop()